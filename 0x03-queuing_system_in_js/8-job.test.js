#!/usr/bin/yarn test
import sinon from 'sinon';
import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  const BIG_BROTHER = sinon.spy(console);
  const QUEUE = createQueue({ name: 'push_notification_code_test' });

  before(() => {
    QUEUE.testMode.enter(true); // Enables test mode for the queue
  });

  after(() => {
    QUEUE.testMode.clear(); // Clears test jobs
    QUEUE.testMode.exit();
  });

  afterEach(() => {
    BIG_BROTHER.log.resetHistory(); // Resets console spy
  });

  it('displays an error message if jobs is not an array', () => {
    expect(
      createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, QUEUE)
    ).to.throw('Jobs is not an array'); // Validates error for non-array input
  });

  it('adds jobs to the queue with the correct type', (done) => {
    expect(QUEUE.testMode.jobs.length).to.equal(0); // Ensures queue is empty
    const jobInfos = [
      {
        phoneNumber: '44556677889',
        message: 'Use the code 1982 to verify your account',
      },
      {
        phoneNumber: '98877665544',
        message: 'Use the code 1738 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobInfos, QUEUE); // Creates jobs
    expect(QUEUE.testMode.jobs.length).to.equal(2); // Checks job count
    expect(QUEUE.testMode.jobs[0].data).to.deep.equal(jobInfos[0]); // Validates job data
    expect(QUEUE.testMode.jobs[0].type).to.equal('push_notification_code_3'); // Validates job type
    QUEUE.process('push_notification_code_3', () => {
      expect(
        BIG_BROTHER.log
          .calledWith('Notification job created:', QUEUE.testMode.jobs[0].id)
      ).to.be.true; // Checks console log
      done();
    });
  });

  it('registers the progress event handler for a job', (done) => {
    QUEUE.testMode.jobs[0].addListener('progress', () => {
      expect(
        BIG_BROTHER.log
          .calledWith('Notification job', QUEUE.testMode.jobs[0].id, '25% complete')
      ).to.be.true; // Checks progress log
      done();
    });
    QUEUE.testMode.jobs[0].emit('progress', 25); // Emits progress event
  });

  it('registers the failed event handler for a job', (done) => {
    QUEUE.testMode.jobs[0].addListener('failed', () => {
      expect(
        BIG_BROTHER.log
          .calledWith('Notification job', QUEUE.testMode.jobs[0].id, 'failed:', 'Failed to send')
      ).to.be.true; // Checks failure log
      done();
    });
    QUEUE.testMode.jobs[0].emit('failed', new Error('Failed to send')); // Emits failure event
  });

  it('registers the complete event handler for a job', (done) => {
    QUEUE.testMode.jobs[0].addListener('complete', () => {
      expect(
        BIG_BROTHER.log
          .calledWith('Notification job', QUEUE.testMode.jobs[0].id, 'completed')
      ).to.be.true; // Check completion log
      done();
    });
    QUEUE.testMode.jobs[0].emit('complete'); // Emits complete event
  });
});

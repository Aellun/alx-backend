#!/usr/bin/yarn dev
import { Queue, Job } from 'kue';

/**
 * Creates push notification jobs from the array of job info.
 * @param {Job[]} jobs - Array of job data.
 * @param {Queue} queue - The job queue.
 */
export const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array'); // Validates input is an array
  }

  for (const jobInfo of jobs) {
    const job = queue.create('push_notification_code_3', jobInfo); // Creates a new job

    // Sets event listeners for job lifecycle events
    job
      .on('enqueue', () => {
        console.log('Notification job created:', job.id);
      })
      .on('complete', () => {
        console.log('Notification job', job.id, 'completed');
      })
      .on('failed', (err) => {
        console.log('Notification job', job.id, 'failed:', err.message || err.toString());
      })
      .on('progress', (progress, _data) => {
        console.log('Notification job', job.id, `${progress}% complete`);
      });

    job.save(); // Saves the job to the queue
  }
};

export default createPushNotificationsJobs;

#!/usr/bin/yarn dev
import { createQueue } from 'kue';

// Creates a queue for push notification jobs
const queue = createQueue({name: 'push_notification_code'});

// Creates a job with phone number and message details
const job = queue.create('push_notification_code', {
  phoneNumber: '011345670',
  message: 'Account registered succesfully',
});

// Handles job events
job
  .on('enqueue', () => {
    console.log('Notification job created:', job.id);  // Log when job is created
  })
  .on('complete', () => {
    console.log('Notification job completed');  // Log on successful completion
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');  // Log if job fails
  });

// Save the job to the queue
job.save();

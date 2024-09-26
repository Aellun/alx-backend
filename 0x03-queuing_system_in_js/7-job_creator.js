#!/usr/bin/yarn dev
import { createQueue } from 'kue';

// List of jobs with phone numbers and messages
const jobs = [
  { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153518743', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153538781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153118782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4159518782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4158718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153818782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4154318781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4151218782', message: 'This is the code 4321 to verify your account' },
];

// Creates a queue for push notification jobs
const queue = createQueue({ name: 'push_notification_code_2' });

// Loops through each job and create a notification job in the queue
for (const jobInfo of jobs) {
  const job = queue.create('push_notification_code_2', jobInfo);

  // Handles job events: enqueue, complete, fail, and progress
  job
    .on('enqueue', () => {
      console.log('Notification job created:', job.id);  // Logs job creations
    })
    .on('complete', () => {
      console.log('Notification job', job.id, 'completed');  // Logs job completion
    })
    .on('failed', (err) => {
      console.log('Notification job', job.id, 'failed:', err.message || err.toString());  // Logs job failure
    })
    .on('progress', (progress, _data) => {
      console.log('Notification job', job.id, `${progress}% complete`);  // Logs job progress
    });
  
  // Saves the job to the queue
  job.save();
}

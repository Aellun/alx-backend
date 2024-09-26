#!/usr/bin/yarn dev
import { createQueue } from 'kue';

// Creates a queue
const queue = createQueue();

// Functions to simulate sending a notification
const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber},`,
    'with message:',
    message,
  );
};

// Processes jobs in the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message); // Sends notification
  done(); // Marks job as complete
});

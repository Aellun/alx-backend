#!/usr/bin/yarn dev
import { createQueue, Job } from 'kue';

// List of blacklisted phone numbers
const BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];
const queue = createQueue();

/**
 * Sends a push notification to  users.
 * @param {String} phoneNumber - The recipient's phone number.
 * @param {String} message - The message to be sent.
 * @param {Job} job - The job instance.
 * @param {*} done - Callback function to signal completion.
 */
const sendNotification = (phoneNumber, message, job, done) => {
  let total = 2, pending = 2; // Initialize total and pending progress steps
  let sendInterval = setInterval(() => {
    if (total - pending <= total / 2) {
      job.progress(total - pending, total); // Update job progress
    }

    // Checks if phone number is blacklisted
    if (BLACKLISTED_NUMBERS.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`)); // Handles blacklisted number
      clearInterval(sendInterval); // Stop the interval
      return;
    }

    // Sends notification if not blacklisted
    if (total === pending) {
      console.log(
        `Sending notification to ${phoneNumber},`,
        `with message: ${message}`,
      );
    }

    --pending || done(); // Call done when all steps complete
    pending || clearInterval(sendInterval); // Clear interval when done
  }, 1000);
};

// Processes jobs from 'push_notification_code_2' queue with concurrency of 2
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

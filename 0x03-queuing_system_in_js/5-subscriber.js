#!/usr/bin/yarn dev
import { createClient } from 'redis';

// Creates Redis client
const client = createClient();

// Handles connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Publishes a message to a Redis channel after a delay
const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
};

// Handles successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Publish messages with different delays
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);

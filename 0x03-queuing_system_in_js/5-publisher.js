#!/usr/bin/yarn dev
import { createClient } from 'redis';

// Creates Redis client
const client = createClient();
const EXIT_MSG = 'KILL_SERVER';

// Handles connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Confirms successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Subscribes to a Redis channel
client.subscribe('holberton school channel');

// Handles incoming messages
client.on('message', (_err, msg) => {
  console.log(msg);
  if (msg === EXIT_MSG) {
    client.unsubscribe(); // Unsubscribe if kill message is received
    client.quit(); // Disconnect from Redis
  }
});

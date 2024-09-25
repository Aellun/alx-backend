#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

// Create Redis client
const client = createClient();

// Handle connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Confirm successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Set a key-value pair in Redis
const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

// Retrieve and display value of a key
const displaySchoolValue = (schoolName) => {
  client.GET(schoolName, (_err, reply) => {
    console.log(reply);
  });
};

// Initial calls to test functionality
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

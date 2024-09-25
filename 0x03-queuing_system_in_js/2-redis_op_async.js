#!/usr/bin/yarn dev
import { promisify } from 'util';
import { createClient, print } from 'redis';

// Create Redis client
const client = createClient();

// Handle connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Set a key-value pair in Redis
const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

// Get and display value of a key (using promisified GET)
const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(client.GET).bind(client)(schoolName));
};

// Main function to test functionality
async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

// Handle successful connection and run main
client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});

#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

// Creates Redis client
const client = createClient();

// Handles connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Updates a hash field with a value
const updateHash = (hashName, fieldName, fieldValue) => {
  client.HSET(hashName, fieldName, fieldValue, print);
};

// Retrieves and print all fields in a hash
const printHash = (hashName) => {
  client.HGETALL(hashName, (_err, reply) => console.log(reply));
};

// Main function to add entries to the hash and display them
function main() {
  const hashObj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  // Update hash with key-value pairs
  for (const [field, value] of Object.entries(hashObj)) {
    updateHash('HolbertonSchools', field, value);
  }

  // Prints the entire hash
  printHash('HolbertonSchools');
}

// Handle successful connection and run main
client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});

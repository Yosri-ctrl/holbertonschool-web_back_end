import redis from "redis";
import { promisify } from 'util';

const client = redis.createClient();



client.on("connect", () => {
    console.log('Redis client connected to the server');
});

client.on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error.toString()}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

const displaySchoolValue = async (schoolName) => {
	const promi = promisify(client.get).bind(client);
  const reply = await promi(schoolName);
  console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

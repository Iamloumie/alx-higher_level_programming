#!/usr/bin/node

// script that computes the number of tasks completed by user id.
// first argument is the API URL: https://jsonplaceholder.typicode.com/todos
//  Only print users with completed task usimg the request module

const request = require("request");

if (process.argv.length !== 3) {
	console.error("Usage: node 6-completed_tasks.js <API_URL");
	process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
	if (error) {
		console.error(error);
		return;
	}

	try {
		const todos = JSON.parse(body);
		const completedTasks = {};

		todos.forEach((todo) => {
			if (todo.completed) {
				completedTasks[todo.userId] = (completedTasks[todo.userId] || 0) + 1;
			}
		});

		console.log(completedTasks);
	} catch (parseError) {
		console.error("Error parsing JSON:", parseError);
	}
});

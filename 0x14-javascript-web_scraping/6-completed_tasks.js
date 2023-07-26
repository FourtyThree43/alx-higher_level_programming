#!/usr/bin/node
// Computes the number of tasks completed by user id.
const request = require('request');

const apiURL = process.argv[2];

request.get(apiURL, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const completed = {};
    const taskData = JSON.parse(body);

    taskData.forEach((task) => {
      if (task.completed) {
        completed[task.userId] = (completed[task.userId] || 0) + 1;
      }
    });
    console.log(completed);
  } else {
    console.log(`Error code: ${response.statusCode}`);
  }
});

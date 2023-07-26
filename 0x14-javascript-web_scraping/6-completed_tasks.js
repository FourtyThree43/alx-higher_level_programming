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

    for (const i in taskData) {
      const task = taskData[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log(`Error code: ${response.statusCode}`);
  }
});

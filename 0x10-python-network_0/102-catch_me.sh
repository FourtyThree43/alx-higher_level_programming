#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that get the message You got me!
curl -s -X POST -d "user_id=42" "http://0.0.0.0:5000/catch_me" | grep -o "You got me!"

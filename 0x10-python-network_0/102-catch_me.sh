#!/bin/bash
# Makes a request that causes the server to respond with a message
curl -sX PUT 0.0.0.0:5000/catch_me -L -d "user_id=98" -H "origin:HolbertonSchool"

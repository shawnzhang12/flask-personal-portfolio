#!/bin/bash
URL=http://localhost:5000/api/timeline_post
response=$(curl -v --request POST $URL -d \
'name=shawnzhang&email=xiaoen.zhang@mail.utoronto.ca&content=Testing curl results' 2>&1 | grep 'HTTP\|\"id\":')
HTTP_CODE=$(echo "$response" | tail -2 | head -1 | awk '{print $3}')
ID=$(echo "$response" | tail -n 1 | tr -d -c 0-9)
GET_RESPONSE=$(curl -v $URL 2>&1 | grep "\"id\": $ID" | wc -l)

if [[ $HTTP_CODE -eq 200 ]] 
then
    echo "Successful PUT request using curl."
else
    echo "Failed PUT request."
fi

if [[ $GET_RESPONSE -eq 1 ]] 
then
    echo "Found PUT request using GET."
else
    echo " Failed finding PUT request using GET."
fi

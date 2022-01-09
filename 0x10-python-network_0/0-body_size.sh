#!/bin/bash
# request to URL and displays size of the body of response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2

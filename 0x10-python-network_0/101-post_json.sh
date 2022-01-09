#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
curl -s "$1" -X POST -d @"$2" -H "Content-Type: application/json"

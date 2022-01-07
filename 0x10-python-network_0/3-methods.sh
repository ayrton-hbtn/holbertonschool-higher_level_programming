#!/bin/bash
# displays all HTTP methods of url

curl -s -i -X OPTIONS -L "$1"

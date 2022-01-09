#!/bin/bash
# displays all HTTP methods of url
curl -s -i -X OPTIONS -L "$1" | grep "Allow" | cut -d " " -f2-

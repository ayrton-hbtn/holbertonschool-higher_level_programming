#!/bin/bash
# request to URL and displays size of the body of response

curl -so /dev/null '$1' -w '%{size_download}\n'

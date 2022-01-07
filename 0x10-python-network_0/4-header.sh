#!/bin/bash
# sends GET req to url and a header var

curl -s --header "X-MyHeader: 123" "$1"

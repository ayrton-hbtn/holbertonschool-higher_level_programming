#!/bin/bash
# sends POST req with params to url
curl -s -X POST --data "email=test@gmail.com&subject=I will always be here for PLD" "$1"

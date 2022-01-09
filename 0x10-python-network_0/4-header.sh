#!/bin/bash
# sends GET req to url and a header var
curl -s --header "X-School-User-Id: 98" "$1"

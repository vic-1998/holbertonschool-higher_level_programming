#!/bin/bash
# Bash script that sends a request to a URL 
curl -so /dev/null --write-out "%{http_code}" "$1"

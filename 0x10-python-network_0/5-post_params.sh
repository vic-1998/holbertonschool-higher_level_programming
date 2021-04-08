#!/bin/bash
# ash script that takes in a URL, sends a POST
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"

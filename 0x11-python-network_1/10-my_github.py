#!/usr/bin/python3
"""
Python script that takes your GitHub
"""
from sys import argv
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    data = requests.get(url, auth=(argv[1], argv[2])).json()
    try:
        print(data['id'])
    except:
        print("None")

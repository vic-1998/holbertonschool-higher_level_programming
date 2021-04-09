#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST
"""
import sys
import requests


if __name__ == '__main__':
    """Search API"""
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    rq = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=rq)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")

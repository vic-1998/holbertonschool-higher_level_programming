#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
"""

if __name__ == '__main__':
    """Response header value"""
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))

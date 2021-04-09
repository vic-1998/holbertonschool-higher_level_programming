#!/usr/bin/python3
"""
Script that takes in a URL
URL and displays the value of the X-Request-Id
"""

if __name__ == "__main__":
    """Header value"""
    import urllib.request as request
    from sys import argv
    rq = request.Request(argv[1])
    with request.urlopen(rq) as r:
        print(r.headers.get('X-Request-Id'))

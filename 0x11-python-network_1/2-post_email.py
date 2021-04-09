#!/usr/bin/python3
"""
POST an email
"""

if __name__ == "__main__":
    """URL and an email, sends a POST"""
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    rq = request.Request(argv[1], data)
    with request.urlopen(rq) as r:
        print(r.read().decode('utf-8'))

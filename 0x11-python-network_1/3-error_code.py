#!/usr/bin/python3
"""
Script that takes in a URL
"""

if __name__ == "__main__":
    """Error code"""
    import urllib.error as error
    import urllib.request as request
    from sys import argv
    data = request.Request(argv[1])
    try:
        with request.urlopen(data) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))

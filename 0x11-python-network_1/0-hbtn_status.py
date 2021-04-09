#!/usr/bin/python3
"""
Script that fetches URL
"""

if __name__ == "__main__":
    """My status"""
    import urllib.request as request
    with request.urlopen('https://intranet.hbtn.io/status') as r:
        html = r.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))

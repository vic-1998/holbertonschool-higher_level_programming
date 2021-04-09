#!/usr/bin/python3
"""
Script that fetches URL
"""

if __name__ == "__main__":
    """My status"""
    import requests
    r = requests.get('https://intranet.hbtn.io/status')
    data = r.text
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))

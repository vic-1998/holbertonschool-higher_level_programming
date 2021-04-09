#!/usr/bin/python3
"""

"""

if __name__ == '__main__':
    """POST an email"""
    import requests
    from sys import argv
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)

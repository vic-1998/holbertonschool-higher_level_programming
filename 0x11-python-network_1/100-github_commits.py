#!/usr/bin/python3
"""
Python script that takes 2 arguments
in order to solve this challenge.
"""

if __name__ == '__main__':
    """Time for an interview!"""
    from sys import argv
    import requests
    data = requests.get('https://api.github.com/repos/{}/{}/commits'
                        .format(argv[2], argv[1]))
    rq = data.json()
    for commit in rq[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))

#!/usr/bin/python3
"""
script that sends a request to a URL
and displays the X-Request-Id
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    response = requests.get(url)

    # check if request was successful
    if response.status_code == 200:
        print(response.headers['X-Request-Id'])

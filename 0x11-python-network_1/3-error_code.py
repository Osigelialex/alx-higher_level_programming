#!/usr/bin/python3
"""
script that sends a request to a passed url
and handles the exceptions
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

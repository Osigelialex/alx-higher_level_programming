#!/usr/bin/python3
"""
Sends a POST request to the passed URL
with the email as a parameter and
diplays the body of the response
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    email_address = sys.argv[2]
    email = f"Your email is: {email_address}"
    response = requests.post(url, params=email)
    print(response)

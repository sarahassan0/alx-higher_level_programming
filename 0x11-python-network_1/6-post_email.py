#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays the
    value of the X-Request-Id variable found in the header of the response."""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    data = {
        'email': argv[2]
    }
    with requests.post(url, data=data) as res:
        print(res.text())
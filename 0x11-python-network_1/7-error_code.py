#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays the
    value of the X-Request-Id variable found in the header of the response."""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    with requests.get(url) as res:
        if (res.status_code >= 400):
            print(f'Error code: {res.status_code}')
        else:
            print(res.text)

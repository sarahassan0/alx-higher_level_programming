#!/usr/bin/python3
""" Sends a request to the URL and displays the body of the response """

if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    url = argv[1]
    try:
        with request.urlopen(url) as res:
            body = res.read()
            print(body.decode("utf-8"))
    except error.HTTPError as err:
        print(f"Error code: {err.code}")

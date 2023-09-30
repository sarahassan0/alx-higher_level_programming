#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    from urllib import request

    with request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        body = res.read().decode("utf-8")

        print('Body response:')
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")

#!/usr/bin/python3
"""script that takes in a letter and send a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == '__main__':
    import requests
    from sys import argv

    data = {'q': argv[1] if len(argv) > 1 else ""}

    with requests.post('http://0.0.0.0:5000/search_user', data=data) as res:
        try:
            res = res.json()
            if len(res):
                print(f'[{res.get("id")}] {res.get("name")}')
            else:
                print('No result')
        except ValueError:
            print('Not a valid JSON')

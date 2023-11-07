#!/usr/bin/python3
"""Queries the Reddit API  and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """gets the number of subscribers for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url).json()

    return res.get('data', {}).get('subscribers', 0)

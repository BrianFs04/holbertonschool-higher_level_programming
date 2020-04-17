#!/usr/bin/python3
"""Twitter Auth"""

import requests
import sys
import base64

if __name__ == '__main__':

    host_auth = "https://api.twitter.com/oauth2/token"
    cont = "{}:{}".format(sys.argv[1], sys.argv[2])
    cont_encoded = base64.b64encode(cont.encode('utf-8'))

    heads = {
        "Authorization": "Basic " + cont_encoded.decode('utf-8'),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    }

    body_reqs = {
        "grant_type": "client_credentials"
    }

    res = requests.post(host_auth, headers=heads, data=body_reqs)

    auth_reqs = {
        "Authorization": "Bearer {}".format(res.json().get("access_token"))
    }

    search_tweets = "https://api.twitter.com/1.1/search/tweets.json"

    search_heads = {
        "q": sys.argv[3],
        "result_type": "mixed",
        "count": 5
    }

    search_reqs = requests.get(search_tweets, headers=auth_reqs,
                               params=search_heads)

    tweets = search_reqs.json().get("statuses")

    for i in tweets:
        print("[{}] {} by {}".format(i.get("id"), i.get("text"),
                                     i.get("user").get("name")))

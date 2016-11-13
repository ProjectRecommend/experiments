from lxml import objectify
import requests
import sys
import re

apiurl = "http://api.lololyrics.com/0.5/getLyric"


def getLyrics(artist, track):
    try:
        payload = {'artist': artist, 'track': track}
        print(payload)
        r = requests.get(apiurl, params=payload)
        print(r)
        result = objectify.fromstring(r.text.encode("utf-8"))
        print(result)
        if result.status == 'OK':
            print('%s\n\nViews: %s\n%s' % (result.response, result.views, result.url))
        else:
            print("Not 200 ")
    except:
        print("Not OK")
        sys.exit(1)

if __name__ == "__main__":
    getLyrics("Rick Astley", "Never Gonna Give You Up")

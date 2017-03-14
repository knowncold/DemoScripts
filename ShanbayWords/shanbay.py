import json
import requests

words = raw_input("> ")
path = "https://api.shanbay.com/bdc/search/?word=" + words
sj = json.loads(requests.get(path).text)

print sj['data']['cn_definition']['defn']


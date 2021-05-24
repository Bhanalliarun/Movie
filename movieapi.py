#!/usr/bin/python3

import requests
from pprint import PrettyPrinter
pp = PrettyPrinter()

import sys,json
apiKey = sys.argv[2]
movie = sys.argv[1]
data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
params = {
't':movie,
'type':'movie',
'y':'year',
'plot':'full'
}
response = requests.get(data_URL,params=params).json()
value = response.get('Ratings')
for i in value:
    if 'Rotten Tomatoes' in i.values():
        pp.pprint("Rotten Tomatoes Movie rating: " + i.get('Value'))
        break

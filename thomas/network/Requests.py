import requests
from pprint import pprint

# Socket programming: https://realpython.com/python-sockets/

r = requests.get('https://api.spotify.com/v1/search?type=artist&q=snoop')

pprint(r.json())

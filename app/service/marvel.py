from dotenv import load_dotenv
from time import time
from model.MarvelHero import MarvelHero

import os
import hashlib
import requests

load_dotenv()

def get_hash():
    ts = int(time())
    pvt = os.getenv('PVT_KEY')
    apikey = os.getenv('API_KEY')
    
    cripto = str(ts) + pvt + apikey
    
    hash_marvel = hashlib.md5(cripto.encode()).hexdigest()
    
    return (ts, apikey, hash_marvel)


def search_marvel_heros(nameStartsWith=None):
    info_hash = get_hash()

    params = {
        "limit": 8,
        "nameStartsWith": nameStartsWith,
        "ts": info_hash[0],
        "apikey": info_hash[1],
        "hash": info_hash[2]
    }
    
    resp = requests.get('https://gateway.marvel.com:443/v1/public/characters', params)
    
    return resp.json()['data']['results']


def herois(request):
    lista = search_marvel_heros(request)
    
    return list(map(lambda heroi : MarvelHero(
        heroi['id'],
        heroi['name'],
        heroi['description'],
        heroi['thumbnail']['path']+ "." +heroi['thumbnail']['extension'],
        ), lista))
    

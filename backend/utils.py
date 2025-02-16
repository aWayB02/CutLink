import pyshorteners
import redis
from backend.main import redis

def get_short_link(link):
    shortener = pyshorteners.Shortener()

    if redis.get(link):
        short_link = redis.get(link)
    else:
        short_link = shortener.clckru.short(link)
        redis.set(link, short_link)
        
    return short_link
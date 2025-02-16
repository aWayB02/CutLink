import pyshorteners

def get_short_link(url):
    shortener = pyshorteners.Shortener()
    return shortener.clckru.short(url)
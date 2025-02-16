from fastapi import FastAPI
from pydantic import BaseModel
import pyshorteners.exceptions
from backend.utils import get_short_link
import redis

app = FastAPI()
r = redis.Redis('localhost', port=6379)


class Link(BaseModel):
    link: str


@app.post('/cutlink')
def cut_link(link: str):
    try:
        if r.get(link):
            print("я в редисе")
            short_link = r.get(link)
        else:
            print("я создал")
            short_link = get_short_link(link)
            r.set(link, short_link)
        return {
            "status": "success",
            "result": short_link
        }
    except pyshorteners.exceptions.ShorteningErrorException as e:
        return {
            "status:": "error",
            "Error": e
        }
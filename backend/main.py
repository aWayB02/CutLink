from fastapi import FastAPI
from pydantic import BaseModel
import pyshorteners.exceptions
from backend.utils import get_short_link
from redis import Redis

app = FastAPI()
redis = Redis('localhost', port=6379)


class Link(BaseModel):
    link: str


@app.post('/cutlink')
def cut_link(link: str):
    try:
        short_link = get_short_link(link)
        return {
            "status": "success",
            "result": short_link
        }
    except pyshorteners.exceptions.ShorteningErrorException as e:
        return {
            "status:": "error",
            "Error": e
        } 
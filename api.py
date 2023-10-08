from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from spacebot.spacebot import SpaceBot
from searcher.searcher import Searcher
import json

app = FastAPI()
api_bot = None
searcher = Searcher()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/init_bot")
async def init_bot(request: Request) -> JSONResponse:
    global api_bot
    try:
        if api_bot is None:
            api_bot = SpaceBot()
        else:
            api_bot.new_conversation()
        return get_welcome_msg()
    except:
        msg = "Unable to initialize the bot."
        raise HTTPException(status_code=402, detail=msg)
     

@app.post("/bot_query")
async def bot_query(request: Request, query: str = Form(...)) -> JSONResponse:
    try:
        result = api_bot.query(query)
        json_compatible_item_data = jsonable_encoder(result)
        return JSONResponse(content=json_compatible_item_data)
    except:
        msg = "Unable to get a response from the bot."
        raise HTTPException(status_code=402, detail=msg)


def get_welcome_msg() -> JSONResponse:
        result = {
            'response': "👋 Welcome to the Bookspace Recommender, my name is SpaceBot🪐. Tell me your needs and I'll recommend what better suits you!"
        }
        json_compatible_item_data = jsonable_encoder(result)
        return JSONResponse(content=json_compatible_item_data)


@app.post("/get_planet")
async def get_planet(request: Request, planet: str = Form(...)) -> JSONResponse:
    result = searcher.get_planet(planet)
    json_compatible = jsonable_encoder(result)
    return JSONResponse(content=json_compatible)


@app.post("/get_moon")
async def get_moon(request: Request) -> JSONResponse:
    result = searcher.get_moon()
    json_compatible = jsonable_encoder(result)
    return JSONResponse(content=json_compatible)

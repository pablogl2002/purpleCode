from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from spacebot.spacebot import SpaceBot
from searcher import Searcher
import json

app = FastAPI()
api_bot = None
searcher = Searcher()

@app.post("/init_bot")
async def init_bot(request: Request):
    global api_bot
    try:
        api_bot = SpaceBot()
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


@app.post("/get_planet")
async def get_planet(request: Request, planet: str = Form(...)) -> JSONResponse:
    result = searcher.get_planet(planet)
    json_compatible = jsonable_encoder(result)
    return JSONResponse(content=json_compatible)


@app.post("/get_moon")
async def get_planet(request: Request, moon: str = Form(...)) -> JSONResponse:
    result = searcher.get_moon(moon)
    json_compatible = jsonable_encoder(result)
    return JSONResponse(content=json_compatible)

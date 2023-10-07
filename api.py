from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from spacebot.spacebot import SpaceBot


app = FastAPI()
api_bot = SpaceBot()

@app.post("/bot_query")
async def bot_query(request: Request, query: str = Form(...)) -> JSONResponse:
    try:
        result = api_bot.query(query)
        json_compatible_item_data = jsonable_encoder(result)
        return JSONResponse(content=json_compatible_item_data)
    except:
        msg = "Unable to get a response from the bot."
        raise HTTPException(status_code=420, detail=msg)
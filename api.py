import json
import uvicorn

from fastapi import FastAPI
from tortoise import Tortoise
from contextlib import asynccontextmanager

import annotations
from models.bot import Bot
from utils import search_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Tortoise.init(
        db_url="sqlite://gpt.sqlite3",
        modules={"models": ["models.bot"]},
    )
    await Tortoise.generate_schemas()
    yield

    await Tortoise.close_connections()


app = FastAPI(lifespan=lifespan)


@app.get("/create")
async def create_base(filters: str, params: str):
    filters: dict = json.loads(filters)
    params: dict = json.loads(params)
    filtered = Bot.filter(**filters)
    if await filtered.first():
        return {"success": False, "data": None}
    await Bot.create(**params)
    return {"success": True, "data": await filtered.first()}


@app.get("/update")
async def update_base(filters: str, params: str):
    filters: dict = json.loads(filters)
    params: dict = json.loads(params)
    filtered = Bot.filter(**filters)
    if not await filtered.first():
        return {"success": False, "data": None}
    await filtered.update(**params)
    return {"success": True, "data": await filtered.first()}


@app.get("/delete")
async def delete_base(filters: str):
    filters: dict = json.loads(filters)
    filtered = Bot.filter(**filters)
    if not await filtered.first():
        return {"success": False, "data": None}
    await filtered.delete()
    return {"success": True, "data": await filtered.first()}


@app.get("/get")
async def get_base(filters: str):
    filters: dict = json.loads(filters)
    obj = Bot.filter(**filters)

    if await obj.first() is None:
        return {"success": False, "data": None}
    return {"success": True, "data": await obj.first()}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

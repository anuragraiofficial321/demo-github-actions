from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.items import Item, ItemCreate, ItemUpdate
from app.models.items import Item as ItemModel
from app.services.llm import generate_llm_response

router = APIRouter()

@router.post("/items/")
async def create_item(item: ItemCreate):
    # db_item = ItemModel(**item.model_dump())
    data={"name":"Anurag","description":"A test item"}
    return data

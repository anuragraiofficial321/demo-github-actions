from pydantic import BaseModel, ConfigDict
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    id: str
    name: str
    description: Optional[str] = None
    llm_response: Optional[str] = None

class ItemUpdate(ItemBase):
    name: Optional[str] = None

class Item(ItemBase):
    id: int
    llm_response: Optional[str] = None

    model_config = ConfigDict(validate_assignment=True)

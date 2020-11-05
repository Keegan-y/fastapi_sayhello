from typing import List, Optional

from pydantic import BaseModel

#--------------------- Item  ---------------------
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

#--------------------- User  ---------------------
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    messages: List[Message] = []#添加messages表

    class Config:
        orm_mode = True


# --------------------- Message  ---------------------

class MessageBase(BaseModel):
    name:str


class MessageCreate(UserBase):
    body:str


class Message(UserBase):
    id:int
    owner_id:int

    class Config:
        orm_mode = True

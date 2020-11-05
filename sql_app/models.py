from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime
#导入字段才能使用
from sqlalchemy.orm import relationship

from .database import Base

import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    messages = relationship("Message",back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

# --------------------------  message    --------------------------
class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer,primary_key = True)
    name = Column(String)
    body = Column(String)
    timestamp = Column(DateTime,default=datetime.datetime.now,index=True)

    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User",back_populates="messages")

    
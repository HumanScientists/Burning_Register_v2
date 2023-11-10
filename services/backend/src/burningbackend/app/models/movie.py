from datetime import datetime
from typing import Optional

from beanie import Document, Indexed
from pydantic.fields import Field
from pydantic import BaseModel


class Movie(Document):
    name: Indexed(str, unique=True) = Field(
        examples=["The Matrix", "The Matrix Reloaded", "The Matrix Revolutions"]
    )
    datetime: datetime
    room: str
    trailer: Optional[str] = None
    description: Optional[str] = None
    language: Optional[str] = None
    poster: Optional[str] = None
    stripe_payment: Optional[str] = None

    class Settings:
        name = "movies"


class UpdateMovie(BaseModel):
    name: Optional[Indexed(str, unique=True)] = None
    datetime: Optional[datetime] = None
    room: Optional[str] = None
    trailer: Optional[str] = None
    description: Optional[str] = None
    language: Optional[str] = None
    poster: Optional[str] = None
    stripe_payment: Optional[str] = None

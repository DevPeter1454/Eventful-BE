from datetime import datetime
from typing import Annotated, Optional, List

from pydantic import BaseModel, ConfigDict, Field

from ..core.schemas import PersistentDeletion, TimestampSchema, UUIDSchema


class EventBase(BaseModel):
    title: Annotated[str, Field(
        min_length=2, max_length=30, examples=["This is my event"])]
    about: Annotated[str, Field(min_length=1, max_length=63206, examples=[
                                "This is the content of my event."])]
    location: Annotated[Optional[str], Field(min_length=1, max_length=100, examples=[
                                             "This is the location of my event."])]
    start_time: Annotated[datetime, Field(examples=["2022-01-01T00:00:00Z"])]
    end_time: Annotated[datetime, Field(examples=["2022-01-01T00:00:00Z"])]
    agenda: Optional[str] = None
    faqs: Optional[str] = None


class Event(TimestampSchema, EventBase, UUIDSchema, PersistentDeletion):
    media_url: Annotated[
        str | None,
        Field(pattern=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$",
              examples=["https://www.eventimageurl.com"], default=None),
    ]
    created_by_user_id: int


class EventRead(BaseModel):
    id: int
    title: Annotated[str, Field(
        min_length=2, max_length=30, examples=["This is my event"])]
    about: Annotated[str, Field(min_length=1, max_length=63206, examples=[
                                "This is the content of my event."])]
    location: Annotated[str | None, Field(min_length=1, max_length=100, examples=[
                                          "This is the location of my event."])]
    start_time: Annotated[datetime, Field(examples=["2022-01-01T00:00:00Z"])]
    end_time: Annotated[datetime, Field(examples=["2022-01-01T00:00:00Z"])]
    agenda: Optional[List[str]] = None
    faqs: Optional[List[str]] = None
    media_url: Annotated[
        str | None,
        Field(pattern=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$",
              examples=["https://www.eventimageurl.com"], default=None),
    ]
    created_by_user_id: int
    created_at: datetime
    updated_at: datetime


class EventCreate(EventBase):
    model_config = ConfigDict(extra="forbid")


class EventUpdate(EventBase):
    model_config = ConfigDict(extra="forbid")

    media_url: Annotated[
        str | None,
        Field(pattern=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$",
              examples=["https://www.eventimageurl.com"], default=None),
    ] = None


class EventCreateInternal(EventCreate):
    created_by_user_id: int
    media_url: Annotated[
        str | None,
        Field(pattern=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$",
              examples=["https://www.eventimageurl.com"], default=None),
    ]


class EventUpdateInternal(EventUpdate):
    updated_at: datetime


class EventDelete(BaseModel):
    model_config = ConfigDict(extra="forbid")

    is_deleted: bool
    deleted_at: datetime

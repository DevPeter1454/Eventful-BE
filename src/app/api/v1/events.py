from typing import Annotated

from fastapi import APIRouter, Depends, Request, UploadFile, Form, File
from fastcrud.paginated import PaginatedListResponse, compute_offset, paginated_response
from sqlalchemy.ext.asyncio import AsyncSession

from ...api.dependencies import get_current_superuser, get_current_user
from ...core.db.database import async_get_db
from ...core.exceptions.http_exceptions import ForbiddenException, NotFoundException, UnprocessableEntityException
from ...core.utils.cache import cache
from ...crud.crud_users import crud_users
from ...crud.crud_events import crud_events
from ...schemas.events import EventCreate, EventCreateInternal, EventRead, EventUpdate
from ...schemas.user import UserRead
from ...core.config import settings
import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name=f"{settings.CLOUDINARY_CLOUD_NAME}",
    api_key=f"{settings.CLOUDINARY_API_KEY}",
    api_secret=f"{settings.CLOUDINARY_API_SECRET}"
)

router = APIRouter(tags=["events"])


@router.post("/{username}/event", status_code=201)
async def write_event(
    request: Request,
    username: str,
    db: Annotated[AsyncSession, Depends(async_get_db)],
    current_user: Annotated[UserRead, Depends(get_current_user)],
    event: EventCreate = Depends(),
    media: UploadFile = File(None)

):
    event_row = await crud_events.get(db=db, title=event.title)
    if event_row:
        raise ForbiddenException("Event already exists. Change the title")
    # if current_user.username != username:
    #     raise ForbiddenException(
    #         "You are not authorized to perform this action")
    print(current_user["username"])

    # if media:
    #     result = cloudinary.uploader.upload(media.file)
    # else:
    #     raise UnprocessableEntityException(
    #         "Please provide an image")

    # event_internal_dict = event.dict()
    # event_internal_dict["image_url"] = result["url"]

    # print(event_internal_dict)

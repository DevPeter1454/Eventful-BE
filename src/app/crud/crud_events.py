from fastcrud import FastCRUD

from ..models.events import Event
from ..schemas.events import EventCreateInternal, EventUpdate, EventUpdateInternal, EventDelete

CRUDEvent = FastCRUD[Event, EventCreateInternal,
                     EventUpdate, EventUpdateInternal, EventDelete]
crud_events = CRUDEvent(Event)

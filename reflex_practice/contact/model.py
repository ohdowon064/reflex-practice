from datetime import datetime
from zoneinfo import ZoneInfo

import reflex as rx
import sqlalchemy
from sqlmodel import Field

from reflex_practice.utils import get_utc_now

KST = ZoneInfo("Asia/Seoul")


class ContactModel(rx.Model, table=True):
    __tablename__ = "contacts"

    user_id: int | None = None
    first_name: str
    last_name: str | None = None
    email: str = Field(nullable=True)
    message: str
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False,
    )

from datetime import datetime
from zoneinfo import ZoneInfo

import reflex as rx
from sqlmodel import Field

from reflex_practice.common.model import CreatedAtField

KST = ZoneInfo("Asia/Seoul")


class ContactModel(rx.Model, table=True):
    __tablename__ = "contacts"

    user_id: int | None = None
    first_name: str
    last_name: str | None = None
    email: str = Field(nullable=True)
    message: str
    created_at: datetime = CreatedAtField

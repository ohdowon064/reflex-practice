from datetime import datetime

import reflex as rx
import sqlalchemy
from sqlmodel import Field

from reflex_practice.utils import get_utc_now


class BlogPostModel(rx.Model, table=True):
    __tablename__ = "blog_posts"

    subject: str
    content: str
    publish_active: bool = False

    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False,
    )
    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            "server_default": sqlalchemy.func.now(),
            "onupdate": sqlalchemy.func.now(),
        },
        nullable=False,
    )

from datetime import datetime
from typing import Self

import reflex as rx
import sqlalchemy
from sqlmodel import Field

from reflex_practice.utils import get_utc_now


class BlogPostModel(rx.Model, table=True):
    __tablename__ = "blog_posts"

    subject: str
    content: str
    publish_active: bool = False
    publish_datetime: datetime | None = Field(
        default=None,
        sa_type=sqlalchemy.DateTime(timezone=True),
        nullable=True,
    )

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

    @classmethod
    def find_all(cls, only_active: bool = True) -> list[Self]:
        with rx.session() as session:
            query = cls.select()
            if only_active:
                query = query.where(
                    cls.publish_active,
                    cls.publish_datetime <= get_utc_now(),
                )
            return session.exec(query).all()

    @classmethod
    def find_one(cls, post_id: int) -> Self | None:
        with rx.session() as session:
            query = cls.select().where(cls.id == post_id)
            return session.exec(query).one_or_none()

    @classmethod
    def create(cls, data: dict) -> Self:
        with rx.session() as session:
            post = cls(**data)
            session.add(post)
            session.commit()
            session.refresh(post)
            return post

    @classmethod
    def update(cls, post_id: int, data: dict) -> None:
        with rx.session() as db_session:
            query = BlogPostModel.select().where(BlogPostModel.id == post_id)
            post = db_session.exec(query).one_or_none()
            if post is None:
                return
            for key, value in data.items():
                setattr(post, key, value)
            db_session.add(post)
            db_session.commit()

from datetime import datetime

import reflex as rx

from reflex_practice.common.model import CreatedAtField, UpdatedAtField


class BlogPostModel(rx.Model, table=True):
    __tablename__ = "blog_posts"

    subject: str
    content: str

    created_at: datetime = CreatedAtField
    updated_at: datetime = UpdatedAtField

from datetime import datetime
from typing import Annotated

from sqlmodel import Field

from reflex_practice.utils import get_utc_now

CreatedAtField = Annotated[
    datetime,
    Field(
        default_factory=get_utc_now,
        nullable=False,
    ),
]

UpdatedAtField = Annotated[
    datetime,
    Field(
        default_factory=get_utc_now,
        sa_column_kwargs={"onupdate": get_utc_now},
        nullable=False,
    ),
]

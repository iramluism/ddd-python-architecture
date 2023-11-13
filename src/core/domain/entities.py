from abc import ABCMeta
from datetime import datetime
import uuid
from uuid import UUID

from pydantic import BaseModel
from pydantic import Field


class IEntity(BaseModel, ABCMeta):
    id: UUID = Field(default_factory=uuid.uuid4)
    modified_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)

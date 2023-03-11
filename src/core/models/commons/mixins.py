from enum import Enum

from sqlalchemy import String, Column


class AuditMixin:
    created_by: str = Column(String)
    updated_by: str = Column(String)


class BaseEnum(Enum):
    @classmethod
    def list(cls):
        return [c.value for c in cls]

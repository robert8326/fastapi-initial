from typing import Any
from sqlalchemy import create_engine, Column, Integer, Boolean, Text, DateTime, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker
from core.conf import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, expire_on_commit=True, bind=engine)


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        class_name = cls.__name__
        new_class_name = class_name[0].lower()
        for letter in class_name[1:]:
            if letter.isupper():
                new_class_name += '_' + letter.lower()
            else:
                new_class_name += letter
        return new_class_name

    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)
    deleted = Column(Boolean, default=False)
    description = Column(Text, default='')

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def save(self, db, obj):
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

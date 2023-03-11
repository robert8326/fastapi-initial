from sqlalchemy import Column, String, Boolean
from sqlalchemy_utils import ChoiceType

from core.models import Base, AuditMixin, BaseEnum


class UserRoleEnum(BaseEnum):
    admin = 'admin'
    warehouse_rep = 'warehouse_rep'
    sales_rep = 'sales_rep'
    api_engine = 'api_engine'


class User(Base, AuditMixin):
    first_name = Column(String)
    last_name = Column(String)
    image = Column(String)
    phone = Column(String)
    email = Column(String, unique=True, index=True)
    # role = Column(ChoiceType(UserRoleEnum, impl=String()))
    is_superuser = Column(Boolean, default=False)
    hashed_password = Column(String)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

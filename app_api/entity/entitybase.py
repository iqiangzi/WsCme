from app_api.database import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import AbstractConcreteBase,declared_attr
from datetime import datetime
import uuid

# Base = db.Model


def getattr_(self, name):
    if name == "Created":
        value = self.__dict__["Created"]
        return str(value)
    else:
        return getattr(self, name, None)


def to_dict(self):
    # print(self.__dict__["Created"])
    """
    model 对象转 字典
    model_obj.to_dict()
    """
    return {c.name: getattr_(self, c.name) for c in self.__table__.columns}


Base.to_dict = to_dict


class EntityBase(Base,AbstractConcreteBase):
    __abstract__ = True
    Id = Column(String(32), default=uuid.uuid4().hex, primary_key=True)
    Created = Column(DateTime, default=datetime.now())

    @declared_attr
    def __mapper_args__(cls):
        return {'polymorphic_identity': cls.__name__.lower(),
                'concrete': True} if cls.__name__ != "EntityBase" else {}
        # from app_api.entity.examination.site import Site
    # print(to_dict(Site))

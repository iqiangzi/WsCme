from app_api.database import db
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid

Base = db.Model


def getattr_(self, name):
    if name == "Created":
        print(isinstance(self.__dict__["Created"], datetime))
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


class EntityBase(Base):
    __abstract__ = True
    Id = Column(String(32), default=uuid.uuid4().hex, primary_key=True)
    Created = Column(DateTime, default=datetime.now())

    # from app_api.entity.examination.site import Site
    # print(to_dict(Site))

from app_api.database import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import AbstractConcreteBase,declared_attr,DeclarativeMeta
from datetime import datetime
import uuid




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

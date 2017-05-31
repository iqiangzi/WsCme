from app_api.database import db
from sqlalchemy import Column,NVARCHAR,String
import uuid

Base = db.Model
metdata = Base.metadata


def to_dict(self):
    """
    model 对象转 字典
    model_obj.to_dict()
    """
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


Base.to_dict = to_dict

class Role(Base):
    __tablename__ = "Roles"
    Id = db.Column(String(32), default=uuid.uuid4().hex, primary_key=True)
    RoleName = db.Column(String(64), unique=True)
    BB = Column(NVARCHAR(55))
    Users = db.relationship("User", backref='Role')

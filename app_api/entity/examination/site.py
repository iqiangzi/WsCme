"""
考场信息
"""
from sqlalchemy import Column, Integer, String, NVARCHAR, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app_api.entity.entitybase import EntityBase


class Site(EntityBase):
    """考场"""
    __tablename__ = "ExaminationSite"

    Name = Column(NVARCHAR(50), unique=True)
    Address = Column(NVARCHAR(100))
    ExaminationRooms = relationship("Room", backref="ExaminationSite")


class Room(EntityBase):
    """
    考场教室信息
    """
    __tablename__ = "ExaminationRoom"

    Name = Column(NVARCHAR(50), unique=True)
    Address = Column(NVARCHAR(100))
    PassWord = Column(String(20))
    ExaminationSiteId = Column(String(32), ForeignKey("ExaminationSite.Id"))

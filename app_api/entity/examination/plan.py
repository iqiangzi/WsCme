"""
考场安排
"""

from app_api.entity.entitybase import EntityBase
from sqlalchemy import Column, String, NVARCHAR, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship


class Plan(EntityBase):
    """
    考场安排类-场次
    """
    __tablename__ = "ExaminationPlan"

    roomId = Column(String(32), ForeignKey("ExaminationRoom.Id"))
    SelectBeginTime = Column(DateTime)
    SelectEndTime = Column(DateTime)
    ExaminationTime = Column(DateTime)
    Galleryful = Column(Integer)
    IsActive = Column(Boolean, default=False)
    ActiveTime = Column(DateTime)
    Num = Column(String(20))

    Tickets = relationship("Ticket",backref="Plan")
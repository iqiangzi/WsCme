"""准考证类"""
from app_api.entity.entitybase import EntityBase

from sqlalchemy import Column,String,NVARCHAR,ForeignKey,DateTime

class Ticket(EntityBase):
    """考生生成的准考证"""
    __tablename__="ExaminationTicket"

    Number = Column(String(20),unique=True)
    IDCard = Column(String(18))
    PlanId = Column(String(32),ForeignKey("ExaminationPlan.Id"))

    SignInTime = Column(DateTime)
    LogInTime = Column(DateTime)
    SubmitTime = Column(DateTime)
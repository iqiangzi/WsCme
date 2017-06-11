from app_api.entity.entitybase import EntityBase
from sqlalchemy import Column,String,NVARCHAR,ForeignKey,Float,TEXT

class ExamScore(EntityBase):
    __tablename__="ExaminationScore"
    TicketId = Column(String(32),ForeignKey("ExaminationTicket.Id"))
    Score = Column(Float)
    PaperContent = Column(TEXT)
    IDCard = Column(String(18))
    TicketNumber =Column(String(20))
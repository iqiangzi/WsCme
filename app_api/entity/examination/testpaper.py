from app_api.entity.entitybase import EntityBase
from sqlalchemy import Column,String,NVARCHAR,Integer,ForeignKey,Float,Boolean
from sqlalchemy.orm import relationship

class TESTPaper(EntityBase):
    __tablename__="TESTPaper"
    Name = Column(NVARCHAR(50),unique=True)
    # TESTLibraryCategoryId = Column(String(32),ForeignKey("LibraryCategory.Id"))
    """
    题型与对应数量 列表 JSON存储
    [{"CategoryId":"xxxxx-xxxx-xxxx-xxx",Type":1,"Count":10,Score:0.5},{....}]
    以上配置为 制定xxxx-xxx-xxx-xxx题库的 单选题 10道 每道0.5分
    """
    ConfigLibraryTypeofCount = Column(String(500))
    Score = Column(Float)
    PassScore = Column(Float)
    """
    自定义题 如果该项不为空 系统根据ConfigLibraryTypeCount抽取完题后会加入该设置匹配的试题
    试题会根据类别融入
    [{"Id":"xxx-xxxx-xxxx-xxxxx",Score:1.5},{.....}]
    以上配置为 指定Id的题1.5分
    """
    Custom = Column(String(500))
    """
    分发试卷是否使用缓存
    """
    DistributeCache = Column(Boolean)
    """
    交卷是否使用缓存
    """
    SubmitCache = Column(Boolean)


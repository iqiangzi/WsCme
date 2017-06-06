"""培训机构相关模型"""

from app_api.entity.manytomany import TrainingInstitutionAndCategory, TrainingInstitutionAndType
from app_api.entity.entitybase import EntityBase
from sqlalchemy import Column, NVARCHAR, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from passlib.apps import custom_app_context as pwd_context


class TrainingInstitutionCategory(EntityBase):
    """
    培训点分类字典
    标识一个培训点属于【公共科目培训】【专业协会】或者两者都是
    """
    __tablename__ = "TrainingInstitution_Category"

    Name = Column(NVARCHAR(50), unique=True)
    Desc = Column(Integer)


class TrainingInstitutionType(EntityBase):
    """
    培训点类别字典
    标识一个培训点是【专业技术人员】【公务员】或者两者都是
    """
    __tablename__ = "TrainingInstitution_Type"

    Name = Column(NVARCHAR(50), unique=True)
    Desc = Column(Integer)


class TrainingInstitution(EntityBase):
    """培训点"""
    __tablename__ = "TrainingInstitution"

    Name = Column(NVARCHAR(50), unique=True)
    Address = Column(NVARCHAR(255))
    LinkMan = Column(NVARCHAR(10))
    LinkManPhoto = Column(String(20))
    Email = Column(String(100))
    Account = relationship("TrainingInstitutionAccount", backref="TrainingInstitution")
    Category = relationship("TrainingInstitutionCategory", secondary=TrainingInstitutionAndCategory, backref="TrainingInstitution")
    Type = relationship("TrainingInstitutionType", secondary=TrainingInstitutionAndType, backref="TrainingInstitution")


class TrainingInstitutionAccount(EntityBase):
    """培训点账号"""
    __tablename__ = "TrainingInstitution_Account"

    Name = Column(NVARCHAR(50), unique=True)
    PassWordHash = Column(String(128))
    TrainingInstitutionId = Column(String(32), ForeignKey("TrainingInstitution.Id"))
    """报名点名称 如果为NULL 说明该账号只是一个培训点账号"""
    ApplyName = Column(NVARCHAR(50))
    UsbKey = Column(String(50))

    def hash_password(self, password):
        self.PassWordHash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.PassWordHash)

"""题库相关"""

from app_api.entity.entitybase import EntityBase
from sqlalchemy import Column, Enum, Integer, String, NVARCHAR, ForeignKey
from sqlalchemy.orm import relationship, backref
from app_api.entity.manytomany import TESTLibraryAndCategory
import enum



class TESTLibraryType(enum.Enum):
    SingleChoice = 1
    MultiChoice = 2
    TrueOrFalse = 3


class LibraryCategory(EntityBase):
    """题库分类"""
    __tablename__ = "TESTLibrary_Category"

    Name = Column(NVARCHAR(50), unique=True)
    PID = Column(String(32), ForeignKey("TESTLibrary_Category.Id"))
    Childs = relationship("LibraryCategory")


class TESTLibrary(EntityBase):
    __tablename__ = "TESTLibrary"

    Type = Column(Enum(TESTLibraryType))
    Answer = Column(Integer)
    Stem = Column(NVARCHAR(500), unique=True)
    Options = Column(NVARCHAR(500))
    Category = relationship("LibraryCategory",secondary=TESTLibraryAndCategory,backref="TESTLibrary")

"""题库相关"""

from app_api.entity.entitybase import EntityBase

from sqlalchemy import Column, Enum, Integer, String, NVARCHAR, ForeignKey
from sqlalchemy.orm import relationship,backref

from abc import ABCMeta, abstractmethod
from app_api.common.classtodict import to_dict

import json

LIBRARY_TYPE = ("Single-Choice", "Multi-choice", "TrueOrFalse")


class TEST(object):
    __metaclass__ = ABCMeta
    Answer = 0
    Resource = []
    LibraryType = LIBRARY_TYPE[0]
    _MediaTag = ["$MP4$", "$GIF$"]
    _MediaItem = []

    @abstractmethod
    def generateContext(self):
        return


class TESTChoice(TEST):
    def generateContext(self):
        self.Stem = ""
        self.SelectItem = []
        self.LibraryType = LIBRARY_TYPE[0]
        self._MediaItem = []


class LibraryCategory(EntityBase):
    """题库分类"""
    __tablename__ = "TESTLibraryCategory"

    Name = Column(NVARCHAR(50), unique=True)
    PID = Column(String(32), ForeignKey("TESTLibraryCategory.Id"))
    Childs = relationship("LibraryCategory", backref=backref("Parent",uselist=False),remote_side=[EntityBase.Id])


class Library(EntityBase):
    __tablename__ = "TESTLibrary"

    # Type = Column(Enum(LIBRARY_TYPE))





if __name__ == "__main__":
    choice = TESTChoice()
    choice.Stem = "sdfasdf"
    choice.generateContext()
    s = json.dumps(choice,default=lambda x:x.__dict__)
    v = json.loads(s)
    print(isinstance(s,dict))
# print(choice.generateContext())

import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType
from db import Base


class Files(Base):
    __tablename__ = "Files"
    id = Column(Integer, primary_key=True,autoincrement=True)
    file = Column(URLType,nullable=True)
    source = Column(String(30),nullable=False)
    source_id = Column(Integer,nullable=False)
    status = Column(Boolean,nullable=True)
    date = Column(DateTime,default=func.now(), nullable=False)


from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import (Column ,
 String ,
  Integer ,
   Date ,
    TIMESTAMP,
     engine,
     func)
from sqlalchemy.sql.elements import Null
from .connection import Connection


Base = declarative_base()


class Student(Base):
    __tablename__ = "member"
    memberID = Column(Integer, primary_key=True , autoincrement=True)
    first_name = Column(String(255) , nullable=True)
    last_name = Column(String(255) , nullable=True)
    image = Column(String(255))
    club_id = Column(Integer , unique=True)
    birth_data = Column(Date)
    update_at = Column(TIMESTAMP
     ,server_default=func.now()
     ,onupdate=func.cucurrent_timestamp()
    )


    def __init__(self , first_name = None , last_name = None ,birth_data = None, image = None):
     self.first_name = first_name
     self.last_name = last_name
     self.image = image
     self.birth_data = birth_data


    def __str__(self):
     pass

engine = Connection().get_connection()
Base.metadata.create_all(engine , checkfirst=True )

from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import (Column ,
 String ,
  Integer ,
   Date ,
    TIMESTAMP,
     engine,
     func)
from connection import Connection


Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    studenId = Column(Integer , primary_key=True , autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    birth_data = Column(Date)
    grade = Column(Integer)
    level = Column(Integer)
    update_at = Column(TIMESTAMP
     ,server_default=func.now()
     ,onupdate=func.cucurrent_timestamp()
    )


    def __init__(self , first_name = None , last_name = None ,birth_data = None, grade = None , level = None):
     self.first_name = first_name
     self.last_name = last_name 
     self.birth_data = birth_data
     self.grade = grade
     self.level = level

    def __str__(self):
        return self.first_name + self.last_name

engine = Connection().get_connection()
Base.metadata.create_all(engine , checkfirst=True )


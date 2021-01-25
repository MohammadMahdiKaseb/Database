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
    studenId = Column(Integer() , primary_key=True , autoincrement=True)
    frist_name = Column(String(50))
    last_name = Column(String(50))
    birth_data = Column(Date())
    grade = Column(Integer)
    level = Column()
    update_at = Column(TIMESTAMP ,
     server_default=func.now()
     ,onupdate=func.cucurrent_timestamp())


    def __init__(self , name = None , family = None , grade = None , level = None):
     self.name = name
     self.family = family 
     self.grade = grade
     self.level = level


engine = Connection().get_connection()
if not engine.dialect.has_table(engine , "student"): 
    Base.metadata.create_all(engine , checkfirst=True )
    print("Database Created")
else:
    print("Database {} exists!".format("student")) 



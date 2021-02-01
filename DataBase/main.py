from models import Student
from connection import Connection 


session = Connection().create_session()


# person1 = Student(
#     "Mobin",
#     "Ziaei" ,
#     "2024-05-02",
#     98,
#     10
# )
# session.add(person1)
# session.commit()

persons = session.query(Student).filter(Student.first_name == "Mahdi")
for person in persons:
    print(person)




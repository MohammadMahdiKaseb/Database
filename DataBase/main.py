from models import Student
from connection import Connection 


session = Connection().create_session()


# person1 = Student(
#     "test",
#     "test" ,
#     "2024-05-02",
#     98,
#     10
# )
# session.add(person1)
# session.commit()

# persons = session.query(Student).filter(Student.studenId == 1)
# for person in persons:
#     print(person)

person = session.query(Student).filter(Student.studenId == 2)
person.update({'last_name': 'test' })
session.commit() 



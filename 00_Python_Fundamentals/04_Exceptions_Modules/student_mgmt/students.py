from student_exceptions import InvalidMarksError,DuplicateIDError

class Student:
    student_id = set()
    def __init__(self,id,name,marks):
        try:
            if id in Student.student_id:
                raise DuplicateIDError(f"Student already exist with {id},{name},{marks}")
            if not all(0<= mark <= 100 for mark in marks):
                raise InvalidMarksError(f"Marks in invalid range {id},{name},{marks}")
            self.id = id
            self.name = name
            self.marks = marks
            Student.student_id.add(self.id)
        except (InvalidMarksError,DuplicateIDError) as error:
            print('Data creation failed due to ',error)
            raise
    def to_dictionary(self):
        return { 'id':self.id, 'name':self.name, 'marks':self.marks}
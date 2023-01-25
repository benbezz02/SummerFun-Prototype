import random

studentState = ["Current", "Past", "Suspended", "Pending"]


class Student:

    def __init__(self, fname, lname, ID, birthday, password, status):

        self.firstname = fname
        self.lastname = lname
        self.IDnumber = ID
        self.birthday = birthday
        self.studentID = Student.generateStudentID(self)
        self.password = password
        if status not in studentState:
            print("Invalid Status entered.")
            return
        else:
            self.status = status

    def editStatus(self, status):

        if self.status == status:
            return None
        else:
            if status not in studentState:
                print("Invalid Status entered.")
                return
            else:
                self.status = status

    def generateStudentID(self):

        StudentID = self.firstname[0] + self.lastname[0] + str(random.randrange(0, 9999))
        # print(f"Student's ID is {StudentID.lower()}")
        return StudentID.lower()

    @property
    def fname(self):
        return self.firstname

    @property
    def lname(self):
        return self.lastname

class Class:

    def __init__(self, number, year):
        self.classnumber = number
        self.year = year
        self.numStudents = 0
        self.students = []
        self.employees = []

    def addStudentToClass(self, student):
        student.status = "Current"

        self.students.append(student)

    def addEmployeeToClass(self, employee):
        employee.status = "Current"

        self.employees.append(employee)

    def printClass(self):
        print(f"Class {self.classnumber}")
        print("Students:")
        for num in range(len(self.students)):
            print(f"Student no. {num+1}: {self.students[num].firstname} {self.students[num].lastname}")
        print("Employees:")
        for num in range(len(self.employees)):
            print(f"Employee no. {num+1}: {self.employees[num].firstname} {self.employees[num].lastname}")

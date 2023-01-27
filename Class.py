import Timetables


class Class:

    def __init__(self, number, year):
        self.classnumber = number
        self.year = year
        self.maxNumStudents = 20
        self.maxNumEmployees = 4
        self.students = []
        self.employees = []
        self.timetable = Timetables.Timetable(number)
        self.events = []

    def addStudentToClass(self, student):
        if len(self.students) >= self.maxNumStudents:
            print("Too many students in this class. Please create another class or add to a different class.")
            return

        student.status = "Current"

        self.students.append(student)

    def addEmployeeToClass(self, employee):
        if len(self.employees) >= self.maxNumEmployees:
            print("Too many employees in this class. Please create another class or add to a different class.")
            return

        employee.status = "Current"

        self.employees.append(employee)

    def printClass(self):
        print(f"Class {self.classnumber}")

        if (len(self.students) == 0) and (len(self.employees) == 0):
            print("Class is empty.")
            return

        print("Students:")
        for num in range(len(self.students)):
            if self.students[num].status == "Past":
                continue
            else:
                print(f"Student no. {num + 1}: {self.students[num].firstname} {self.students[num].lastname}")

        print("\n")
        print("Employees:")
        for num in range(len(self.employees)):
            if (self.employees[num].status == "Past") or (self.employees[num].status == "Dismissed"):
                continue
            else:
                print(
                    f"Employee no. {num + 1}: {self.employees[num].__class__.__name__} {self.employees[num].firstname} {self.employees[num].lastname}")

        print("\n")

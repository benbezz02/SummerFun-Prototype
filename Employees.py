import random

employeeState = ["Current", "Past", "Dismissed", "Pending"]


class Employee:

    def __init__(self, fname, lname, ID, birthday, password, status):

        self.firstname = fname
        self.lastname = lname
        self.IDnumber = ID
        self.birthday = birthday
        self.employeeID = self.generateEmployeeID()
        self.password = password
        if status not in employeeState:
            print("Invalid Status entered.")
            return
        else:
            self.status = status

    def generateEmployeeID(self):
        EmployeeID = self.firstname[0] + self.lastname[0] + str(random.randrange(0, 9999))
        # print(f"Employee's ID is {EmployeeID.lower()}")
        return EmployeeID.lower()

    def editStatus(self, status):

        if self.status == status:
            return
        else:
            if status not in employeeState:
                print("Invalid Status entered.")
                return
            else:
                self.status = status
                return self


class Playworker(Employee):

    def __init__(self, fname, lname, ID, birthday, password, status):
        super().__init__(fname, lname, ID, birthday, password, status)


class ChildSupport(Employee):

    def __init__(self, fname, lname, ID, birthday, password, status):
        super().__init__(fname, lname, ID, birthday, password, status)


class ITSupport(Employee):

    def __init__(self, fname, lname, ID, birthday, password, status):
        super().__init__(fname, lname, ID, birthday, password, status)

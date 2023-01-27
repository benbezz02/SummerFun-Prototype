import random
import Payments

studentState = ["Current", "Past", "Suspended", "Pending"]


class Student:

    def __init__(self, fname, lname, ID, birthday, password):

        self.firstname = fname
        self.lastname = lname
        self.IDnumber = ID
        self.birthday = birthday
        self.studentID = Student.generateStudentID(self)
        self.password = password
        self.status = "Pending"
        self.pastPayments = []
        self.currentPayment = None

    def editStatus(self, status):

        if self.status == status:
            return
        else:
            if status not in studentState:
                print("Invalid Status entered.")
                return
            else:
                self.status = status
                return self

    def generateStudentID(self):

        StudentID = self.firstname[0] + self.lastname[0] + str(random.randrange(0, 9999))
        # print(f"Student's ID is {StudentID.lower()}")
        return StudentID.lower()

    def newPayment(self, amount, month, year):

        self.currentPayment = Payments.Payment(self, amount, month, year)

    def printCurrentPayment(self):

        if self.currentPayment is None:
            print(f"Student {self.firstname} {self.lastname} is up to date on payments.")
        else:
            print(f"Student {self.firstname} {self.lastname} needs to pay {self.currentPayment.amount} for {self.currentPayment.month} {self.currentPayment.year}")

    def paymentPaid(self):

        if self.currentPayment is None:
            return
        else:
            self.currentPayment.paymentPaid()
            self.currentPayment = None

    def studentPayments(self):

        Payments.Payment.printPayments(self)

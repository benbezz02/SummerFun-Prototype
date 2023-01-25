paymentState = ["Unpaid", "Paid", "Extended"]


class Payment:

    def __init__(self, student, amount, month, year):

        self.student = student
        self.amount = amount
        self.month = month
        self.year = year
        self.status = "Unpaid"

    def paymentPaid(self):
        self.status = "Paid"

        self.student.pastPayments.append(self)

        # print("Payment successful")

    def editStatus(self, status):

        if self.status == status:
            return
        else:
            if status not in paymentState:
                print("Invalid Status entered.")
                return
            else:
                self.status = status
                return self

    @staticmethod
    def printPayments(student):

        print(f"\nStudent {student.firstname} {student.lastname} has Paid:")
        for num in range(len(student.pastPayments)):
            print(f"${student.pastPayments[num].amount} for {student.pastPayments[num].month} {student.pastPayments[num].year}")

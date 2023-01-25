paymentState = ["Unpaid", "Paid", "Extended"]


class Payment:

    def __init__(self, student, amount, month, year):

        self.student = student
        self.pastPayments = []
        self.amount = amount
        self.month = month
        self.year = year
        self.status = "Unpaid"

    def addPayment(self, amount, month, year):
        self.amount = amount
        self.month = month
        self.year = year
        self.status = "Unpaid"

    def paymentPaid(self):
        self.status = "Paid"

        self.pastPayments.append(self)

        print("Payment successful")

    def editStatus(self, status):

        if self.status == status:
            return None
        else:
            if status not in paymentState:
                print("Invalid Status entered.")
                return
            else:
                self.status = status
            return 0

    def printPayments(self, student):

        for num in range(len(self.pastPayments)):
            print(f"{self.pastPayments[num].amount}, {self.pastPayments[num].status}")


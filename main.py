import Student
import Class
import Employees
import Timetables
import Payments

s1 = Student.Student("Ben", "Bezzina", "137102L", "15/04/2002", "ben1024")
s2 = Student.Student("Chris", "Azzopardi", "102088L", "05/02/2002", "ca2002")
c1 = Class.Class(9, 2022)
c1.addStudentToClass(s1)
c1.addStudentToClass(s2)
s1.editStatus("Past")


e1 = Employees.Playworker("Lilly", "Rosario", "349503M", "01/08/1972", "lillyros72", "Pending")
e2 = Employees.ChildSupport("Ellen", "Foster", "827601M", "24/06/1985", "elfoster85", "Pending")
c1.addEmployeeToClass(e1)
c1.addEmployeeToClass(e2)
c1.printClass()
e2.editStatus("Past")
c1.printClass()

p1 = Payments.Payment(s1, 18, "June", "2022")
p1.paymentPaid()


t1 = Timetables.Timetable(9)
t1.printTimetable()

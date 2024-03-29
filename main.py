import Student
import Class
import Employees
import Events
import FileManagement


students = []
employees = []
classes = []


def createStudents():
    print("Creating Students...")
    students.append(Student.Student("Ben", "Bezzina", "137102L", "15/04/2002", "ben1024"))
    students.append(Student.Student("Chris", "Azzopardi", "102088L", "05/02/2002", "ca2002"))
    students.append(Student.Student("Joanna", "Smith", "05676L", "19/08/2002", "jojo1234"))


def creatingEmployees():
    print("Creating Employees...")
    employees.append(Employees.Playworker("Lilly", "Rosario", "349503M", "01/08/1972", "lillyros72", "Pending"))
    employees.append(Employees.ChildSupport("Ellen", "Foster", "827601M", "24/06/1985", "elfoster85", "Pending"))
    employees.append(Employees.ITSupport("George", "Vella", "554961M", "20/10/1974", "g_Vella2010", "Pending"))


def classOperations():
    print("Creating Class...")
    classes.append(Class.Class(9, 2022))

    print("\n")
    classes[0].printClass()
    print("\n")

    print("Adding Students to Class...")
    classes[0].addStudentToClass(students[0])
    classes[0].addStudentToClass(students[1])
    classes[0].addStudentToClass(students[2])

    print("Adding Employees to Class...")
    classes[0].addEmployeeToClass(employees[0])
    classes[0].addEmployeeToClass(employees[1])

    print("\n")
    classes[0].printClass()


def pastStatus():
    print("Making some students and employees past...")
    students[0].editStatus("Past")
    employees[0].editStatus("Past")

    classes[0].printClass()


def paymentOperations():
    students[1].newPayment(18, "June", "2022")
    students[1].currentPaid()
    students[1].newPayment(18, "August", "2022")

    students[1].studentPayments()

    students[1].printCurrentPayment()

    print("\nPaying what needs to be paid...")
    students[1].currentPaid()

    students[1].studentPayments()

    students[1].printCurrentPayment()


def timetableOperations():
    classes[0].timetable.printTimetable()

    print("Manually inputting Timetable...\n")
    classes[0].timetable.manualInput("8:00 - Start od Day\n 8:30 - Science\n 10:00 - Break\n 11:30 - Physical Education\n 13:00 - End of Day\n",
                                     "8:00 - Start of Day\n 8:30 - ...\n",
                                     "8:00 - Start of Day\n 8:30 - ...\n",
                                     "8:00 - Start of Day\n 8:30 - ...\n",
                                     "8:00 - Start of Day\n 8:30 - ...\n")

    classes[0].timetable.printTimetable()


def eventsOperations():

    print("Creating Event...")
    event1 = Events.Event("Cinema Day", "05/07/2022", "Saint Julian's, Malta", "The classes will be going to Eden Cinemas to watch the new Puss in Boots movie.", "Upcoming")

    print("Adding Event to classes...")
    event1.addEventToClass(classes[0])
    classes[0].events[0].printEvent()
    print(classes[0].events[0].status)

    print("\nEditing Event to Completed...")
    event1.editEvent("Cinema Day", "05/07/2022", "Saint Julian's, Malta", "The classes will be going to Eden Cinemas to watch the new Puss in Boots movie.", "Completed")
    classes[0].events[0].printEvent()
    print(classes[0].events[0].status)


def fileManagement():
    print("\nUploading a file...")
    file = FileManagement.FileManagement("This is a file.")

    file.fileView()

    print("Deleting the file...")
    file.fileDelete()

    file.fileView()


createStudents()
creatingEmployees()
classOperations()
pastStatus()
paymentOperations()
timetableOperations()
eventsOperations()
fileManagement()

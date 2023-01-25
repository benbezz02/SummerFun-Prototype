import datetime


class Timetable:

    def __init__(self, classNum):

        self.classNum = classNum
        self.Monday = "8:00 - Start od Day\n" \
                      "8:30 - Science\n" \
                      "10:00 - Break\n" \
                      "11:30 - Physical Education\n" \
                      "13:00 - End of Day\n"
        self.Tuesday = "8:00 - Start of Day\n" \
                       "8:30 - ...\n"
        self.Wednesday = "8:00 - Start of Day\n" \
                         "8:30 - ...\n"
        self.Thursday = "8:00 - Start of Day\n" \
                        "8:30 - ...\n"
        self.Friday = "8:00 - Start of Day\n" \
                      "8:30 - ...\n"
        self.Saturday = "No School\n"
        self.Sunday = "No School\n"

    def printTimetable(self):

        day = datetime.datetime.now()
        day = day.strftime("%a")
        print(f"\n Timetable of {day}")

        if day == "Mon":
            print(self.Monday)
        if day == "Tue":
            print(self.Tuesday)
        if day == "Wed":
            print(self.Wednesday)
        if day == "Thu":
            print(self.Thursday)
        if day == "Fri":
            print(self.Friday)
        if day == "Sat":
            print(self.Saturday)
        if day == "Sun":
            print(self.Sunday)

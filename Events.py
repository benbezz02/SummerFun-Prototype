eventStatus = ["Upcoming", "Completed", "Cancelled"]


class Event:

    def __init__(self, name, date, location, description, status):

        self.name = name
        self.date = date
        self.location = location
        self.description = description
        if status not in eventStatus:
            print("Invalid Status entered.")
            return
        else:
            self.status = status

    def editEvent(self, name, date, location, description, status):

        if name != self.name:
            self.name = name
        if date != self.date:
            self.date = date
        if location != self.location:
            self.location = location
        if description != self.description:
            self.description = description
        if status != self.status:
            if status not in eventStatus:
                print("Invalid Status entered.")
                return
            else:
                self.status = status

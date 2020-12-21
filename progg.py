class Class:
    def __init__(self, id, depart, course):
        self._id = id
        self._depart = depart
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._room = None

    def get_id(self): return self._id
    def get_depart(self): return self._depart
    def get_course(self): return self._course
    def get_instructor(self): return self._instructor
    def get_meetingTime(self): return self._meetingTime
    def get_room(self): return self._room
    def set_instructor(self, instructor): self._instructor = instructor
    def set_meetingTime(self, meetingTime): self._meetingTime =meetingTime
    def set_room(self, room): self._room = room
    def __str__(self):
        return "{" + str(self._depart.get_name()) + "," + str(self._course.get_number()) + "," + \
               str(self._room.get_number()) + "," + str(self._instructor.get_id()) + "," + str(
            self._meetingTime.get_id()) + "}"

class Population:
    def __init__(self, size):
        self.size = size
        self.data = data
        self.sched = []
        for x in range(0, size):
            self.sch.append(sched().initialize())

    def get_sched(self):
        return self.sched
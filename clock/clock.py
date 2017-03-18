class Clock:

    def __init__(self, hours, minutes):
        self.__minutes = 0
        self.add(hours * 60 + minutes)

    def __str__(self):
        hours, minutes = divmod(self.__minutes, 60)
        return "{:02d}:{:02d}".format(hours, minutes)

    __repr__ = __str__

    def __eq__(self, other):
        return self.__minutes == other.__minutes

    def add(self, minutes):
        self.__minutes = (self.__minutes + minutes) % 1440
        return self

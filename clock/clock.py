class Clock:

    def __init__(self, hours, minutes):
        self.__minutes = minutes + (60 * hours)

    def __str__(self):
        hours = (self.__minutes // 60) % 24
        return "{:02d}:{:02d}".format(hours, self.__minutes % 60)

    __repr__ = __str__

    def __eq__(self, other):
        return self.__minutes % 1440 == other.__minutes % 1440

    def add(self, minutes):
        self.__minutes += minutes
        return self

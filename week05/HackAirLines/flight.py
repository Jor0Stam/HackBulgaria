from metadata import *


class Date:

    def __init__(self, dd=1, mm=1, yyyy=2000, hour="00:00"):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy
        self.hour = hour

    def __str__(self):
        return "{}/{}/{} - {}".format(self.dd, self.mm, self.yyyy, self.hour)

    def __repr__(self):
        return "{}/{}/{} - {}".format(self.dd, self.mm, self.yyyy, self.hour)

    def __eq__(self, other):
        return self.dd == other.dd and self.mm == other.mm and \
            self.yyyy == other.yyyy and self.hour == other.hour

    def __hash__(self):
        return hash(self.hour) * 22 / 7


class Terminal:

    def __init__(self, number, max_flights):
        self.number = number
        self.max_flights = max_flights

    def _str__(self):
        return "Terminal n.{n}".format(n=self.number)

    def __repr__(self):
        return "Terminal n.{n}".format(n=self.number)


class Flight:

    def __init__(self, start_time=Date(29, 11, 2016, hour='12:20'),
                 end_time=Date(29, 11, 2016, hour='15:30'),
                 passengers=100, max_passengers=120, from_dest="Sofia",
                 to_dest="London", terminal=Terminal(2, 30), declined=False):
        self.start_time = start_time
        self.end_time = end_time
        self.passengers = passengers
        self.max_passengers = max_passengers
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.terminal = terminal
        self.declined = declined

    def __str__(self):
        return FLIGHT_INFO.format(fr=self.from_dest, to=self.to_dest,
                                  beg=self.start_time, end=self.end_time,
                                  term=self.Terminal, stat=not self.declined)

    def __repr__(self):
        return FLIGHT_INFO.format(fr=self.from_dest, to=self.to_dest,
                                  beg=self.start_time, end=self.end_time,
                                  term=self.Terminal, stat=not self.declined)

    def __eq__(self, other):
        return self.start_time == other.start_time and \
            self.end_time == other.end_time and         \
            self.max_passengers == other.max_passengers and \
            self.passengers == other.passengers and          \
            self.to_dest == other.to_dest and self.from_dest == other.from_dest

    def __hash__(self):
        return hash(self.start_time)

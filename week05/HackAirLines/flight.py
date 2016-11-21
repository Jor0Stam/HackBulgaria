from metadata import *


class Date:

    def __init__(self, day, month, year, hour="00:00"):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and \
                self.year == other.year and self.hour == other.hour

    def __hash__(self):
        return hash(self.hash())

    def __str__(self):
        return DATE_INFO.format(d=self.day, m=self.month, y=self.year,
                                h=self.hour)

    def get_date(self):
        return (self.day, self.month, self.year)

    def get_hour(self):
        return self.hour


class Terminal:

    def __init__(self, num, max_flights):
        self.num = num
        self.max_flights = max_flights

    def __eq__(self, other):
        return self.num == other.num and self.max_flights == other.max_flights

    def __hash__(self):
        return hash(self.hash())

    def get_number(self):
        return self.num


class Flight:

    def __init__(self, start_time=Date(15, 11, 2016, "15:25"),
                 end_time=Date(15, 11, 2016, "19:00"),
                 passengers=99, max_passengers=100,
                 from_dest="Sofia", to_dest="Moscow",
                 terminal=Terminal(1, 30), declined=False):
        self.start_time = start_time
        self.end_time = end_time
        self.passengers = passengers
        self.max_passengers = max_passengers
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.terminal = terminal
        self.declined = declined

    def __eq__(self, other):
        return self.start_time == other.start_time and self.end_time == other.end_time and            \
               self.passengers == other.passengers and self.max_passengers == other.max_passengers and \
               self.from_dest == other.from_dest and self.to_dest == other.to_dest and \
               self.terminal == other.terminal and self.declined == other.declined

    def __hash__(self):
        return hash(self.hash())

    def __str__(self):
        if self.is_declined():
            return FLIGHT_DECLINED
        return FLIGHT_INFO.format(f=self.from_dest, t=self.to_dest,
                                  dt=self.start_time, at=self.end_time,
                                  p=self.passengers)

    def __repr__(self):
        if self.is_declined():
            return FLIGHT_DECLINED
        return FLIGHT_INFO.format(f=self.from_dest, t=self.to_dest,
                                  dt=self.start_time, at=self.end_time,
                                  p=self.passengers)

    def flight_from(self):
        return self.from_dest

    def flight_to(self):
        return self.to_dest

    def is_declined(self):
        return self.declined

    def get_time(self):
        return self.start_time

    def get_terminal(self):
        return self.terminal.get_number()

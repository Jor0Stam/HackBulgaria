from flight import *


class Passenger:

    def __init__(self, first_name="Rositsa", last_name="Zlateva",
                 flight=Flight(), age=22):
        self.first_name = first_name
        self.last_name = last_name
        self.flight = flight
        self.age = age

    def __eq__(self, other):
        return self.first_name == other.first_name and \
                self.last_name == other.last_name and   \
               self.flight == other.flight and self.age == other.age

    def __hash__(self):
        return hash(self.hash())

    def __str__(self):
        return PASSENGER_INFO.format(fn=self.first_name, ls=self.last_name,
                                     age=self.age, fl=self.flight)

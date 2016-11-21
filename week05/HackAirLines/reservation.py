from flight import *
from passenger import *


class Reservation:

    def __init__(self, flight=Flight(), passenger=Passenger(), accepted=True):
        self.flight = flight
        self.passenger = passenger
        self.accepted = accepted

    def __eq__(self, other):
        return self.flight == other.flight and self.passenger == other.passenger \
                and self.accepted == other.accepted

    def __hash__(self):
        return hash(self.hash())

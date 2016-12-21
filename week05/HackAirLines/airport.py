from metadata import *
from collections import defaultdict


class Airport:

    def __init__(self):
        self.flights = []
        self.reservations = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def get_flights_for(self, date):
        flights_for = []
        cnt = 0
        for fly in self.flights:
            if fly.start_time.get_date() == date.get_date():
                flights_for.append(fly)
                cnt += 1

        return [el for el in flights_for]

    def get_flights_before(self, date, hour):
        flights_before = []
        for fly in self.flights:
            if fly.start_time.get_date() == date.get_date() and \
                    fly.start_time.get_hour() < hour:
                flights_before.append(fly)

        return flights_before

    def get_flights_from_date_hour(self, destination, date):
        flights_from = []
        for fly in self.flights:
            if fly.flight_from() == destination and \
                    fly.get_time() == date:
                flights_from.append(fly)

        return flights_from

    def get_flights_from(self, destination, date=None):
        if date:
            return self.get_flights_from_date_hour(destination, date)
        flights_from = []
        for fly in self.flights:
            if fly.flight_from() == destination:
                flights_from.append(fly)

        return flights_from

    def get_flights_to(self, destination, date=None):
        if date:
            return self.get_flights_to_date_hour(destination, date)
        flights_to = []
        for fly in self.flights:
            if fly.flight_to() == destination:
                flights_to.append(fly)

        return flights_to

    def get_flights_to_date_hour(self, destination, date):
        flights_to = []
        for fly in self.flights:
            if fly.flight_to() == destination and \
                    fly.get_time() == date:
                flights_to.append(fly)

        return flights_to

    def get_terminal_flights(self):
        flights_from = defaultdict(int)
        for fly in self.flights:
            flights_from[fly.get_terminal()] += 1

        return flights_from

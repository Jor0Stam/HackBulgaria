import unittest
from flight import *
from passenger import *
from reservation import *
from airport import *

# watch -n <secs between tests> <python_ver> <file_name>.py


class TestFlight(unittest.TestCase):

    def setUp(self):
        self.flight1 = Flight(Date(15, 11, 2016, "15:25"),
                              Date(15, 11, 2016, "19:00"),
                              99, 100, "Sofia", "Moscow",
                              Terminal(1, 30), False)

    def test_flight_equal(self):
        self.assertEqual(self.flight1, Flight(Date(15, 11, 2016, "15:25"),
                                              Date(15, 11, 2016, "19:00"), 99,
                                              100, "Sofia", "Moscow",
                                              Terminal(1, 30), False))


class TestPassenger(unittest.TestCase):

    def setUp(self):
        self.passenger1 = Passenger("Rositza", "Zlateva", Flight(), 22)

    def test_eq(self):
        self.assertEqual(self.passenger1, Passenger("Rositza", "Zlateva",
                                                    Flight(), 22))


class TestReservation(unittest.TestCase):

    def setUp(self):
        self.reserv1 = Reservation(Flight(), Passenger(), True)

    def test_eq(self):
        self.assertEqual(self.reserv1, Reservation(Flight(),
                                                   Passenger(), True))


class TestAirport(unittest.TestCase):

    def setUp(self):
        self.pernik = Airport()
        self.pernik.add_flight(Flight(Date(18, 11, 2016, "10:00"),
                               Date(18, 11, 2016, "12:00"), 125, 150,
                               "Pernik", "Oslo", Terminal(1, 15), False))
        self.pernik.add_flight(Flight(Date(18, 11, 2016, "12:00"),
                               Date(18, 11, 2016, "14:00"), 130, 175,
                               "Pernik", "Warsaw", Terminal(1, 15), False))

    def test_add_flight(self):
        self.assertTrue(self.pernik.flights)

    def test_get_flights_for(self):
        self.assertTrue(self.pernik.get_flights_for(Date(18, 11, 2016,
                        "00:00")))

    def test_get_flights_before(self):
        self.assertTrue(self.pernik.get_flights_before(Date(18, 11, 2016),
                        "12:00"))

    def test_get_flight_from_dest(self):
        self.assertTrue(self.pernik.get_flights_from("Pernik"))
        self.assertFalse(self.pernik.get_flights_from("Timbuktu"))

    def test_get_flights_to_dest(self):
        self.assertTrue(self.pernik.get_flights_to("Oslo"))
        self.assertFalse(self.pernik.get_flights_to("Pernik"))

    def test_get_flights_to_dest_d_h(self):
        self.assertTrue(self.pernik.get_flights_to("Oslo", Date(18, 11, 2016,
                        "10:00")))
        self.assertFalse(self.pernik.get_flights_to("Pernik", Date(18, 11,
                         2016, "10:00")))

    def test_get_flights_from_dest_d_h(self):
        self.assertTrue(self.pernik.get_flights_from("Pernik", Date(18, 11,
                        2016, "12:00")))
        self.assertFalse(self.pernik.get_flights_from("Oslo", Date(18, 11,
                         2016, "10:00")))

    def test_get_terminal_flights(self):
        self.pernik.add_flight(Flight(Date(18, 11, 2016, "12:00"),
                               Date(18, 11, 2016, "14:00"), 130, 175,
                               "Pernik", "Warsaw", Terminal(2, 15), False))
        self.assertEqual(self.pernik.get_terminal_flights(), {1: 2,
                         2: 1})


if __name__ == "__main__":
    unittest.main()

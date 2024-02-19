"""
Tests for Reservation class
"""
import unittest
from datetime import date
from classes import Reservation, Customer, Hotel


class TestReservation(unittest.TestCase):
    """
    Test the Reservation class
    """
    def setUp(self):
        self.hotel = Hotel("Hotel ABC", "123 Main St", 200)
        self.customer = Customer("John Doe",
                                 30,
                                 "1234567890",
                                 "johndoe@example.com")
        self.reservation = Reservation(self.hotel,
                                       self.customer,
                                       101,
                                       date(2024, 1, 1),
                                       date(2024, 1, 5))

    def test_reservation_attributes(self):
        """
        Test the attributes of the Reservation class
        """
        self.assertEqual(self.reservation.hotel, self.hotel)
        self.assertEqual(self.reservation.customer, self.customer)
        self.assertEqual(self.reservation.room_number, 101)
        self.assertEqual(self.reservation.start_date, date(2024, 1, 1))
        self.assertEqual(self.reservation.end_date, date(2024, 1, 5))
        self.assertFalse(self.reservation.active)

    def test_reservation_str(self):
        """
        Test the __str__ method of the Reservation class
        """
        expected_output = "John Doe had a reservation at Hotel ABC"\
            + " from 2024-01-01 to 2024-01-05."
        self.assertEqual(str(self.reservation), expected_output)

    def test_reservation_create(self):
        """
        Test the create method of the Reservation class
        """
        self.reservation.create()
        self.assertTrue(self.reservation.active)

    def test_reservation_cancel(self):
        """
        Test the cancel method of the Reservation class
        """
        self.reservation.create()
        self.reservation.cancel()
        self.assertFalse(self.reservation.active)


if __name__ == "__main__":
    unittest.main()

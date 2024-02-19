"""
This file contains the test cases for the Hotel class.
"""
import unittest
from datetime import date
from classes import Hotel, Customer


class TestHotel(unittest.TestCase):
    """
    Test the Hotel class
    """
    def setUp(self):
        self.hotel = Hotel("Test Hotel", 10, 100.0)

    def test_hotel_attributes(self):
        """
        Test the attributes of the Hotel class
        """
        self.assertEqual(self.hotel.name, "Test Hotel")
        self.assertEqual(self.hotel.rooms, 10)
        self.assertEqual(self.hotel.rate, 100.0)

    def test_hotel_str(self):
        """
        Test the __str__ method of the Hotel class
        """
        expected_output = "Welcome to Test Hotel! We have 10 rooms available"\
            + " at $100.0 per night."
        self.assertEqual(str(self.hotel), expected_output)

    def test_create_reservation(self):
        """
        Test the create_reservation method of the Hotel class
        """
        customer = Customer("John Doe",
                            30,
                            "1234567890",
                            "johndoe@example.com")
        start_date = date(2024, 1, 1)
        end_date = date(2024, 1, 5)
        reservation = self.hotel.create_reservation(customer,
                                                    1,
                                                    start_date,
                                                    end_date)
        self.assertEqual(len(self.hotel.reservations), 1)
        self.assertEqual(reservation.hotel, self.hotel)
        self.assertEqual(reservation.customer, customer)
        self.assertEqual(reservation.room_number, 1)
        self.assertEqual(reservation.start_date, start_date)
        self.assertEqual(reservation.end_date, end_date)
        self.assertEqual(reservation.cost, 400.0)

    def test_get_reservations(self):
        """
        Test the get_reservations method of the Hotel class
        """
        customer1 = Customer("John Doe",
                             30,
                             "1234567890",
                             "johndoe@example.com")
        customer2 = Customer("Jane Smith",
                             25,
                             "0987654321",
                             "janesmith@example.com")
        start_date = date(2024, 1, 1)
        end_date = date(2024, 1, 5)
        reservation1 = self.hotel.create_reservation(customer1,
                                                     1,
                                                     start_date,
                                                     end_date)
        reservation2 = self.hotel.create_reservation(customer2,
                                                     2,
                                                     start_date,
                                                     end_date)
        reservations = self.hotel.get_reservations()
        self.assertEqual(len(reservations), 2)
        self.assertIn(reservation1, reservations)
        self.assertIn(reservation2, reservations)

    def test_get_active_reservations(self):
        """
        Test the get_reservations method of the Hotel class
        """
        customer1 = Customer("John Doe",
                             30,
                             "1234567890",
                             "johndoe@example.com")
        customer2 = Customer("Jane Smith",
                             25,
                             "0987654321",
                             "janesmith@example.com")
        start_date = date(2024, 1, 1)
        end_date = date(2024, 1, 5)
        reservation1 = self.hotel.create_reservation(customer1,
                                                     1,
                                                     start_date,
                                                     end_date)
        reservation2 = self.hotel.create_reservation(customer2,
                                                     2,
                                                     start_date,
                                                     end_date)
        reservation2.cancel()
        active_reservations = self.hotel.get_reservations(only_active=True)
        self.assertEqual(len(active_reservations), 1)
        self.assertIn(reservation1, active_reservations)
        self.assertNotIn(reservation2, active_reservations)


if __name__ == "__main__":
    unittest.main()

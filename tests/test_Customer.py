"""
Tests for the Customer class.
"""
import unittest
from classes import Customer


class TestCustomer(unittest.TestCase):
    """
    Test the Customer class
    """
    def setUp(self):
        self.customer = Customer(
            "John Doe",
            30,
            "1234567890",
            "johndoe@example.com"
            )

    def test_customer_attributes(self):
        """
        Test the attributes of the Customer class
        """
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.age, 30)
        self.assertEqual(self.customer.phone, "1234567890")
        self.assertEqual(self.customer.email, "johndoe@example.com")

    def test_customer_str(self):
        """
        Test the __str__ method of the Customer class
        """
        expected_output = "John Doe is 30 years"\
            + " old and can be reached at 1234567890"
        self.assertEqual(str(self.customer), expected_output)


if __name__ == "__main__":
    unittest.main()

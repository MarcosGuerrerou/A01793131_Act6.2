"""
Abstraction of a customer
"""


class Customer:
    """Abstraction of a customer"""
    def __init__(self, name, age, phone, email):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    def __str__(self):
        return self.name + " is " + str(self.age) + " years old "\
              + "and can be reached at " + self.phone

    @property
    def is_adult(self):
        """Return True if the customer is an adult"""
        return self.age >= 18

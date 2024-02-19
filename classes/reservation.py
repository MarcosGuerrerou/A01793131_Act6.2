"""
A reservation class that holds the reservation
information for a customer at a hotel
"""
from datetime import datetime


class Reservation:
    """
    A reservation class that holds the reservation
    information for a customer at a hotel
    """
    def __init__(self,
                 hotel,
                 customer,
                 room_number: int,
                 start_date: datetime.date,
                 end_date: datetime.date,
                 **kwargs
                 ):
        self.hotel = hotel
        self.customer = customer
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date
        self.active = False

        if kwargs.get('cost'):
            self.cost = kwargs.get('cost')

    def __str__(self) -> str:
        return self.customer.name + f" {'has' if self.active else 'had'} "\
                                    "a reservation at "\
                                    + self.hotel.name + " from "\
                                    + str(self.start_date) + " to "\
                                    + str(self.end_date) + "."

    def create(self):
        """Create the reservation"""
        self.active = True
        return self

    def cancel(self):
        """Cancel the reservation"""
        self.active = False
        return self

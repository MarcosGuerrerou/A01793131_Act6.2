"""
Abstraction of a Hotel
"""
from datetime import datetime
from .reservation import Reservation


class Hotel:
    """Abstraction of a Hotel"""
    def __init__(self, name: str, rooms: int, rate: float, **kwargs):
        self.reservations = []
        self.name = name
        self.rooms = rooms
        self.rate = rate
        if kwargs.get('city'):
            self.city = kwargs.get('city')

    def __str__(self):
        return "Welcome to " + self.name + \
                "! We have " + str(self.rooms) + " rooms available at $"\
                + str(self.rate) + " per night."

    def create_reservation(
            self,
            customer,
            room_number: int,
            start_date: datetime.date,
            end_date: datetime.date):
        """
        Create a reservation for a customer at the hotel.
        Return the reservation.
        """
        num_nights = (end_date - start_date).days
        cost = num_nights * self.rate
        reservation = Reservation(
            hotel=self,
            customer=customer,
            room_number=room_number,
            start_date=start_date,
            end_date=end_date,
            cost=cost
            )
        self.reservations.append(reservation)
        return reservation

    def get_reservations(self, only_active: bool = False):
        """Return all reservations for the hotel."""
        if only_active:
            return [reservation for reservation
                    in self.reservations if reservation.active]
        return self.reservations

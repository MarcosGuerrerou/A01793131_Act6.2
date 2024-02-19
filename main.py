"""
Main file for the project.
This file will be used to run the project.
"""
from datetime import date
from utils import load_json_data
from classes.reservation import Reservation
from classes.customer import Customer
from classes.hotel import Hotel

if __name__ == "__main__":

    # Req 2.1a: Create a hotel.
    hotels: list[Hotel] = [
        Hotel(**hotel) for hotel
        in load_json_data('data/sample_hotels.json')
    ]

    # Req 2.1b: Delete a hotel.
    del hotels[-1]

    # Req 3.1a: Create a customer.
    customers: list[Customer] = [
        Customer(**customer) for customer
        in load_json_data('data/sample_customers.json')
    ]

    # Req 3.1b: Delete a customer.
    del customers[-1]

    # Req 3.1c: Display Customer Information.
    print(customers[0])

    # Req 3.1d: Modify Customer Information.
    customers[0].name = 'Juan Doe'

    # Look for a specific hotel.
    la_hotel: Hotel = [
        hotel for hotel in hotels
        if hotel.city == 'Los Angeles'
        ][0]

    # Req 2.1c: Display Hotel Information.
    print(la_hotel)

    # Req 2.1d: Modify Hotel Information.
    la_hotel.rate = 200

    # Req 2.1e: Reserve a room.
    # Req 4.1a: Create a reservation.
    sample_reservation: Reservation = la_hotel.create_reservation(
        customer=customers[0],
        room_number=101,
        start_date=date(2024, 3, 6),
        end_date=date(2024, 3, 10)
    ).create()

    print(sample_reservation)

    # Print all reservations for the Los Angeles hotel:
    print(la_hotel.get_reservations())

    # Req 2.1f: Cancel a reservation.
    # Req 4.1b: Cancel a reservation.
    sample_reservation.cancel()

    print(sample_reservation)

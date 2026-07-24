"""def book_ticket(movie, seat_number):
    if seat_number < 0:
        raise InvalidSeatNumberError('Seat number must be positive')
    print(f"Ticket booked for {movie}, seat {seat_number}")

book_ticket('Avengers', -2)"""

#This is the broken code.
#Fixed:

class InvalidSeatNumberError(Exception):
    pass

def book_ticket(movie, seat_number):
    if seat_number < 0:
        raise InvalidSeatNumberError('Seat number must be positive')
    print(f"Ticket booked for {movie}, seat {seat_number}")

try:
    book_ticket('Avengers', -2)
except InvalidSeatNumberError as isne:
    print(f"Booking failed :{isne}")
wallet_balance = 1000

def book_movie_ticket():
    try:
        num_tickets = int(input("Enter the number of tickets: "))
        price_per_ticket = wallet_balance/num_tickets
        return price_per_ticket
    except ValueError:
        return "Please enter a number."
    except ZeroDivisionError:
        return "Number of tickets cannot be zero."

print(f"Price per ticket: {book_movie_ticket():.2f}")

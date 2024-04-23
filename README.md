Bus Ticket Booking System

This Python program simulates a bus booking system with functionalities for viewing available seats, booking seats, viewing booked seats, and applying discounts.

Object-Oriented Design:

The program utilizes several classes to represent entities in the system:

    1.Seat: Represents a bus seat with attributes like seat_type, price, place (corner or window), and id.
    2.Bus: Represents a bus with attributes like id and name. It also has a list of Seat objects.
    3.Booked: Represents a booked seat with attributes like bus_id and seat_id.
    4.Discount (optional): Defines discount rates for specific bus IDs and seat IDs (currently implemented for specific scenarios).

Functionalities:

    1.Users can view available seats for all buses, displaying details like bus name, seat ID, seat type, price, and place.
    2.The system allows booking seats by entering the bus ID and seat ID. It checks for seat availability and applies a discount if applicable based on pre-defined rules.
    3.Users can view a list of their booked seats.
    4.The program handles invalid user inputs (e.g., non-integer choices, invalid bus or seat IDs).

Discount Rules:

    1.Discounts are currently defined in the Discount class for specific combinations of bus ID and seat ID. You can modify these rules to implement different discount               strategies.

Getting Started:

    1.Ensure you have Python installed.
    2.Save the code as a Python file (e.g., bus_booking.py).
    3.Run the script from your terminal using python bus_booking.py.

Further Enhancements:

    1.Implement functionalities to cancel bookings.
    2.Add user authentication to manage bookings.
    3.Integrate with a database to store seat information and booking history persistently.
    4.Allow users to search for specific routes or dates (if applicable to your use case).

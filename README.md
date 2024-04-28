Bus Ticket Booking System

This program simulates a bus booking system with functionalities to view available seats, book seats, view booked seats, and calculate the total bill amount.
Features

    1.Seat Management:
       1. Stores details like seat type, price, and location (corner/window).
       2.Supports different bus types (identified by ID) with various seat configurations.
    2.Booking System:
        1.Allows booking seats for a chosen bus after verifying seat availability.
        2.Handles invalid bus IDs and seat IDs.
    3.Discount Management:
        1.Defines discounts for specific seats (can be extended to include other criteria).
        2.Calculates the final bill amount after applying applicable discounts.
    4.User Interface:
        1.Provides a menu-driven interface for users to interact with the system.
        2.Validates user input (e.g., integer input for choices).

Code Structure

The program consists of several classes:

    1.Seat: Represents a seat with attributes like type, price, location, and ID.
    2.Cart: Stores information about seats added to the cart (bus ID, seat ID, price).
    3.Bus: Represents a bus with attributes like ID, name, and a list of Seat objects.
    4.Booked: Represents a booked seat with bus ID and seat ID.
    5.Discount: Stores discount information for specific bus IDs, seat IDs, and discount rate.

Dependencies
 
       1.This program does not require any external libraries beyond the built-in Python functionalities. 
         Running the Program
       2.Save the code as a Python file (e.g., bus_booking.py).
       3.Run the program from the command line using:
       
The program presents a menu with the following options:

    1.View the Seats: Displays details of all available seats across buses.
    2.Book the Seat(s): Allows booking seats for a chosen bus (validates bus ID and seat ID).
    3.View the Booked Seats: Lists the currently booked seats.
    4.Exit: Terminates the program.

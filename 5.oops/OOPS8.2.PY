class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_booked = False


class Guest:
    def __init__(self, name):
        self.name = name


class Booking:
    def book_room(self, room, guest):
        if room.is_booked:
            print(f"Room {room.room_number} is already booked.")
        else:
            room.is_booked = True
            print(f"Room {room.room_number} booked successfully for {guest.name}.")

    def cancel_booking(self, room):
        if not room.is_booked:
            print(f"Room {room.room_number} is not booked.")
        else:
            room.is_booked = False
            print(f"Booking for Room {room.room_number} has been cancelled.")

    def view_available_rooms(self, rooms):
        print("\nAvailable Rooms:")
        available = False

        for room in rooms:
            if not room.is_booked:
                print(f"Room {room.room_number}")
                available = True

        if not available:
            print("No rooms available.")


# Create Rooms
rooms = [
    Room(101),
    Room(102),
    Room(103),
    Room(104),
    Room(105)
]

booking = Booking()

while True:
    print("\n===== HOTEL ROOM BOOKING SYSTEM =====")
    print("1. View Available Rooms")
    print("2. Book a Room")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        booking.view_available_rooms(rooms)

    elif choice == "2":
        room_number = int(input("Enter Room Number: "))
        guest_name = input("Enter Guest Name: ")

        found = False
        for room in rooms:
            if room.room_number == room_number:
                guest = Guest(guest_name)
                booking.book_room(room, guest)
                found = True
                break

        if not found:
            print("Room not found.")

    elif choice == "3":
        room_number = int(input("Enter Room Number to Cancel: "))

        found = False
        for room in rooms:
            if room.room_number == room_number:
                booking.cancel_booking(room)
                found = True
                break

        if not found:
            print("Room not found.")

    elif choice == "4":
        print("Thank you for using the Hotel Booking System.")
        break

    else:
        print("Invalid choice. Please try again.")
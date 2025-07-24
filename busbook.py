from datetime import datetime

class Bus:
    def __init__(self, bno, ac, cap):
        self.bno = bno
        self.ac = ac
        self.cap = cap

    def get_bno(self):
        return self.bno

    def get_ac(self):
        return self.ac

    def get_cap(self):
        return self.cap

    def display(self):
        print("1. BUS NO     :", self.get_bno())
        print("2. AC         :", self.get_ac())
        print("3. CAPACITY   :", self.get_cap())

BUSES = [Bus(1, "YES", 2), Bus(2, "NO", 1), Bus(3, "YES", 3)]
BOOKINGS = []

class Booking:
    def __init__(self):
        self.name = input("Enter passenger name: ")
        self.bno = int(input("Enter bus no: "))
        d = input("Enter date (dd-mm-yyyy): ")
        try:
            self.date = datetime.strptime(d, "%d-%m-%Y").date()
        except ValueError:
            print("Invalid date format!")
            self.date = None

    def make_booking(self, BUSES, BOOKINGS):
        if self.is_available(BUSES, BOOKINGS, self.bno, self.date):
            BOOKINGS.append(self)
            print("Booking Successful!")
        else:
            print("BUS IS FULL")

    def is_available(self, BUSES, BOOKINGS, bno, date):
        booked = 0
        capacity = 0
        for i in BUSES:
            if i.bno == bno:
                capacity = i.cap
        for i in BOOKINGS:
            if i.bno == bno and i.date == date:
                booked += 1
        return booked < capacity

    def display_book_info(self):
        print("Passenger Name:", self.name)
        print("Bus No:", self.bno)
        print("Date:", self.date)
        print("----------")

print("Available buses are:")
for i in BUSES:
    i.display()
    print("----------")

while True:
    print("PRESS 1 TO BOOK TICKETS")
    print("PRESS 2 TO VIEW BOOKING")
    print("PRESS 3 TO EXIT")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        b = Booking()
        b.make_booking(BUSES, BOOKINGS)
    elif ch == 2:
        if not BOOKINGS:
            print("No Booking so far")
        else:
            for i in BOOKINGS:
                i.display_book_info()
    elif ch == 3:
        print("Exiting the system. Thank You!")
        break
    else:
        print("Invalid choice")
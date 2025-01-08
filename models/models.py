import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database/hotel.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        with open('database/schema.sql', 'r') as f:
            self.cursor.executescript(f.read())
        self.connection.commit()

    def get_all_rooms(self):
        return self.cursor.execute("SELECT * FROM rooms").fetchall()

    def get_available_rooms(self):
        return self.cursor.execute("SELECT * FROM rooms WHERE availability = 1").fetchall()

    def book_room(self, customer_name, room_id, days):
        room = self.cursor.execute("SELECT availability FROM rooms WHERE id = ?", (room_id,)).fetchone()
        if room and room[0] == 1:
            self.cursor.execute(
                "INSERT INTO bookings (customer_name, room_id, days) VALUES (?, ?, ?)",
                (customer_name, room_id, days)
            )
            self.cursor.execute("UPDATE rooms SET availability = 0 WHERE id = ?", (room_id,))
            self.connection.commit()
            return True
        return False

    def get_all_bookings(self):
        return self.cursor.execute("""
            SELECT bookings.id, customer_name, room_id, days, price_per_day * days as total
            FROM bookings
            JOIN rooms ON bookings.room_id = rooms.id
        """).fetchall()

    def get_invoice(self, booking_id):
        return self.cursor.execute("""
            SELECT bookings.id, customer_name, room_id, days, price_per_day * days as total
            FROM bookings
            JOIN rooms ON bookings.room_id = rooms.id
            WHERE bookings.id = ?
        """, (booking_id,)).fetchone()

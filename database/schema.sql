CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY ,
    room_number TEXT NOT NULL,
    price_per_day REAL NOT NULL,
    availability INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY ,
    customer_name TEXT NOT NULL,
    room_id INTEGER NOT NULL,
    days INTEGER NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms (id)
);

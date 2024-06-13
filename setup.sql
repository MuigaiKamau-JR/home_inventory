-- Create Room table
CREATE TABLE Room (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Create Item table
CREATE TABLE Item (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    purchase_date DATE NOT NULL,
    price REAL NOT NULL,
    warranty_expiry_date DATE,
    quantity INTEGER NOT NULL,
    room_id INTEGER,
    FOREIGN KEY (room_id) REFERENCES Room(id)
);

-- Insert example rooms
INSERT INTO Room (name) VALUES ('Living Room'), ('Kitchen'), ('Bedroom');

-- Insert example items
INSERT INTO Item (name, purchase_date, price, warranty_expiry_date, quantity, room_id)
VALUES ('Sofa', '2023-01-15', 500.00, '2028-01-15', 1, 1),
       ('Refrigerator', '2023-02-20', 1200.00, '2030-02-20', 1, 2),
       ('Bed', '2022-12-10', 800.00, '2027-12-10', 1, 3);

import sqlite3

# Function to connect to the SQLite database
def connect_db(db_file):
    conn = sqlite3.connect(db_file)
    return conn

# Function to fetch all rows from a table
def get_all_rows(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    return rows

# Example usage
if __name__ == "__main__":
    db_file = "db/mydatabase.db"
    conn = connect_db(db_file)
    rows = get_all_rows(conn, "Room")  # Replace "Room" with your table name
    for row in rows:
        print(row)
    conn.close()

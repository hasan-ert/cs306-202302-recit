import mysql.connector
from connect import create_connection
from mysql.connector import Error


# Function to execute a query
def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


# Create table Operation
def create_table(connection, table_name, fields):
    query = f"CREATE TABLE {table_name} ("

    for column_name, column_type in fields.items():
        query += f" {column_name} {column_type},"
    query = query[:-1] + ");"
    print(query)
    execute_query(connection=connection, query=query)


# Insert Operation
def insert_sailor(connection, data):
    query = "INSERT INTO sailors (sid,name, age, rating) VALUES (%s,%s, %s, %s)"
    execute_query(connection, query, data)


# Read Operation


def read_sailors(connection):
    query = "SELECT * FROM sailors"
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print(record)
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


# Update Operation
def update_sailor_rating(connection, sailor_id, new_rating):
    query = "UPDATE sailors SET rating = %s WHERE sid = %s"
    data = (new_rating, sailor_id)
    execute_query(connection, query, data)


# Delete Operation
def delete_sailor(connection, sailor_id):
    query = "DELETE FROM sailors WHERE sid = %s"
    data = (sailor_id,)
    execute_query(connection, query, data)


# Main function
def main():
    connection = create_connection()
    cursor = connection.cursor()

    # First insert these values to your table
    values_to_insert = [
        (1, "Bob", 25, 8.2),
        (2, "Dylan", 23, 3),
        (3, "Arnold", 20, 5),
        (4, "Casey", 22, 6.3),
        (5, "John", 20, 6.6),
        (6, "Billy", 21, 10),
        (7, "Mary", 21, 4),
    ]
    fields = {
        "sid": "INT PRIMARY KEY",
        "name": "VARCHAR(50)",
        "age": "INT",
        "rating": "DECIMAL",
    }

    # Create your sailors table
    # create_table(connection, "sailors", fields)

    # Uncomment and complete the following lines as per the assignment requirements
    for sailor in values_to_insert:
        insert_sailor(connection, sailor)
    read_sailors(connection)
    update_sailor_rating(connection, 1, "B")
    delete_sailor(connection, 2)

    if connection:
        connection.close()
        print("Connection closed")


if __name__ == "__main__":
    main()

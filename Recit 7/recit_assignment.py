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
    # Write a function to create a table with given table name and fields dictionary
    pass


# Insert Operation
def insert_student(connection, data):
    # Write a function to insert given data into students table
    pass


# Read Operation
def read_students(connection):
    # Write a function to retrieve all students
    pass


# Update Operation
def update_student_grade(connection, student_id, new_grade):
    # Write a function to update a student grade with given id and new grade
    pass


# Delete Operation
def delete_student(connection, student_id):
    # Write a function to delete a student with given id
    pass


# Main function
def main():
    connection = create_connection()

    fields = {"sid": "INT", "name": "VARCHAR(50)", "age": "INT", "grade": "VARCHAR(5)"}

    # First, create your students table
    # create_table(connection, "students", fields)

    # Then insert these values to your table
    values_to_insert = [
        (1, "Hasan", 25, "A"),
        (2, "Alper", 23, "A-"),
        (3, "Ekin", 20, "B+"),
        (4, "Mine", 22, "B"),
        (5, "Ceyda", 20, "A"),
        (6, "Mert", 21, "C"),
        (7, "Serra", 21, "B+"),
    ]

    # Uncomment and complete the following lines as per the assignment requirements
    # insert_student(connection, ('John Doe', 20, 'A'))
    # read_students(connection)
    # update_student_grade(connection, 1, 'B')
    # delete_student(connection, 2)

    if connection:
        connection.close()
        print("Connection closed")


if __name__ == "__main__":
    main()

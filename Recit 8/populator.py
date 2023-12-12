import mysql.connector
from faker import Faker
import random
from connect import create_connection

# Connect to your MySQL server
connection = create_connection()

# Create a cursor object
cursor = connection.cursor()

# Create a Faker instance
fake = Faker()

# Number of records to generate
num_records = 1000000

# Create a table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(50),
        age INT,
        INDEX idx_last_name (last_name)
    )
"""
)

# Generate and insert data
for _ in range(num_records):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    age = random.randint(18, 99)

    cursor.execute(
        """
        INSERT INTO users (first_name, last_name, email, age)
        VALUES (%s, %s, %s, %s)
    """,
        (first_name, last_name, email, age),
    )

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

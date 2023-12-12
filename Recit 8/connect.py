import mysql.connector
from mysql.connector import errorcode


# pip install mysql-connector-python
def create_connection():
    try:
        cnx = mysql.connector.connect(user="root", password="2539", database="recit8")
        print("Connection established with the database")
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
    else:
        cnx.close()
        return None

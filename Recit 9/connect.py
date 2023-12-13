from pymongo import MongoClient


# First of all, install the pymongo using pip
# python -m pip install "pymongo[srv]"
def connectDB():
    # Replace the connection string with your MongoDB connection string
    # You can obtain the connection string from your MongoDB Atlas dashboard or configure it locally
    # For example, if your database is running on localhost, the connection string might look like this:
    # "mongodb://localhost:27017/"

    connection_string = "mongodb+srv://hasan_test:test1234@cluster0.dr2hcsc.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(connection_string)

    # Access a specific database (replace "your_database_name" with your actual database name)
    db = client.cluster0
    print("Connection established to your db")
    return db
    # Close the connection when you're done
    # client.close()

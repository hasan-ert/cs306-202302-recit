from connect import connectDB
from dummy_data import dummy_data
from pymongo import errors


def createCollection(db, collection_name):
    try:
        # If the collection doesn't exist, create it
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Collection '{collection_name}' created.")
        elif collection_name in db.list_collection_names():
            print("Collection already exists")
    except Exception as e:
        print("An error occured: ", e)


def insert_into_collection(db, collection_name, data):
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Insert the data into the collection
        result = collection.insert_one(data)

        # Print the inserted document ID
        print("Insertion successfully completed")
        print(f"Inserted document ID: {result.inserted_id}")

    except Exception as e:
        print(f"An error occurred: {e}")


def read_all_data(db, collection_name):
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Use the find method to retrieve all documents
        result = collection.find()

        # Iterate through the documents and print them
        for document in result:
            print(document)

    except Exception as e:
        print(f"An error occurred: {e}")


def find_orders_containing_item(db, collection_name, item_name):
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Define the query to find orders containing the specified item
        query = {"order_items.item_name": item_name}

        # Use the find method to retrieve matching documents
        cursor = collection.find(query)

        # Convert your cursor to a list to freely operate over it
        result = list(cursor)

        # Print the matching documents
        for document in result:
            print(document)

        # Return the whole result list
        return result

    except Exception as e:
        print(f"An error occurred: {e}")


def delete_record_by_id(db, collection_name, record_id):
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Define the query to find the document by its ID
        query = {"_id": record_id}

        # Use the delete_one method to delete the document
        result = collection.delete_one(query)

        # Check if the deletion was successful
        if result.deleted_count == 1:
            print(f"Successfully deleted record with ID {record_id}")
        else:
            print(f"No record found with ID {record_id}")

    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")


def update_order_list_by_id(db, collection_name, record_id, new_order_list):
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Define the query to find the document by its ID
        query = {"_id": record_id}

        # Use the update_one method to update the specific field (order_list)
        result = collection.update_one(query, {"$set": {"order_items": new_order_list}})

        # Check if the update was successful
        if result.matched_count == 1:
            print(f"Successfully updated order_list for record with ID {record_id}")
        else:
            print(f"No record found with ID {record_id}")

    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")


def delete_record_by_item(db, collection_name, item="Pizza"):
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Define the query to find the document by its ID
        query = {"order_items.item_name": item}

        # Use the delete_one method to delete the document
        result = collection.delete_many(query)

        # Check if the deletion was successful
        if result.deleted_count >= 1:
            print(
                f"Successfully deleted {result.deleted_count} record that contains {item}"
            )
        else:
            print(f"No record found with {item}")

    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # First create a connection
    db = connectDB()

    # Then create a collection
    # createCollection(db, "orders")

    # # Insert some dummy data into your collection
    # for item in dummy_data:
    #     insert_into_collection(db, "orders", item)

    read_all_data(db, "orders")
    # Try to find documents which contains a Pizza as an order item
    # found_documents = find_orders_containing_item(
    #     db, collection_name="orders", item_name="Pizza"
    # )

    # # Delete the first record which has a pizza in its order list
    # id_to_delete = found_documents[0]["_id"]
    # found_documents.pop(0)
    # delete_record_by_id(db, "orders", id_to_delete)

    # # Update the next item
    # id_to_update = found_documents[0]["_id"]
    # new_order_list = (
    #     [
    #         {"item_name": "Hamburger", "quantity": 1},
    #         {"item_name": "Fries", "quantity": 1},
    #         {"item_name": "Iced Tea", "quantity": 2},
    #     ],
    # )
    # update_order_list_by_id(db, "orders", id_to_update, new_order_list)

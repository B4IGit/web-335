"""
Title: ledesma_usersp2.py
Author: Devin Ledesma
Date: 14 July 2025
Description: Hands_On_5.2: Python with MongoDB, Part II
"""

# Import the MongoClient
from pymongo import MongoClient
from pymongo.errors import OperationFailure
import datetime

# Build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.dlgzebu.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity")

print(client)

# Configure a variable to access the web335DB
db = client['web335DB']

# Callback to define transaction steps
def crud_operations(session):
    # Create a new user document and add it to the users collection
    toast = {
        "firstName": "French",
        "lastName": "Toast",
        "employeeId": "1014",
        "email": "ftoast@me.com",
        "dateCreated": datetime.datetime.utcnow()
    }

    # Insert the document into the users collection
    toast_user_id = db.users.insert_one(toast, session=session).inserted_id
    print("Inserted ID:", toast_user_id)

    # Prove the insert worked by searching the collection for the document
    print("After insert:", db.users.find_one({"employeeId": "1014"}, session=session))

    # Create an update query to change the user's email address
    db.users.update_one(
        {"employeeId": "1014"},
        {"$set": {"email": "french.toast@me.com"}},
        session=session
    )

    # Prove the update worked by searching the collection for the user by employeeId
    print("After update:", db.users.find_one({"employeeId": "1014"}, session=session))

    # Build a query to remove a user document
    result = db.users.delete_one({"employeeId": "1014"}, session=session)
    print("Delete result:", result)

    # Prove the delete worked by searching the collection for the deleted document
    print("After delete:", db.users.find_one({"employeeId": "1014"}, session=session))

# Run transaction using with_transaction
with client.start_session() as session:
    try:
        session.with_transaction(crud_operations)
    except OperationFailure as e:
        print("Transaction failed:", e)

client.close()
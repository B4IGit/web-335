"""
Title: ledesma_usersp1.py
Author: Devin Ledesma
Date: 08 July 2025
Description: Hands_On_4.2
"""

# Import the MongoClient
from pymongo import MongoClient
import datetime

# Build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.dlgzebu.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity")

print(client)

# Configure a variable to access the web335DB
db = client['web335DB']

# Call the find function to display all of the users in the collection; use projections to only show the first and last names.
for user in db.users.find({},{'firstName': 1, 'lastName': 1}):
    print(user)

#
print(" ") # Line break
#

# Call the find_one function to display an employee by id
print(db.users.find_one({'employeeId': '1011'}))

#
print(" ") # Line break
#

# Call the find_one function to display the last name Mozart
print(db.users.find_one({'lastName': 'Mozart'}))
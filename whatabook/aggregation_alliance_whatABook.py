"""
Title: aggregation_alliance_whatABook.py
Author: Devin Ledesma, Riley Bird
Date: 07/22/2025
Description: This is a simple application for whatABook. It allows customers to add books, search for books by author, genre, and title, creates wishlistitems by adding and removing books. Allows customers to view personal wishlists.
"""

"""
Resources Used:
    https://stackoverflow.com/questions/37565793/how-to-let-the-user-select-an-input-from-a-finite-list

"""

# Import MongoClient
from pymongo import MongoClient

# Import Inquirer
import inquirer

# Build a connection string
print('Test Connection')
client = MongoClient('mongodb+srv://web335_user:s3cret@bellevueuniversity.dlgzebu.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity')
db = client['whatabook']
print(client)

# Add line break
print()

# Testing if connection is successful
print('Testing to find Customers')
for customer in db.customers.find({},{'firstName': 1, 'lastName': 1}):
    print(customer)

# Add line break
print()

# Display books from 'books' collection
print('List of Books')
for book in db.books.find():
    print('Title:', book.get('title'))
    print('Author:', book.get('author'))
    print('Genre:', book.get('genre'))
    print('Book ID:', book.get('bookId'))
    print() # line break
    print('--------------------------') # line separation

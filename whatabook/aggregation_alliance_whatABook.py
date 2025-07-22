"""
Title: aggregation_alliance_whatABook.py
Author: Devin Ledesma, Riley Bird
Date: 07/22/2025
Description: This is a simple application for whatABook. It allows customers to add books, search for books by author, genre, and title, creates wishlistitems by adding and removing books. Allows customers to view personal wishlists.
"""

"""
Resources Used:
    https://stackoverflow.com/questions/37565793/how-to-let-the-user-select-an-input-from-a-finite-list
    https://python-inquirer.readthedocs.io/en/latest/usage.html#question-types
    https://www.w3schools.com/python/ref_string_upper.asp
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

# Formats books
def format_books(book):
    print() # line break
    print('Title:', book.get('title'))
    print('Author:', book.get('author'))
    print('Genre:', book.get('genre'))
    print('Book ID:', book.get('bookId'))
    print() # line break
    print('--------------------------') # line separation

# Display books from 'books' collection
print('List all Books')
for book in db.books.find():
    format_books(book)

# List books by genre (supplies users with choices)
    # installed inquirer using pip (stack overflow)
list_genres = [
    inquirer.List('genre_options',
        message = 'Please choose from the following genres.',
        choices = [
            'Horror', 'Science-Fiction', 'Psychological Thriller', 'Humor', 'Non-Fiction'
        ]
    ),
]
answers = inquirer.prompt(list_genres)
selected_genre = answers['genre_options']

# Filters the list of books based on the selected genre
print('List of Books by Genre')
for book in db.books.find({'genre': selected_genre}):
    format_books(book)

# Display a customer's wishlist by customerId
    # Add error handing for invalid customerId
find_customer_by_id = [
    inquirer.Text('customer_id',
        message = 'Please enter your customer ID.'
    ),
]
while True:
    answer = inquirer.prompt(find_customer_by_id)
    customerId = answer['customer_id']

    # Validates customerId
    customer = db.customers.find_one({'customerId': customerId})

    if customer:
        print(f'Welcome, {customer['firstName']} {customer['lastName']}!'.upper())

        print('Your Wishlist:')
        # Accesses items in wishlist
        wishlist = db.wishlistitems.find({'customerId': customerId})

        if wishlist:
            for item in wishlist:
                # Accesses books in customers wishlist
                book = db.books.find({'bookId': item['bookId']})
                #
                #
                # NEED TO FIGURE OUT HOW TO IMPORT BOOKS
                if book:
                    format_books(book)
                #
                #
                #
        else:
            print('No wishlist found.')
        break # exits loop once a valid ID is entered
    else:
        print('Invalid customer ID. Please try again.')

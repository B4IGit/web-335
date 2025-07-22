/*
Title: aggregation_alliance_whatABook.js
Author: Devin Ledesma, Riley Bird
Date: 07/18/2025
Description: Queries to showcase the functionality of whatABook's application.
*/

// Load script.js
load('script.js')

//Query to display a list of books
db.books.find();

//Query to display a list of books by genre
db.books.aggregate([
  { $group: { _id: "$genre", books: { $push: "$title" } } }
]);

//Query to display a list of books by author
db.books.aggregate([
  { $group: { _id: "$author", books: { $push: "$title" } } }
]);

//Query to display a book by bookId
db.books.findOne({ bookId: "b101" });

// Query to display wishlist by customerId

// Query to add book(s) to customer's wishlist

// Remove book(s) from a customer's wishlist


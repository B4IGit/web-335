//Query to display a list of books
db.books.find()

//Query to display a list of books by genre
db.books.aggregate([
  { $group: { _id: "$genre", books: { $push: "$title" } } }
])

//Query to display a list of books by author
db.books.aggregate([
  { $group: { _id: "$author", books: { $push: "$title" } } }
])

//Query to display a book by bookId
db.books.findOne({ bookId: "b101" })


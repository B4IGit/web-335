/*
Title: script.js
Author: Devin Ledesma, Riley Bird
Date: 07/17/2025
Description: MongoDB shell scripts for WhatABook.
*/

// Drop collections and database
db.books.drop()
db.customers.drop()
db.wishlistitems.drop()

// Create books collection
db.createCollection('books', {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["bookId", "title", "author", "genre"],
            properties: {
                bookId: { bsonType: "string" },
                title: { bsonType: "string" },
                author: { bsonType: "string" },
                genre: { bsonType: "string" }

            }
        }
    }
});

// Create customers collection
db.createCollection('customers', {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["customerId", "firstName", "lastName"],
            properties: {
                customerId: { bsonType: "string" },
                firstName: { bsonType: "string" },
                lastName: { bsonType: "string" }
            }
        }
    }
});

db.createCollection('wishlistitems', {
    validator: {
        $jsonSchema:{
            bsonType: "object",
            required: ["customerId", "bookId"],
            properties: {
                customerId: { bsonType: "string" },
                bookId: { bsonType: "array" }
            }
        }
    }
});

// Books
mexicanGothic = {
    bookId: "b101",
    title: "Mexican Gothic",
    author: "Silvia Moreno-Garcia",
    genre: "Horror"
};

hailMary = {
    bookId: "b102",
    title: "Project Hail Mary",
    author: "Andy Weir",
    genre: "Science-Fiction"
};

secertHistory = {
    bookId: "b103",
    title: "The Secret History",
    author: "Donna Tartt",
    genre: "Psychological Thriller"
};

calledOve = {
    bookId: "b104",
    title: "A Man Called Ove",
    author: "Fredrick Backman",
    genre: "Humor"
};

sweetgrass = {
    bookId: "b105",
    title: "Braiding Sweetgrass",
    author: "Robin Wall Kimmerer",
    genre: "Non-Fiction"
};

// Insert book documents
db.books.insertOne(mexicanGothic)
db.books.insertOne(hailMary)
db.books.insertOne(secertHistory)
db.books.insertOne(calledOve)
db.books.insertOne(sweetgrass)


// Customers
wenlock = {
    customerId: "c1007",
    firstName: "Brad",
    lastName: "Wenlock"
};

gold = {
    customerId: "c1008",
    firstName: "Sarah",
    lastName: "Gold"
};

kitten = {
    customerId: "c1009",
    firstName: "Ryan",
    lastName: "Kitten"
};

// Insert customer documents
db.customers.insertOne(wenlock)
db.customers.insertOne(gold)
db.customers.insertOne(kitten)

// Customer wishlists
wenlockWishlist = {
    customerId: "c1007",
    bookId: ["b101", "b103", "b104"]
};

goldWishlist = {
    customerId: "c1008",
    bookId: ["b102", "b105"]
}

// Insert wishlist documents
db.wishlistitems.insertOne(wenlockWishlist)
db.wishlistitems.insertOne(goldWishlist)
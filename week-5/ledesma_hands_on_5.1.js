/*
Author:         Devin Ledesma
Date:           06/26/2025
File Name:      ledesma_hands_on_5.1.js
Description:    This file demonstrates that I can perform various operations on the user's collection from assignment 4.2
*/

// Adds a new user to the users collection
db.users.insertOne(
    {
        "firstName": "Devin",
        "lastName": "Ledesma",
        "employeeId": "1013",
        "email": "ledesma011@msn.com",
        "dateCreated": new Date()
    })

// Updates a users email in the users collection
db.users.updateOne({"firstName": "Wolfgang"}, {$set:{email: "mozart@me.com"}})

// Displays all users in the users collection, using projections to only show firstName, lastName, and email
db.users.find({}, {firstName: 1, lastName: 1, email: 1, _id: 0})
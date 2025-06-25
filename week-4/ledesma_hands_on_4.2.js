/*
Author:         Devin Ledesma
Date:           06/24/2025
File Name:      ledesma_hands_on_4.2.js
Description:    This file demonstrates that I create a MongoDB account, connected database, and was able to look up data in the users.js file.
*/


// Displays all users in the collection
db.users.find();

// Display the user with the email address jbach@me.com
db.users.findOne({email: 'jbach@me.com'});

// Display the user with the last name Mozart
db.users.findOne({lastName: 'Mozart'})

// Display the user with the first name Richard
db.users.find({firstName: 'Richard'});

// Display the user with employeeId 1010
db.users.findOne({employeeId: '1010'});
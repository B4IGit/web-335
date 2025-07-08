/*
Author:         Devin Ledesma
Date:           07/07/2025
File Name:      ledesma_hands_on_6.1.js
Description:    This file demonstrates that I can perform various operations such as aggregation with the houses.js file
*/

// Load
load("houses.js")

// A
db.students.find()

// B
db.students.insertOne({
 firstName: 'Devin',
 lastName: 'Ledesma',
 studentId: 's1019',
 houseId: 'h1010'
 })

// C
db.students.updateOne(
 {firstName: "Devin"},
 {$set: {firstName: "Burnt", lastName: "Toast"}}
 )

// D
db.students.deleteOne({lastName: "Toast"})

// E
db.houses.aggregate([
       {
             $lookup: {
       from: "students",
       localField: "houseId",
       foreignField: "houseId",
       as: "students"
     }
   },
   {
     $unwind: "$students"
   },
   {
     $sort: {
           houseId: 1,
           "students.lastName": 1,
           "students.firstName": 1.     }
   },
   {
     $group: {
           _id: "$houseId",
           house: { $first: "$$ROOT" },
           students: { $push: "$students" }
         }
   },
   {
     $replaceRoot: {
           newRoot: {
                 houseId: "$_id",
                 mascot: "$house.mascot",
                 founder: "$house.founder",
                 students: "$students"
               }
         }
   },
   {
     $sort: { houseId: 1 }
   }
 ])

// F
db.houses.aggregate([
    {
        $match: { houseId: "h1007" }
    },
    {
        $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "students"
        }
    },
    {
        $unwind: "$students"
    },
    {
        $sort: {
            "students.lastName": 1,
            "students.firstName": 1
        }
    },
    {
        $addFields: {
            "students.houseId": null
        }
    },
    {
        $group: {
            _id: "$houseId",
            house: { $first: "$$ROOT" },
            students: { $push: "$students" }
        }
    },
    {
        $replaceRoot: {
            newRoot: {
                houseName: "Gryffindor",
                houseId: "$_id",
                mascot: "$house.mascot",
                founder: "$house.founder",
                students: "$students"
            }
        }
    }
])

// G
db.houses.aggregate([
    {
        $match: { mascot: "Eagle" }
    },
    {
        $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "students"
        }
    },
    {
        $unwind: "$students"
    },
    {
        $sort: {
            "students.lastName": 1,
            "students.firstName": 1
        }
    },
    {
        $addFields: {
            "students.houseId": null
        }
    },
    {
        $group: {
            _id: "$houseId",
            house: { $first: "$$ROOT" },
            students: { $push: "$students" }
        }
    },
    {
        $replaceRoot: {
            newRoot: {
                mascot: "$house.mascot",
                houseName: "Ravenclaw",
                houseId: "$_id",
                founder: "$house.founder",
                students: "$students"
            }
        }
    }
])
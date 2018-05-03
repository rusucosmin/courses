- [x] 1. Execute all commands listed above.
- [x] 2. Insert the following documents in a collection called ‘students’ that belongs to the ‘test’
database:
```
db.students.insert({
  "firstname" : "Bob",
  "lastname" : "Tabor",
  "city" : "New York",
  "admission" : {"grade" :10, "year" : 2015},
  "domain" : "Computer Science",
  "yearofstudy" : 3,
  "hobbies" : ["reading","camping"]
  })

db.students.insert({
  "firstname" : "Bob",
  "lastname" : "Black",
  "city" : "London",
  "admission" : {"grade":9.4, "year": 2016},
  "domain" : "Computer Science",
  "yearofstudy" : 2,
  "hobbies" : ["hiking","swimming","camping"]
  })

db.students.insert({
  "firstname" : "Anna",
  "lastname" : "Grey",
  "city" : "Padstow",
  "admission" : {"grade":6.4, "year": 2017},
  "domain" : "Computer Science",
  "yearofstudy" : 1,
  "hobbies" : ["surfing","cooking","photography"]
  })

db.students.insert({
  "firstname" : "Jane",
  "lastname" : "Reed",
  "city" : "Edingburg",
  "admission" : {"grade":8.9, "year": 2016},
  "domain" : "Biology",
  "yearofstudy" : 2, "hobbies" : ["travel","camping","photography"]
  })

db.students.insert({
  "firstname" : "James",
  "lastname" : "Horner",
  "admission" : {"grade":8.9, "year": 2015},
  "domain" : "Biology",
  "yearofstudy" : 3,
  "hobbies" : ["travel","martial arts"]
  })
```
- [x] 3. Return all documents for which grade is greater than or equal to 6.4 and less than 10 and
domain is equal to “Computer Science”. The documents must be sorted by firstname in
ascending order.

```
> db.students.find({"admission.grade":{"$gte":6.4,"$lt":10},"domain":"Computer Science"}).sort({"firstname":1}).pretty()
{
  "_id" : ObjectId("5aea9f23a6f877af09074d0b"),
  "firstname" : "Anna",
  "lastname" : "Grey",
  "city" : "Padstow",
  "admission" : {
    "grade" : 6.4,
    "year" : 2017
  },
  "domain" : "Computer Science",
  "yearofstudy" : 1,
  "hobbies" : [
    "surfing",
    "cooking",
    "photography"
  ]
}
{
  "_id" : ObjectId("5aea9edea6f877af09074d0a"),
  "firstname" : "Bob",
  "lastname" : "Black",
  "city" : "London",
  "admission" : {
    "grade" : 9.4,
    "year" : 2016
  },
  "domain" : "Computer Science",
  "yearofstudy" : 2,
  "hobbies" : [
    "hiking",
    "swimming",
    "camping"
  ]
}
```

- [x] 4. Return only the ‘firstname’, ‘lastname’,’domain’ and ‘admission’ fields of the document that has
the highest grade.

```
db.students.find({}, {"firstname":1, "lastname":1, "_id":0, "admission":1, "domain":1}).sort({"admission.grade":-1}).limit(1).pretty()
{
  "firstname" : "Bob",
  "lastname" : "Tabor",
  "admission" : {
    "grade" : 10,
    "year" : 2015
  },
  "domain" : "Computer Science"
}
```

- [x] Set the ‘city’ field value to “London” for all documents that have the domain equal to “Biology”.

```
db.students.update({"domain": "Biology"}, {"$set": {"city": "London"}}, {"multi": true})
WriteResult({ "nMatched" : 2, "nUpserted" : 0, "nModified" : 2 })

db.students.find({"domain": "Biology"}).pretty()
{
  "_id" : ObjectId("5aea9f84a6f877af09074d0c"),
  "firstname" : "Jane",
  "lastname" : "Reed",
  "city" : "London",
  "admission" : {
    "grade" : 8.9,
    "year" : 2016
  },
  "domain" : "Biology",
  "yearofstudy" : 2,
  "hobbies" : [
    "travel",
    "camping",
    "photography"
  ]
}
{
  "_id" : ObjectId("5aea9fb6a6f877af09074d0d"),
  "firstname" : "James",
  "lastname" : "Horner",
  "admission" : {
    "grade" : 8.9,
    "year" : 2015
  },
  "domain" : "Biology",
  "yearofstudy" : 3,
  "hobbies" : [
    "travel",
    "martial arts"
  ],
  "city" : "London"
}
```

- [x] Delete all documents that have the admission year equal to 2015.

```
db.students.remove({"admission.year": 2015})
WriteResult({ "nRemoved" : 2 })

db.students.find({}).pretty()
{
  "_id" : ObjectId("5aea9edea6f877af09074d0a"),
  "firstname" : "Bob",
  "lastname" : "Black",
  "city" : "London",
  "admission" : {
    "grade" : 9.4,
    "year" : 2016
  },
  "domain" : "Computer Science",
  "yearofstudy" : 2,
  "hobbies" : [
    "hiking",
    "swimming",
    "camping"
  ]
}
{
  "_id" : ObjectId("5aea9f23a6f877af09074d0b"),
  "firstname" : "Anna",
  "lastname" : "Grey",
  "city" : "Padstow",
  "admission" : {
    "grade" : 6.4,
    "year" : 2017
  },
  "domain" : "Computer Science",
  "yearofstudy" : 1,
  "hobbies" : [
    "surfing",
    "cooking",
    "photography"
  ]
}
{
  "_id" : ObjectId("5aea9f84a6f877af09074d0c"),
  "firstname" : "Jane",
  "lastname" : "Reed",
  "city" : "London",
  "admission" : {
    "grade" : 8.9,
    "year" : 2016
  },
  "domain" : "Biology",
  "yearofstudy" : 2,
  "hobbies" : [
    "travel",
    "camping",
    "photography"
  ]
}
```

/*Q1&Q2 Create the above database and collection.Insert the above document into the collection.*/
use simpleClinic

db.patients.insertOne({
    firstName:'Ben',
    lastName:'Choi',
    age:18,
    history:[
        {disease:'cold',treatment:'pain killer'},
        {checkup:'annual',output:'OK'},
        {disease:'sore throat',treatment:'antibodies'}
        ]
})

/*Q3 3.	Insert 3 additional patient records (documents) with at least 1 history entry per patient.*/
db.patients.insertMany([{
    firstName:'Romelu',
    lastName:'Lukaku',
    age:28,
    history:[
        {disease:'flu',treatment:'aspirin'},
        {checkup:'annual',output:'OK'},
        ]
},{
    firstName:'Kai',
    lastName:'Havertz',
    age:22,
    history:[
        {disease:'stomachache',treatment:'relax and sleep'},
        {checkup:'daily',output:'OK'},
        ]
},{
    firstName:'N\'golo',
    lastName:'Kante',
    age:30,
    history:[
        {disease:'muscle strain',treatment:'ice compress'},
        {checkup:'monthly',output:'OK'},
        ]
}])

/*Q4 Test out your database with find().*/
db.patients.find()

/*Q5 Find all patients who are older than 30 years old (or a value of your choice-29).*/
db.patients.find({'age':{$gt:29}})

/*Q6 Delete all patients who got a flu as a disease.*/
db.patients.deleteMany({"history.disease":'flu'})
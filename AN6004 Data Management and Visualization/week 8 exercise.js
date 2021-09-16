use Restaurants

/* Q1 Write a MongoDB query to display all the documents in the collection restaurants. */
db.Restaurants.find()

/* Q2 Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant. */
db.Restaurants.aggregate([
    {$project: {restaurant_id:1, name:1, borough:1, cuisine:1}}
    ])
    
/* Q3 Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine, but exclude the field _id for all the documents in the collection restaurant. */
db.Restaurants.aggregate([
    {$project: {_id:0, restaurant_id:1, name:1, borough:1, cuisine:1}}
    ])

/* Q4 Write a MongoDB query to display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all. */
db.Restaurants.aggregate([
    {$project: {_id:0, restaurant_id:1, name:1, borough:1, 'address.zipcode':1}}
    ])
    
/* Q5 Write a MongoDB query to display all the restaurant which is in the borough Bronx. the documents in the collection restaurant. */
db.Restaurants.aggregate([
    {$match:{'borough':'Bronx'}}
    ])
    
/* Q6 Write a MongoDB query to display the first 5 restaurant which is in the borough Bronx. */
db.Restaurants.aggregate([
    {$match:{'borough':'Bronx'}}
    ]).limit(5)
    
/* Q7 Write a MongoDB query to display the next 5 restaurants after skipping first 5 which are in the borough Bronx. */
db.Restaurants.aggregate([
    {$match:{'borough':'Bronx'}}
    ]).skip(5).limit(5)
    
/* Q8 Write a MongoDB query to find the restaurants who achieved a score more than 90. */
db.Restaurants.aggregate([
    {$match: {'grades':{$elemMatch:{'score':{$gt:90}}}}},
    ])
    
/* Q9 Write a MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100. */
db.Restaurants.aggregate([
    {$match: {'grades':{$elemMatch:{'score':{$gt:80, $lt:100}}}}},
    ])

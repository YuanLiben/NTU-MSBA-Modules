use "boxoffice"

/* Q1 Display the first document. */
db.moviestarts.findOne()

/* Q2 Search all movies that have a rating higher than 9.2 and a runtime lower than 100 minutes.*/
db.moviestarts.find({'meta.rating':{$gt: 9.2},'meta.runtime':{$lt: 100}})

/* Q3 Search all movies that have a genre of “drama” or “action”. */
db.moviestarts.find({'genre':{$in:['drama','action']}})

/* Q4 Search all movies that have a genre of “drama” and “action”. You must not use $and.*/
db.moviestarts.find({'genre':{$all:['drama','action']}})

/* Q5 Search all movies where visitors exceeded expected visitors.*/
db.moviestarts.find({$expr:{$gt:['$visitors','$expectedVisitors']}})

/* Q6 Search all movies that have a title contains the letter “Su”.*/
db.moviestarts.find({'title':{$regex:/Su/}})

/* Q7 Search all movies that either have a genre of “action” and “thriller” or have a genre of “drama”, and at the same time, have more than 300000 visitors with a rating between 8 and 9.5 (inclusive).*/
db.moviestarts.find(
    {$and:[
        {$or:[
            {'genre':{$all:['action','thriller']}},
            {'genre':'drama'}
            ]
        },
        {$and:[
            {'visitors':{$gt:300000}},
            {'meta.rating':{$gte:8}},
            {'meta.rating':{$lte:9.5}}
        ]
        }
    ]})

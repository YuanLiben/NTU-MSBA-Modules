use anz

/* Q1 How many transactions are performed by each customer_id? */
db.anz.aggregate([
    {$group: { _id: {groupByCus_id:'$customer_id'},totalTransactions:{$sum:1}}}
    ])

/* Q2 Which state has customers with the highest average transaction amount? */
db.anz.aggregate([
    {$group: { _id: {groupByState:'$merchant_state'},averageTransactions:{$avg: "$amount"}}},
    {$sort:{averageTransactions:-1}}
    ]).limit(1)
/* Answer2: Australian Capital Territory (ACT) has customers with the highest average transaction amount. */

/* Q3 Monthly transaction insights – for each month, generate the number of transactions made in each merchant_state. */
db.anz.aggregate([
    {$group:{_id: {groupByMonth:{$month:{$dateFromString:{dateString: "$extraction"}}},groupByState:'$merchant_state'},totalTransactions:{$sum:1}}},
    {$sort:{_id:1}}
    ])
    
/* Q4 Demographic and locational insights – For each merchant_state, generate the amount of unique male customers and female customers. */
db.anz.aggregate([
    {$match:{'gender':'M'}},
    {$group: { _id: {groupByState:'$merchant_state'}, cusidList:{$addToSet: "$customer_id"}}},
    {$unwind:'$cusidList'},
    {$group:{_id:'$_id', uniqueMale:{$sum:1}}},
    {$sort:{_id:1}}
    ])

db.anz.aggregate([
    {$match:{'gender':'F'}},
    {$group: { _id: {groupByState:'$merchant_state'}, cusidList:{$addToSet: "$customer_id"}}},
    {$unwind:'$cusidList'},
    {$group:{_id:'$_id', uniqueFemale:{$sum:1}}},
    {$sort:{_id:1}}
    ])
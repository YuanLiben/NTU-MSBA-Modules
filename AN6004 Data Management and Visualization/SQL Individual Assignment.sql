use anz;

-- Q1 How many unique accounts are there?
select count(distinct(account)) as unique_accounts
from anz;

-- Q2 What are the currencies used in transactions?
select distinct(currency)
from anz;

-- Q3 What are the types of txn_descriptions? For each type, how many transactions are there?
select distinct(txn_description), count(*) as transactions
from anz
group by txn_description;

-- Q4 Based on the above txn_descriptions types, for each type, how many unique accounts can be observed to have performed at least 2 transactions?
select inner_table.txn_description, count(distinct(inner_table.account)) as unique_accounts
from
(select txn_description, account, count(transaction_id) as transaction_count
from anz
group by txn_description, account
having count(transaction_id) >= 2) as inner_table
group by inner_table.txn_description;

-- Q5 Are there any customers with more than one account? If so, how many?
select count(distinct(customer_id))
from anz
group by customer_id
having count(distinct(account)) > 1;
-- Answer5: There is no customer with more than one account.

-- Q6 The management believes a majority of movements is “debit”, not “credit”. Is it the case?
select distinct(movement), count(movement) as movement_count, concat(count(movement)/(select count(movement) from anz) * 100, '%') as percentage_of_movements
from anz
group by movement;
-- Answer6: Yes it is. In fact, all the movements are debit.

-- Q7 What are the top 3 most important merchants (i.e., merchants with the most transactions)?
select * from
(select merchant_id, count(transaction_id) as transactions_count, rank() over (order by count(transaction_id) desc) as merchant_rank
from anz
group by merchant_id
order by transactions_count desc) as inner_table
where inner_table.merchant_rank <= 3;

-- Q8 For each state, what are the top 3 most important merchants?
select * from
(select merchant_id, count(transaction_id) as transactions_count, merchant_state, row_number() over (partition by merchant_state order by count(transaction_id) desc) as merchant_rank
from anz
group by merchant_id
order by merchant_state asc, transactions_count desc) as inner_table
where inner_table.merchant_rank <= 3;

-- Q9 For each state, what is the total amount of transactions? 
select merchant_state, count(*) as transactions_count, round(sum(amount),2) as total_transactions_amount
from anz
group by merchant_state
order by merchant_state;

-- Q10 Related to (3), does all merchants utilized all the available forms of transactions? Provide details.
select inner_table.transactions_forms_used, count(distinct(inner_table.merchant_id)) as merchants_count, concat(count(distinct(inner_table.merchant_id))/(select(count(distinct(merchant_id)))from anz) * 100,'%') as merchant_percentage
from
(select merchant_id, count(distinct(txn_description)) as transactions_forms_used
from anz
group by merchant_id) as inner_table
group by inner_table.transactions_forms_used;
-- Answer10: No, not all merchants utilized all the available forms of transactions, only 13.5721% of merchants did so.

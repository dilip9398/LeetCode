# Write your MySQL query statement below
SELECT customer_id, count(*) As count_no_trans From Visits

WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)

GROUP BY customer_id
SELECT a.product_id, a.product_name, (a.price*sum(b.amount)) as total_sales
FROM FOOD_PRODUCT as a
JOIN FOOD_ORDER as b
ON a.product_id = b.product_id
WHERE year(b.produce_date) = 2022 AND month(b.produce_date) = 5
group by a.product_id
ORDER BY total_sales desc, a.product_id
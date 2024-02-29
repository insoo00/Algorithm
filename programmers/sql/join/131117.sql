SELECT a.product_id, a.product_name, (a.price * sum(b.amount))as total_sales
from food_product a
left join food_order b on a.product_id = b.product_id
where year(b.produce_date) = 2022 and month(b.produce_date) = 5
group by product_id
order by total_sales desc, a.product_id asc;

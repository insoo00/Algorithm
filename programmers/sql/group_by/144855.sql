SELECT category, sum(sales) as total_sales
from book a
join book_sales b on a.book_id = b.book_id
where date_format(sales_date, '%Y-%m') = '2022-01'
group by category
order by category;

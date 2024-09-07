with offline_sale_tmp as (
    select PRODUCT_ID, sum(SALES_AMOUNT) as sales_amount
    from OFFLINE_SALE
    group by PRODUCT_ID
)

select a.PRODUCT_CODE, (a.price*b.sales_amount) as sales
from PRODUCT as a
join offline_sale_tmp as b
on a.product_id = b.product_id
order by sales desc, a.PRODUCT_CODE

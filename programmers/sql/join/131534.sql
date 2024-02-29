WITH
    join_user as (
        select user_id
        from user_info
        where YEAR(JOINED) = 2021
    ),
    join_user_cnt as (
        select count(*) as cnt
        from join_user
    ),
    sale_join_user as (
        select year(sales_date) as year, month(sales_date) as month, count(distinct user_id) as puchased_users
        from online_sale
        where user_id in (select user_id from join_user)
        group by year(sales_date), month(sales_date)
    )
    
SELECT 
    YEAR, 
    MONTH,
    PUCHASED_USERS, 
    ROUND((PUCHASED_USERS / (select cnt from join_user_cnt)) ,1)AS PUCHASED_RATIO
FROM sale_join_user
with july_sum as (
    select flavor, sum(total_order) as total_order
    from july
    group by flavor
)

SELECT a.flavor
FROM FIRST_HALF as a
left JOIN july_sum as b
ON a.flavor = b.flavor
group by a.flavor
order by (a.total_order + sum(b.total_order)) desc
limit 3


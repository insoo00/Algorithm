with front as (
    select sum(code) as front_code 
    from skillcodes
    where category = 'Front End')

select id, email, first_name, last_name
from developers
where skill_code & (select front_code from front)
order by id

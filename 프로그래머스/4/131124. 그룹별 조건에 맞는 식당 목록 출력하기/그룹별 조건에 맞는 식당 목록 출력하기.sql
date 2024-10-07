select a.member_name, b.review_text, date_format(b.review_date, '%Y-%m-%d') as review_date
from MEMBER_PROFILE as a
right join REST_REVIEW as b
on a.member_id = b.member_id
where b.member_id = (
    select member_id 
    from REST_REVIEW
    group by member_id
    order by count(member_id) desc
    limit 1
)
order by review_date, review_text;
SELECT a.member_name, b.review_text, date_format(b.review_date, '%Y-%m-%d') as review_date
from member_profile a
left join rest_review b on a.member_id = b.member_id
where a.member_id in ( 
                    select member_id from rest_review
                    group by member_id
                    having count(*) = ( select count(*) from rest_review group by member_id
                                        order by count(*) desc  
                                        limit 1
                                    )
                    )
order by review_date, review_text;
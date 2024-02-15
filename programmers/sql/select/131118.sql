SELECT a.REST_ID, a.REST_NAME, a.food_type, a.favorites, a.address, round(avg(b.review_score), 2) as score
FROM REST_INFO as a
inner JOIN REST_REVIEW as b ON a.rest_id = b.rest_id
GROUP BY a.rest_id
having a.address like '서울%'
order by score desc, favorites desc

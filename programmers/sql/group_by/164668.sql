SELECT user_id, nickname, sum(price) as total_sales
from USED_GOODS_BOARD b
inner join USED_GOODS_USER u on b.writer_id = u.user_id
where b.STATUS	= 'DONE'
GROUP by b.writer_id
having total_sales >= 700000
order by total_sales asc;
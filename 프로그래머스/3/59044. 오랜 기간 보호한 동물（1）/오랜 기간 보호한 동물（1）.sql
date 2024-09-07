select a.name, a.datetime
from ANIMAL_INS as a
left join ANIMAL_OUTS as b
on a.animal_id = b.animal_id
where b.animal_id is NULL
order by a.datetime
limit 3
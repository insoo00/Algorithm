select a.animal_id, a.animal_type, a.name
from ANIMAL_INS as a
join ANIMAL_OUTS as b
on a.animal_id = b.animal_id
where a.SEX_UPON_INTAKE like 'Intact%'
and (b.SEX_UPON_OUTCOME like 'Spayed%' or b.SEX_UPON_OUTCOME like 'Neutered%')
order by a.animal_id asc
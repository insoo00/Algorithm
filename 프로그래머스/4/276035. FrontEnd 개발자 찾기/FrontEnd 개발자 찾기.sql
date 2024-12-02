with SKILLCODES_TMP as (
    select CATEGORY, BIN(CODE) as CODE
    from SKILLCODES
),
DEVELOPERS_TMP as (
    select id, first_name, last_name, email, BIN(SKILL_CODE) as SKILL_CODE
    from DEVELOPERS
)

select distinct a.id, a.email, a.first_name, a.last_name
from DEVELOPERS_TMP as a 
left join SKILLCODES_TMP as b
on ((a.skill_code - b.code) not like '%9%')
# on a.SKILL_CODE & b.CODE = b.CODE
where b.category = 'Front End'
order by a.id;
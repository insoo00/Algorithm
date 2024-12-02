# with SKILLCODES_TMP as (
#     select CATEGORY, BIN(CODE) as CODE
#     from SKILLCODES
# ),
# DEVELOPERS_TMP as (
#     select id, first_name, last_name, email, BIN(SKILL_CODE) as SKILL_CODE
#     from DEVELOPERS
# )

# select distinct a.id, a.email, a.first_name, a.last_name
# from DEVELOPERS_TMP as a 
# left join SKILLCODES_TMP as b
# on ((a.skill_code - b.code) not like '%9%')
# where b.category = 'Front End'
# order by a.id;

SELECT DISTINCT A.ID, A.EMAIL, A.FIRST_NAME, A.LAST_NAME
    FROM DEVELOPERS AS A
        INNER JOIN SKILLCODES AS B
        ON (A.SKILL_CODE & B.CODE = B.CODE) 
WHERE B.CATEGORY = 'Front End'
ORDER BY A.ID ASC
;
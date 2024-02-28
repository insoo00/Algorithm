WITH 
    FRONT AS (
        SELECT SUM(CODE) AS CODE
        FROM SKILLCODES
        WHERE CATEGORY='FRONT END'
    ),
    PYTHON AS (
        SELECT CODE
        FROM SKILLCODES
        WHERE NAME = 'Python'
    ),
    CSHAP AS (
        SELECT CODE
        FROM SKILLCODES
        WHERE NAME = 'C#'
    )

SELECT
    CASE
        WHEN (D.SKILL_CODE & (SELECT CODE FROM FRONT)) AND (D.SKILL_CODE & (SELECT CODE FROM PYTHON)) THEN 'A'
        WHEN D.SKILL_CODE & (SELECT CODE FROM CSHAP) THEN 'B'
        WHEN D.SKILL_CODE & (SELECT CODE FROM FRONT) THEN 'C'
    END AS GRADE,
    D.ID,
    D.EMAIL
FROM DEVELOPERS D
HAVING GRADE IS NOT NULL
ORDER BY GRADE, ID
    
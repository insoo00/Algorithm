SELECT count(*) as users
FROM USER_INFO
WHERE YEAR(JOINED) = 2021 AND age between 20 and 29
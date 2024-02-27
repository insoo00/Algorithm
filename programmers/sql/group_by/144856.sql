SELECT b.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, sum(b.price*s.sales) as TOTAL_SALES
FROM BOOK b
JOIN AUTHOR a on b.author_id = a.author_id
JOIN BOOK_SALES s on b.book_id = s.book_id
WHERE DATE_FORMAT(s.sales_date, '%Y-%m') = '2022-01'
GROUP BY b.author_id, b.category
ORDER BY b.AUTHOR_ID asc, b.CATEGORY desc;

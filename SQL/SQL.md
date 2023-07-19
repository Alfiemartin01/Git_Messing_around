SELECT title, release_date 
FROM movielens
WHERE id LIKE "%0" AND title LIKE "%I%"
ORDER BY id DESC
LIMIT 5 OFFSET 1;


###### 1. list all actors
SELECT *
FROM actor;

###### 2. Find the surname of the actor with the forename 'John'.
SELECT last_name
FROM actor
WHERE first_name = 'John';

###### 3. Find all actors with surname 'Neeson'
SELECT *
FROM actor
WHERE last_name = 'Neeson';

###### 4. Find all actors with ID numbers divisible by 10.
SELECT *
FROM actor
WHERE actor_id%10 = 0;

###### 5. What is the description of the movie with an ID of 100?
SELECT description, film_id
FROM film
WHERE film_id = 100;

###### 6. Find every R-rated movie.
SELECT title, rating
FROM film
WHERE rating = 'R';

###### 7. Find every non-R-rated movie.
SELECT title, rating
FROM film
WHERE rating <> 'R';

###### 8. Find the ten shortest movies.
SELECT title, length
FROM film 
ORDER BY length ASC
LIMIT 10;

###### 9. Find the movies with the longest runtime, without using LIMIT.

SELECT title, length
FROM film
WHERE length = (SELECT MAX(LENGTH) FROM film);

###### 10. Find all movies that have deleted scenes.
SELECT TITLE, special_features
FROM film
WHERE special_features = 'Deleted Scenes';

###### 11. Using HAVING, reverse-alphabetically list the last names that are not repeated.
SELECT last_name, count(last_name) as total
FROM actor
GROUP BY last_name
HAVING total = 1
ORDER BY last_name DESC;
 
###### 12. Using HAVING, list the last names that appear more than once, from highest to lowest frequency.
SELECT last_name, count(last_name) as total
FROM actor
GROUP BY last_name
HAVING total > 1
ORDER BY total DESC;

###### 13. Which actor has appeared in the most films?
SELECT actor_id,count(actor_id) AS no_of_films
FROM film_actor
GROUP BY (actor_id)
ORDER BY no_of_films DESC
LIMIT 1;

SELECT actor_id, first_name, last_name
FROM actor
WHERE actor_id = 107;


###### 14.  When is 'Academy Dinosaur' due?

###### 15. What is the average runtime of all films?
SELECT AVG(length) as avg_len
FROM film_list;

###### 16. List the average runtime for every film category.
SELECT category, AVG(length) as avg_len
FROM film_list
GROUP BY category;

###### 17. List all movies featuring a robot.
SELECT title
FROM film_list
WHERE description LIKE '%robot%';

###### 18. How many movies were released in 2010?
SELECT release_year, COUNT(release_year) as ryc
FROM film 
GROUP BY release_year
HAVING release_year = 2010;

###### 19. Find the titles of all the horror movies.
SELECT title,category
FROM film_list
WHERE category LIKE "%horror%" OR category LIKE "%Horror%";

###### 20. List the full name of the staff member with the ID of 2.
SELECT name
FROM staff_list
WHERE ID = 2;

###### 21. List all the movies that Fred Costner has appeared in.
SELECT title
FROM film_list
WHERE actors LIKE '%Fred Costner%';

How many distinct countries are there?
List the name of every language in reverse-alphabetical order.
List the full names of every actor whose surname ends with '-son' in alphabetical order by their forename.
Which category contains the most films?
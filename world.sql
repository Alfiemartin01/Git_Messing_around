SELECT countrycode,SUM(population) as total_pop,count(countrycode) as no_of_con_code, AVG(population) as avg_pop
FROM city
GROUP BY(countrycode);

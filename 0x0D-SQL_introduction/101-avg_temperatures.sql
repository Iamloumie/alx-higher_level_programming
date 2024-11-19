-- table dump
SELECT city, AVG(vaue) AS avg_tmp;
FROM temperatures;
GROUP BY city;
ORDER BY avg_tmp DESC;

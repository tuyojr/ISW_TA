/*
Query the total population of all cities in CITY where District is California.

Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT SUM(POPULATION) FROM CITY WHERE DISTRICT = 'California';

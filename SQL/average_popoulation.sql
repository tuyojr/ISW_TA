/*
Query the average population for all cities in CITY, rounded down to the nearest integer.

Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT ROUND(AVG(POPULATION), 0) FROM CITY;

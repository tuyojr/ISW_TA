/*
Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
where LAT_N is the northern latitude and LONG_W is the western longitude.

Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT DISTINCT CITY FROM STATION WHERE CITY NOT LIKE 'a%' AND 
  CITY NOT LIKE 'e%' AND CITY NOT LIKE 'i%' AND CITY NOT LIKE 'o%' AND 
  CITY NOT LIKE 'u%';

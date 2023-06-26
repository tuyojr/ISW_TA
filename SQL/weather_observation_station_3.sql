/*
Query a list of CITY names from STATION for cities that have 
an even ID number. Print the results in any order, but exclude 
duplicates from the answer.

Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT DISTINCT CITY FROM STATION WHERE ID % 2 = 0;
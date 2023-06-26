/*
Write a query that prints a list of employee names (i.e.: the name attribute)
for employees in Employee having a salary greater than $2000 per month who have
been employees for less than 10 months. Sort your result by ascending employee_id.

Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a
single line to avoid error.
*/

SELECT name FROM Employee WHERE salary > 2000 AND months < 10 ORDER BY employee_id ASC;

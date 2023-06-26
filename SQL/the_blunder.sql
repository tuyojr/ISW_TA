/*
Samantha was tasked with calculating the average monthly salaries for
all employees in the EMPLOYEES table, but did not realize her keyboard's
key was broken until after completing the calculation. She wants your help
finding the difference between her miscalculation (using salaries with any
zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: actual - miscalculated
average monthly salaries), and round it up to the next integer.

NOTE: Salary is per month

Constraints
1000 < Salary < 10^5

Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT FLOOR(AVG(SALARY) - AVG(CAST(REPLACE(CAST(SALARY AS VARCHAR(10)), '0', '') AS INT)) +1) FROM EMPLOYEES;

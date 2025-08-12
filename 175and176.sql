175: Combine Tables
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.

Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
 

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:
FirstName, LastName, City, State

================================================
select p.FirstName, p.LastName, a.city,a.state
from Person p
left join Address a
on p.personId=a.personId;
============================================================================================================================================================================

============================================================================================================================================================================
176: Second Highest Salary
Write a SQL query to get the second highest salary from the Employee table.
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
====================================================

  SELECT IFNULL(
    (
    SELECT DISTINCT Salary
    from Employee
    order by salary DESC
    LIMIT 1 OFFSET 1
    ),  NULL
) as SecondHighestSalary;
============================================================================================================================================================================

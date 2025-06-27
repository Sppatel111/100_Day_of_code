--CREATE TABLE Worker (
--    WORKER_ID INT NOT NULL PRIMARY KEY identity(1,1),
--    FIRST_NAME CHAR(25),
--    LAST_NAME CHAR(25),
--    SALARY INT,
--    JOINING_DATE DATETIME,
--    DEPARTMENT CHAR(25)
--)
postgres:
CREATE TABLE Worker (
    WORKER_ID SERIAL  NOT NULL  PRIMARY KEY ,
    FIRST_NAME CHAR(25),
    LAST_NAME CHAR(25),
    SALARY INT,
    JOINING_DATE TIMESTAMP,
    DEPARTMENT CHAR(25)
)

--SET IDENTITY_INSERT Worker ON;
--
--INSERT INTO Worker
--(WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) VALUES
--(001, 'Monika', 'Arora', 100000, '2014-02-20 09:00:00', 'HR'),
--(002, 'Niharika', 'Verma', 80000, '2014-06-11 09:00:00', 'Admin'),
--(003, 'Vishal', 'Singhal', 300000, '2014-02-20 09:00:00', 'HR'),
--(004, 'Amitabh', 'Singh', 50000, '2014-02-20 09:00:00', 'Admin'),
--(005, 'Vivek', 'Bhati', 500000, '2014-06-11 09:00:00', 'Admin'),
--(006, 'Vipul', 'Diwan', 200000, '2014-06-11 09:00:00', 'Account'),
--(007, 'Satish', 'Kumar', 75000, '2014-01-20 09:00:00', 'Account'),
--(008, 'Geetika', 'Chauhan', 90000, '2014-04-11 09:00:00', 'Admin');

postgres:
INSERT INTO Worker
( FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) VALUES
('Monika', 'Arora', 100000, '2014-02-20 09:00:00', 'HR'),
('Niharika', 'Verma', 80000, '2014-06-11 09:00:00', 'Admin'),
('Vishal', 'Singhal', 300000, '2014-02-20 09:00:00', 'HR'),
('Amitabh', 'Singh', 50000, '2014-02-20 09:00:00', 'Admin'),
('Vivek', 'Bhati', 500000, '2014-06-11 09:00:00', 'Admin'),
('Vipul', 'Diwan', 200000, '2014-06-11 09:00:00', 'Account'),
('Satish', 'Kumar', 75000, '2014-01-20 09:00:00', 'Account'),
('Geetika', 'Chauhan', 90000, '2014-04-11 09:00:00', 'Admin');


--SET IDENTITY_INSERT Worker OFF;


--CREATE TABLE Bonus (
--    WORKER_REF_ID INT,
--    BONUS_AMOUNT INT,
--    BONUS_DATE DATETIME,
--    FOREIGN KEY (WORKER_REF_ID)
--        REFERENCES Worker(WORKER_ID)
--        ON DELETE CASCADE
--)

postgress:
CREATE TABLE Bonus (
    WORKER_REF_ID INT,
    BONUS_AMOUNT INT,
    BONUS_DATE TIMESTAMP,
    FOREIGN KEY (WORKER_REF_ID)
        REFERENCES Worker(WORKER_ID)
        ON DELETE CASCADE
)

INSERT INTO Bonus
(WORKER_REF_ID, BONUS_AMOUNT, BONUS_DATE) VALUES
(001, 5000, '2016-02-20'),
(002, 3000, '2016-06-11'),
(003, 4000, '2016-02-20'),
(001, 4500, '2016-02-20'),
(002, 3500, '2016-06-11')



--CREATE TABLE Title (
--    WORKER_REF_ID INT,
--    WORKER_TITLE CHAR(25),
--    AFFECTED_FROM DATETIME,
--    FOREIGN KEY (WORKER_REF_ID)
--        REFERENCES Worker(WORKER_ID)
--		ON DELETE CASCADE
--)
postgres:
CREATE TABLE Title (
    WORKER_REF_ID INT,
    WORKER_TITLE CHAR(25),
    AFFECTED_FROM TIMESTAMP,
    FOREIGN KEY (WORKER_REF_ID)
        REFERENCES Worker(WORKER_ID)
		ON DELETE CASCADE
)

INSERT INTO Title 
(WORKER_REF_ID, WORKER_TITLE, AFFECTED_FROM) VALUES
(001, 'Manager', '2016-02-20 00:00:00'),
(002, 'Executive', '2016-06-11 00:00:00'),
(008, 'Executive', '2016-06-11 00:00:00'),
(005, 'Manager', '2016-06-11 00:00:00'),
(004, 'Asst. Manager', '2016-06-11 00:00:00'),
(007, 'Executive', '2016-06-11 00:00:00'),
(006, 'Lead', '2016-06-11 00:00:00'),
(003, 'Lead', '2016-06-11 00:00:00')



--1. Write a SQL query to print first 3 characters of first name from Worker table.

select substring(first_name,1,3) from worker;

--2. Write a SQL query to find a position of alphbet 'A' in first name column 'Amitabh' from Worker table.

	select position('A' in first_name) from worker where first_name='Amitabh';

--3. Print first name column after removing the right side spaces from names.

select trim(first_name) from worker;

--4. Replace 'A' with 'A' in Wroker table, first name column.

select replace(first_name,'A','A') from worker;

--5. Write a query for get details who have joined in feb'2014.

SELECT * FROM worker WHERE joining_date BETWEEN  '2014-02-01' AND '2014-02-28';

--6. Write a query to fetch workers names with salary >=50000 and <=100000.

select first_name from worker where salary>=50000 and salary<=100000;

--7. Write a query to fetch the no. of workers for each department in the des order.

select department, count(worker_id)from worker group by department order by count(worker_id) desc;

--8. Write a query to print details about workers who are also managers.

select * from worker where worker_id=any(select worker_ref_id from title where worker_title='Manager');

--9. Write a query to fetch duplicate records from Title table having matching data in some field of a table.

--select * from title where worker_title in(select worker_title from title group by worker_title having count(*) > 1);

SELECT worker_title, COUNT(*) AS count FROM Title GROUP BY worker_title HAVING COUNT(*) > 1;

--10. Write a query to only shows the odd rows from the table.
select * from worker where worker_id % 2 <>0;

--11. Write a query to clone a table with data.

create table worker_2 as table worker;

--12. Write a query to fetch intersecting records of two tables.

select worker_id from worker intersect select worker_ref_id from title;
select worker_id from worker intersect select worker_ref_id from bonus;

--13. Write a query ro show records from one table that another table does not have.
select worker_id from worker except select worker_ref_id from bonus;

--14. Write a query to determine the 5th highest salary without using top.

select distinct salary from worker order by salary desc offset 4 limit 1;

--15. Write a query to fetch the list of employee with the same salary.
***
select worker_id,count(*) as count from worker group by salary having count(*) >1;
select salary,count(salary) as count from worker group by worker_id having count(*) >1;

SELECT salary,COUNT(*) AS COUNT
FROM worker
WHERE salary IN (
    SELECT salary
    FROM worker
    GROUP BY salary
    HAVING COUNT(*) > 1
) GROUP BY salary;

select * from worker group by salary having count(salary)>1;


--16. Write a query to show second highest salary from a table.

select distinct salary from worker order by salary desc offset 1 limit 1;
--17. Write a query to show one row twice in results from a table.


--18. Write a query to fetch 50% records from a table.

select * from worker limit (select count(*) from worker)/2;

--19. Write a query to fetch last record from a table.

select * from worker offset (select count(*) from worker)-1 limit 1;

--20. Write a query to fetch last five records from a table.

select * from worker offset (select count(*)  from worker)-5  limit 5;

--21. Write a query to print the no. of employees having the highest salary in each department.

select w.department,count(w.worker_id) from worker w  where w.salary in
select max(salary) from worker group by department) group by w.department;

--22. Write a query to fetch three max salaries from a table.

select salary from worker order by salary desc limit 3;

--23. Write a query to fetch the department that have less than 4 people in it.

select department ,count(worker_id) from worker  group by department having count(worker_id) < 4 ;

--24. Writa a query to fetch Nth min salaries from a table.

select salary from worker order by salary offset N-1 limit 1;
--where N=5,
select salary from worker order by salary offset 4 limit 1;

--25. Write a query to fetch the names of workers who earn the highest salary.

select first_name from worker order by salary desc limit 1;

--26. List all workers who never received any bonus.

select * from worker where worker_id  not  in(select worker_ref_id from bonus);

--27. Find workers who got the highest bonus amount.

select * from worker where worker_id in(select worker_ref_id from bonus order by bonus_amount desc limit 1);

--28. Get the latest title for each worker.

--SELECT DISTINCT ON (WORKER_REF_ID) WORKER_REF_ID, WORKER_TITLE, AFFECTED_FROM
--FROM Title ORDER BY WORKER_REF_ID, AFFECTED_FROM DESC;

select distinct on (worker_ref_id)  * from title order by worker_ref_id,affected_from desc;

--29. Show department-wise total and average salary.

select department,sum(salary) as total ,avg(salary) as average from worker group by department;

--30. List workers whose salary is above the average salary of their department.

select * from worker w where w.salary > any(select avg(salary) from worker group by department);

--31. Show workers whose latest title is �Manager�.

select * from worker where worker_id=any(select worker_ref_id from title where worker_title='Manager');

--32. Rank workers by salary within each department.

select *, RANK() OVER (partition by department order by salary desc) as salary_rank from worker;

--33. Find workers who changed their title more than once.
***
SELECT WORKER_REF_ID FROM Title GROUP BY WORKER_REF_ID HAVING COUNT(DISTINCT WORKER_TITLE) > 1;

--34. Find departments that have more than 3 workers.

select department ,count(worker_id) from worker  group by department having count(worker_id) > 3 ;

--35. Display the highest bonus given in each year.
***
select * from bonus group by DATE_PART('Year',bonus_date) order by bonus_amount desc limit 1  ;

--36. List all workers and their total bonus amount (even if 0).
***
select *,bonus from workers where worker_id=any(select worker_ref_id from bonus where bonus_amount )

SELECT w.worker_id, w.first_name, w.last_name, COALESCE(SUM(b.bonus_amount), 0) AS total_bonus
FROM worker w
LEFT JOIN bonus b ON w.worker_id = b.worker_ref_id
GROUP BY w.worker_id, w.first_name, w.last_name;


--37. Identify workers who have received bonuses in consecutive months.

--38. For each worker, show the title history with row numbers.

--39. Find workers who received a bonus in their joining year.

--40. List workers who were promoted (i.e., their title changed) within 1 year of joining.

--41. Find workers who never had the title "Lead".

--42. List the titles that have been held by more than one worker.

--43. Show the salary gap between highest and lowest paid worker in each department.

--44. Get workers who joined in the same year a bonus was issued to them.

--45. Get the average bonus per department.

--46. Show the second highest salary in each department.

--47. Find workers who have the same salary as someone in a different department.

--48. Get the top 3 earners in the entire company.

--49. Find workers who received bonuses more than once in the same year.

--50. Show workers who received a bonus before joining (data anomaly check).

--51. For each worker, show the number of days between their joining and first title change.

--52. Find workers who received a bonus every year since they joined (inclusive).

--53. List workers whose bonus amount ever exceeded their salary.

--54. Show workers who got a new title within 30 days after receiving a bonus.

--55. Show workers who have had more than 2 different titles in their career.


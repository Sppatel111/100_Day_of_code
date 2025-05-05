--Exercise � 1

create table EmpDetails(
	Empid int primary key,
	EmpName	varchar(20),
	Department varchar(10),
	ContactNo varchar(20),
	EmailId varchar(50),
	EmpHeadId int
)

insert into EmpDetails values
	(101, 'Isha', 'E-101', '1234567890', 'isha@gmail.com', 105),
	(102, 'Priya', 'E-104', '1234567890', 'priya@yahoo.com', 103),
	(103, 'Neha', 'E-101', '1234567890', 'neha@gmail.com', 101),
	(104, 'Rahul', 'E-102', '1234567890', 'rahul@yahoo.com', 105),
	(105, 'Abhishek', 'E-101', '1234567890', 'abhishek@gmail.com', 102)
	
create table EmpDept(
	DeptId varchar(50) primary key,
	DeptName varchar(100), 
	Dept_off varchar(100), 
	DeptHead int foreign key references EmpDetails(Empid)
)
##changed
create table EmpDept(
	DeptId varchar(50) primary key,
	DeptName varchar(100),
	Dept_off varchar(100),
	DeptHead int  references EmpDetails(Empid)
)


insert into EmpDept values
	('E-101', 'HR', 'Monday', 105),
	('E-102', 'Development', 'Tuesday', 101),
	('E-103', 'Hous Keeping', 'Saturday', 103),
	('E-104', 'Sales', 'Sunday', 104),
	('E-105', 'Purchage', 'Tuesday', 104)


create table EmpSalary(
	EmpId int foreign key references EmpDetails(EmpId), 
	Salary bigint, 
	IsPermanent varchar(3)
	)
##chaged

create table EmpSalary(
	EmpId int references EmpDetails(EmpId),
	Salary bigint,
	IsPermanent varchar(3)
	)

insert into EmpSalary values
	(101, 2000, 'Yes'),
	(102, 10000, 'Yes'),
	(103, 5000, 'No'),
	(104, 1900, 'Yes'),
	(105, 2300, 'Yes')


create table Project(
	ProjectId varchar(50) primary key,
	Duration int
)

insert into Project values
	('p-1', 23),
	('p-2', 15),
	('p-3', 45),
	('p-4', 2),
	('p-5', 30)


create table Country(
	cid varchar(50) primary key, 
	cname varchar(100)
)


insert into Country values
	('c-1', 'India'),
	('c-2', 'USA'),
	('c-3', 'China'),
	('c-4', 'Pakistan'),
	('c-5', 'Russia')


create table ClientTable(
	ClientId varchar(50) primary key, 
	ClientName varchar(100), 
	cid varchar(50) references country(cid)
)


insert into ClientTable values
	('cl-1', 'ABC Group', 'c-1'),
	('cl-2', 'PQR', 'c-1'),
	('cl-3', 'XYZ', 'c-1'),
	('cl-4', 'tech altum', 'c-3'),
	('cl-5', 'mnp', 'c-5')


create table EmpProject(
	EmpId int foreign key references EmpDetails(EmpId), 
	ProjectId varchar(50) foreign key references Project(ProjectId), 
	ClientID varchar(50) foreign key references ClientTable(ClientID),
	StartYear int, 
	EndYear int
)

##changed
create table EmpProject(
	EmpId int  references EmpDetails(EmpId),
	ProjectId varchar(50)  references Project(ProjectId),
	ClientID varchar(50)  references ClientTable(ClientID),
	StartYear int,
	EndYear int
)

insert into EmpProject values
	(101, 'p-1', 'Cl-1', '2010', '2010'),
	(102, 'p-2', 'Cl-2', '2010', '2012'),
	(103, 'p-1', 'Cl-3', '2013', ''),
	(104, 'p-4', 'Cl-1', '2014', '2015'),
	(105, 'p-4', 'Cl-5', '2015', '')

##changed
insert into EmpProject values
	(101, 'p-1', 'cl-1', 2010, 2010),
	(102, 'p-2', 'cl-2', 2010, 2012),
	(103, 'p-1', 'cl-3', 2013, NULL),
	(104, 'p-4', 'cl-1', 2014, 2015),
	(105, 'p-4', 'cl-5', 2015, NULL)

Question:

--1. Select the detail of the employee whose name start with P.
--2. How many permanent candidate take salary more than 5000.
--3. Select the detail of employee whose emailId is in gmail.
--4. Select the details of the employee who work either for department E-104 or E-102.
--5. What is the department name for DeptID E-102?
--6. What is total salary that is paid to permanent employees?
--7. List name of all employees whose name ends with a.
--8. List the number of department of employees in each project.
--9. How many project started in year 2010.
--10. How many project started and finished in the same year.
--11. select the name of the employee whose name's 3rd charactor is 'h'.
--12. Select the department name of the company which is assigned to the employee whose employee id is grater 103.
--13. Select the name of the employee who is working under Abhishek.
--14. Select the name of the employee who is department head of HR.
--15. Select the name of the employee head who is permanent.
--16. Select the name and email of the Dept Head who is not Permanent.
--17. Select the employee whose department off is Monday
--18. Select the indian clinets details.
--19. Select the details of all employee working in development department.
--20. Select the client name, who has worked on one project at least for one year and half year.
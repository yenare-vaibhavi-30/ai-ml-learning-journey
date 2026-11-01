create database school;
use school;
create table teacher (
id int primary key auto_increment,
fname varchar(20),
lname varchar(20),
desig varchar(30),
dept varchar(20));
desc teacher;
insert into teacher (id , fname, lname, desig, dept)
Values
(1, "Raju", "Rastogi", "teacher", "dept");
insert into teacher ( fname, lname, desig, dept)
Values
("Sham", "Mohan", "HOD", "DBMS"),
("Baburao", "Apte", "teacher", "Teaching"),
("Paul", "Philip", "Teacher", "IT"),
("Deva", "Mahajan", "Teacher", "IT"),
("Ram", "Deve", "teacher", "IT");
select * from teacher;
select * from teacher
order by fname;
select * from teacher
order by fname DESC;
select fname , desig from teacher
order by dept, fname ;
select * from teacher
where desig like "%HOD%";
select * from teacher
where fname like"____";
select * from teacher
where fname like "R___";
ALTER TABLE teacher
ADD column
salary INT NOT NULL default 25000;
select * from teacher limit 5;
show tables;
select count(*) from teacher;
select count(distinct dept) from teacher;
select * from teacher;
select dept, count(*) from teacher group by dept;
select * from teacher order by fname DESC;
select * from teacher order by fname asc;
select * from teacher order by dept desc;
select * from teacher limit 3;
select * from teacher limit 5;
select * from teacher
where  fname like "R%";
select * from teacher 
where lname like "____";
select dept, count(fname) from teacher GROUP BY dept ;
select desig from teacher group by desig;
select desig , count(fname) from teacher group by desig;
select max(salary) from teacher;
select min(salary) from teacher;
select id , fname, salary from teacher 
where
salary = (select max(salary) from teacher);
select dept , SUM(salary) FROM teacher
GROUP BY dept;
select dept , count(id), SUM(salary) from teacher 
group by dept;

-- find total no of teachers in database-- 
SELECT  COUNT(id)
FROM teacher;

-- find no of employees in each department
select id , fname, salary from teacher 
where
salary = (select max(salary) from teacher);

-- find the lowest salary paying
select * from teacher 
where
salary = (select max(salary) from teacher)  ;

-- find highest salary paying
select min(salary) from teacher;

-- find total salary paying in loan department
select sum(salary) from teacher
where dept = "IT";

-- average salary paying in each department
select dept , avg(salary) from teacher 
group by dept;

-- DataType
-- 1) Decimal
-- THE MAXIMUM NUMBER OF DIGITS FOR DECIMAl IS 65
-- DECIMAL(5 , 2);
-- 5 = Total digit
-- 2 = Digit after decimal
-- 119.12 allowd
-- 28.15 allowd
-- 1150.15 not allowd
create table num 
(d decimal);
desc num;
insert into num1 values(11.45);

-- 2) float and double
-- float - upto ~7 digits, takes 4 bytes of memory
-- double - upto ~15 digits, takes 8 bytes of memory
 create table num2
(f FLOAT , d DOUBLE);
desc num2;
insert into num2 values (123.456, 123.456);
select * from num2;
insert into num2 values (123.12334566 , 123.4567854);
select * from num2;

-- 3) Date, Time and datetime

create table person
(jd date,
jt time,
jdt datetime
);
desc person;

insert into person 
value
("2022-04-17", "23:00:00", "2023-05-16 22:04:23");

select * from person;

-- 4) date time functions
-- curdate , curtime , now
-- syntax
-- CURDATE() = yyyy-mm-dd
-- CURTIME() = hh:mm:ss
-- NOW() = yyyy-mm-dd hh:mm:ss
select curdate();  -- current date deil
select curtime();

-- 5) DATE_FORMAT();
--  DATE_FORMAT(now(), '%D %a at %T');
--  Result: 21st Tue 21:21:34
--  DATE_FORMAT(now(), '%m/%d/%y')
--  Result : 04/16/23
select date_format(now(), '%d/%m/%y');

-- 6) math date
-- DATEDIFF(expr1 , expr2)
-- DATA_ADD(data, INTERVAL expr unit)
-- DATA_SUB(data, INTERVAl expr unit)
select DATEDIFF('2025-11-27','2025-11-30');
select DATE_ADD('2023-05-01', INTERVAL 1 DAY);
select DATE_ADD(now(), INTERVAL 1 month);
select DATE_SUB('2023-04-21', interval 1 month);

-- 7) TIMEDIFF(expr1, expr2)
-- TIMEDIFF('20:00:00', '18:00:00');
select timediff('23:00:30', '20:00:50');

-- 8) default and on update timestamp
create table blogs (
text varchar(150),
created_at datetime default current_timestamp,
updated_at datetime ON update current_timestamp
);

create database containt;

use containt;

create table blogs(
blog varchar(150),
ct datetime default current_timestamp,
ut datetime on update current_timestamp
);
desc blogs;
insert into blogs (blog)
values ('This is my first bolg');
select * from blogs;
UPDATE blogs 
SET blog = 'This is my first blog from India';
-- 1 . Print the current time (HH:MM:SS)
-- 2. Print the current date (yyyy-mm-dd)
-- 3. Print the current day of the week (Monday, Tuesday…)
--  4. What is the use case of CHAR datatype?
--  5. Which datatype can store value 123.456?
-- 6. Display date in the given formats
-- 🔵 Format: dd:mm:yyyy
-- 🔵 Format: "April 22nd at 22:00:00"

create database College;
use College;
create table info (
id int primary key ,
name varchar(20),
class varchar(30),
city varchar(20),
mobileNo int,
age int);
desc info;
insert into info
(id, name , class, city, mobileNo, age)
value
(1, "Ram", "BCA", "Pune", 346364, 20),
(2, "sham" , "BCA", "Pune", 87789, 21),
(3, "Nadu", "BCS", "Pune", 8765438, 21),
(4 , "Sita", "BTech", "Nashik", 98766, 21),
(5, "Isha", "BE", "Nagpur", 987659, 21);
insert into info
(id, name , class, city, mobileNo, age)
value
(6, "Mohini", "BCA", "Pune", 3987667, 22);
alter table info 
add column collName varchar(20) default "APJ College";
update info 
set name = "Yogesh" , city = "Mumbai"
where id = 5;
delete from info 
where id = 2;
alter table info 
drop column mobileNo;
alter table info
rename to information;
select * from information;
alter table information
rename to info;
alter table info
change column city location varchar(20);
alter table info
add column departId int default 2;
alter table info 
modify departId int(2) default 4;
select name ,age 
from info 
where age > 20;
select name , age , id
from info
where age > 20 and id > 4;
select name , age , location
from info 
where age between 21 and 27 ;
select name , class , age
from info
where class in ('BCA', 'BE') ;
select name , age , location 
from info
where age > 20 limit 2;
select name, age, location 
from info 
order by name asc;
select age , count(id)
from info
group by age;
select id , max(age)
from info
group by id
having max(age) > 20;
SELECT id, MAX(age)
FROM info
GROUP BY id
HAVING MAX(age) > 20;
select * from info;

DROP DATABASE studentdb;



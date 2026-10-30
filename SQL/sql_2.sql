-- create a database for your college.
-- create a table named teacher to store (id, name, subject, salary)
-- insert following data in the table:
--      23, "ajay", "math", 50000
--      47, "bharat", "english", 60000
--      18, "chetan", "chemistry", 45000
--      9, "divya", "physics", 75000

create database college1;
use college1;

create table teacher(
   id int primary key, name varchar (25), subject varchar(20), salary int
);

insert into teacher 
value
   (23, "ajay", "math", 50000),
   (47, "bharat", "english", 60000),
   (18, "chetan", "chemistry", 45000),
   (9, "divya", "physics", 75000);
   
   
-- select teachers whose salary is more than 55k
select name, max(salary)
from teacher
group by name 
having max(salary) > 55000;

-- rename the salary column of teacher table to ctc
alter table teacher
change column salary payment int default 0;
   
   
-- update salary of all teachers by giving them an increment of 25%
UPDATE teacher
SET payment = payment + payment * 0.25;

select * from teacher;





create database college;
create database xyz;
use college;

create table student(
 rollno INT,
 name varchar(30),
 age INT
);

INSERT INTO student
values
(101, "adam", 12),
(102, "om", 14);

select * from student;


create database if not exists instagram;

use instagram;

create table user (
   id INT,
   age int,
   name varchar(30) not null,
   email varchar(50) unique,
   followers int default 0,
   following int, 
   constraint check (age >= 13),
   primary key (id)
);

INSERT INTO user
(id , age , name, email, followers, following)
values
(1,14, "adam", "adam123@gmail.com", 128, 145),
(2, 15, "om", "om432@gamil.com", 234, 243),
(3, 16, "ram", "ram321@gmail.com", 243, 183),
(4, 17, "sham", "sham234@gmail.com", 231, 232);

INSERT INTO user
(id , age , name, email, followers, following)
values
(1,14, "adam", "sneha123@gmail.com", 128, 145),
(2, 15, "om", "yogi231@gamil.com", 234, 243);

select name, age 
from user
where age < 16;

select name, age, followers
from user
where age > 15 and followers > 200;

select name, age, followers
from user
where age > 15 or followers > 200;

select name, age, followers
from user
where age between 15 and 17;

select name, email, followers
from user
where email in ("sham234@gmail.com", "ram321@gmail.com", "gori@123gmail.com");

select name, age, email
from user
where age not in (15, 16);

select name, age, email
from user
where age > 14
limit 2;

select name, age, followers
from user
order by followers desc ;

select count(age)
from user
where age = 14;

select * from user;

CREATE DATABASE students;

USE students;

create table student(
   student_id INT NOT NULL,
   name VARCHAR(25) NOT NULL,
   sex VARCHAR(25) NOT NULL,
   age INT NOT NULL,
   PRIMARY KEY ( student_id )
);

insert into student (student_id, name, sex, age) 
values (1, "Alice", "Female", 20);
insert into student (student_id, name, sex, age) 
values (2, "Bob", "Male", 21);
insert into student (student_id, name, sex, age) 
values (3, "Peter", "Male", 22);
insert into student (student_id, name, sex, age) 
values (4, "George", "Male", 27);
insert into student (student_id, name, sex, age) 
values (5, "William", "Male", 28);
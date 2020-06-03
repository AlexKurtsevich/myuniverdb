--НАЧАЛО СКРИПТА------------------------------------------------------------

insert into Faculty(id,name) values (1,'Faculty of Arts');
insert into Faculty(id,name) values (2,'Faculty of Applied Mathematics');

insert into FGroup(id,faculty_id) values (1,1); 
insert into FGroup(id,faculty_id) values (2,1); 
insert into FGroup(id,faculty_id) values (3,2); 

insert into Student(id,first_name,last_name,group_id) values (1,'Roman','Ivanov',1);
insert into Student(id,first_name,last_name,group_id) values (2,'Aleksey','Kuznetsov',1);
insert into Student(id,first_name,last_name,group_id) values (3,'Olga','Naumova',1);

insert into Student(id,first_name,last_name,group_id) values (4,'Irina','Filippenko',2);
insert into Student(id,first_name,last_name,group_id) values (5,'Alexandr','Galkin',2);
insert into Student(id,first_name,last_name,group_id) values (6,'Petr','Kutepov',2);

insert into Student(id,first_name,last_name,group_id) values (7,'Sergey','Ivaschenko',3);
insert into Student(id,first_name,last_name,group_id) values (8,'Oleg','Alekseev',3);
insert into Student(id,first_name,last_name,group_id) values (9,'Vladimir','Kupriyanov',3);
insert into Student(id,first_name,last_name,group_id) values (10,'Evgeniya','Nesmelova',3);

insert into Staff(id,first_name,last_name) values (1,'Semen','Vasilenko');
insert into Staff(id,first_name,last_name) values (2,'Nadezhda','Gavrilova');
insert into Staff(id,first_name,last_name) values (3,'Igor','Makarov');

insert into HR_record(staff_id,faculty_id,position) values (1,1,'professor');
insert into HR_record(staff_id,faculty_id,position) values (2,2,'professor');
insert into HR_record(staff_id,faculty_id,position) values (3,2,'docent');

insert into Exam(id,discipline,staff_id) values (1,'History of Arts',1);
insert into Exam(id,discipline,staff_id) values (2,'Programming',2);
insert into Exam(id,discipline,staff_id) values (3,'Math',3);

insert into Exam_record(student_id,exam_id,grade,date) values(1,1,4,'2020-01-15');
insert into Exam_record(student_id,exam_id,grade,date) values(2,1,5,'2020-01-15');
insert into Exam_record(student_id,exam_id,grade,date) values(4,2,3,'2020-01-10');
insert into Exam_record(student_id,exam_id,grade,date) values(5,2,4,'2020-01-10');
insert into Exam_record(student_id,exam_id,grade,date) values(6,2,3,'2020-01-10');
insert into Exam_record(student_id,exam_id,grade,date) values(6,3,5,'2020-01-05');
insert into Exam_record(student_id,exam_id,grade,date) values(8,3,5,'2020-01-05');
insert into Exam_record(student_id,exam_id,grade,date) values(9,3,4,'2020-01-05');
insert into Exam_record(student_id,exam_id,grade,date) values(10,2,4,'2020-01-10');
insert into Exam_record(student_id,exam_id,grade,date) values(10,3,5,'2020-01-05');

--КОНЕЦ СКРИПТА------------------------------------------------------------

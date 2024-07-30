INSERT INTO students(name, second_name, group_id) values('Mateo', 'Legend', 1514);
SELECT * from `groups`  ;
INSERT INTO `groups` (title, start_date, end_date) values ('QAauto', 'may 2024', 'oct 2024' );
select * from students;
insert INTO books (title, taken_by_student_id) VALUES ('Gore ot uma', 1595);
INSERT INTO books (title, taken_by_student_id) VALUES ('Neuromarketing', 1595);
INSERT INTO books (title, taken_by_student_id) VALUES ('Study for QA', 1595);
INSERT INTO subjets (title) VALUES ('Geografia');
INSERT INTO subjets (title) VALUES ('Math');
INSERT INTO lessons (title, subject_id) VALUES ('firs_lesson',2045);
INSERT INTO lessons (title, subject_id) VALUES ('second_lesson', 2045);
INSERT INTO lessons (title, subject_id) VALUES ('trith_lesson', 2046);
INSERT INTO lessons (title, subject_id) VALUES ('five_lesson',2046);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 4579, 1595);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('3', 4579, 1595);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('4', 4578, 1595);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('2', 4578, 1595);
SELECT * FROM marks WHERE student_id = 1595; 
SELECT * FROM books WHERE taken_by_student_id = 1595;
SELECT * FROM students
JOIN books on students.id = books.taken_by_student_id 
JOIN marks on students.id = marks.student_id
JOIN `groups` on students.group_id = `groups`.id
JOIN lessons on marks.lesson_id = lessons.id
JOIN subjets on lessons.subject_id = subjets.id 
WHERE students.id = 1595;
SELECT lesson_id FROM marks WHERE student_id = 1595;

select * from students order by id desc limit 5;
SELECT id from books ORDER BY id DESC LIMIT 1 OFFSET 2;
SELECT * FROM marks order by id desc;
SELECT * FROM marks WHERE student_id = 1640;
select * from books;
select * from students  order by id desc limit 5;
Update students SET group_id = 1580 where id = 1645;
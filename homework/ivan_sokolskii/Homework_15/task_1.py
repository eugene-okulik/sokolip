import mysql.connector as mysql
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)
create_student = '''
INSERT INTO students(name, second_name)
VALUES (%s, %s)
'''
cursor.execute(create_student, ('Matte', 'Manatee'))
last_student_id = cursor.lastrowid
print('идентификатор студента: ', last_student_id)
create_groups = '''
INSERT INTO `groups` (title, start_date, end_date)
VALUES (%s, %s, %s)
'''
cursor.execute(create_groups, ('QAgroup353', 'may 2024', 'oct 2024'))
last_id_group = cursor.lastrowid
print('идентификатор группы: ', last_id_group)
add_student_in_group = f'''
UPDATE students
SET group_id = {last_id_group}
WHERE id = {last_student_id}
'''
cursor.execute(add_student_in_group)
create_books_query = '''
INSERT INTO books (title, taken_by_student_id)
VALUES (%s, %s);
'''
cursor.executemany(
    create_books_query, [
        ('Python for everyone', last_student_id),
        ('Bratiay Karamazovy', last_student_id),
        ('Curse of yoga', last_student_id)
    ]
)
curse_of_yoga_id = cursor.lastrowid
bratiay_karamazovy_id_query = cursor.execute("SELECT id from books ORDER BY id DESC LIMIT 1 OFFSET 1")
bratiay_karamazovy_id_value = cursor.fetchone()
bratiay_karamazovy_id = bratiay_karamazovy_id_value['id']
python_for_everyone_id_query = cursor.execute("SELECT id from books ORDER BY id DESC LIMIT 1 OFFSET 2")
python_for_everyone_id_value = cursor.fetchone()
python_for_everyone_id = python_for_everyone_id_value['id']
print('ID book_1: ', curse_of_yoga_id)
print('ID book_2: ', bratiay_karamazovy_id)
print('ID book_3: ', python_for_everyone_id)
create_subjets_query = "INSERT INTO subjets(title) VALUES(%s)"
cursor.execute(create_subjets_query, ('Fizra',))
fizra_subjets_id = cursor.lastrowid
print('ID fizra', fizra_subjets_id)
cursor.execute(create_subjets_query, ('OBJ',))
obj_subjet_id = cursor.lastrowid
print('ID OBJ: ', obj_subjet_id)
create_lessons_query = "INSERT INTO lessons(title, subject_id) VALUES (%s, %s)"
cursor.execute(create_lessons_query, ('first_less_bio', obj_subjet_id))
first_less_fis_id = cursor.lastrowid
print('ID first lesson: ', first_less_fis_id)
cursor.execute(create_lessons_query, ('second_less_math', fizra_subjets_id))
second_less_math_id = cursor.lastrowid
print('ID second lesson: ', second_less_math_id)
cursor.execute(create_lessons_query, ('trith_less_wor', obj_subjet_id))
trith_less_wor_id = cursor.lastrowid
print('ID Trith lesson: ', trith_less_wor_id)
cursor.execute(create_lessons_query, ('five_less_fis', fizra_subjets_id))
five_less_fis_id = cursor.lastrowid
print('ID five lesson: ', five_less_fis_id)
marks_lesson_by_id = f"SELECT lesson_id FROM marks WHERE student_id = {last_student_id}"
create_marks_query = '''
INSERT INTO marks (value, lesson_id, student_id)
VALUES (%s, %s, %s)
'''
cursor.executemany(
    create_marks_query, [
        ('5', five_less_fis_id, last_student_id),
        ('3', trith_less_wor_id, last_student_id),
        ('2', second_less_math_id, last_student_id),
        ('4', first_less_fis_id, last_student_id)
    ]
)
db.commit()
marks_by_student_id_query = f"SELECT * FROM marks WHERE student_id = {last_student_id}"
cursor.execute(marks_by_student_id_query)
marks_by_student_id_value = cursor.fetchall()
print('Оценки студента: ', marks_by_student_id_value)
taken_book_by_student_id_query = f"SELECT * FROM books WHERE taken_by_student_id = {last_student_id}"
cursor.execute(taken_book_by_student_id_query)
taken_book_by_student_id = cursor.fetchall()
print('Книги взятые студентом ', taken_book_by_student_id)
students_group_id_query = f"SELECT group_id from students WHERE id = {last_student_id}"
cursor.execute(students_group_id_query)
students_group_id = cursor.fetchall()
print('ид групп студента: ', students_group_id)
all_info_by_student_id_query = f'''
SELECT *
FROM students
JOIN books on students.id = books.taken_by_student_id
JOIN marks on students.id = marks.student_id
JOIN `groups` on students.group_id = `groups`.id
JOIN lessons on marks.lesson_id = lessons.id
JOIN subjets on lessons.subject_id = subjets.id
WHERE students.id = {last_student_id}
'''
all_info_by_student_id = cursor.execute(all_info_by_student_id_query)
all_information = cursor.fetchone()
print('All infomation about student: ', all_information)
db.close()

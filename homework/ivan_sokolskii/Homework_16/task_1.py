import os
import mysql.connector as mysql
import dotenv
import csv
import collections

dotenv.load_dotenv()
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor(dictionary=True)
query_student_name = '''
SELECT name, second_name, groups.title as group_title, books.title as book_title,
subjets.title as subject_title, lessons.title as lesson_title, marks.value as mark_value
FROM students
JOIN books on students.id = books.taken_by_student_id 
JOIN marks on students.id = marks.student_id
JOIN `groups` on students.group_id = `groups`.id
JOIN lessons on marks.lesson_id = lessons.id
JOIN subjets on lessons.subject_id = subjets.id
'''
cursor.execute(query_student_name)
student_data = cursor.fetchall()
# print(student_data)
# names_in_db = []
# second_name_in_db = []
# group_id_in_db = []
# for i in student_data:
#     names_in_db.append(i['name'])
#     second_name_in_db.append(i['second_name'])
#     group_id_in_db.append(i['group_id'])
# # print(names_in_db)
# # print(second_name_in_db)
# # print(group_id_in_db)
current_directory = os.getcwd()
file_path = os.path.abspath(os.path.join(current_directory, '../..', 'eugene_okulik/Lesson_16/hw_data', 'data.csv'))
# data_file = collections.defaultdict(list)


def read_csv_file(file_path):
    with open(file_path, newline='') as csv_file:
        data = csv.DictReader(csv_file)
        return[row for row in data]
    # for row in data:
    #     print(row)
    #     for key, value in row.items():
    #         data_file[key].append(value)


csv_dict_list = read_csv_file(file_path)


def dict_to_tuple(d):
    return tuple(sorted(d.items()))


db_tuples = set(dict_to_tuple(row) for row in student_data)
file_tuple = set(dict_to_tuple(row) for row in csv_dict_list)


def find_diffenes_rows(file_tuples, db_tuples):
    return file_tuples - db_tuples


missing_rows = find_diffenes_rows(file_tuple, db_tuples)
print('Строки из csv файла, которых нет в базе данных: ')
for row in missing_rows:
    print(dict(row))
# # names_in_file = data_file['name']
# second_name_in_file = data_file['second_name']
# group_title_in_file = data_file['group_title']
# print(names_in_file)
# print(second_name_in_file)
# print(group_title_in_file)
# diff_name = list(set(names_in_file) - set(names_in_db))
# print(diff_name)
# for line in student_data:
#     for line1 in data_file:
#         if line != line1:
#             print(line1)
db.close()

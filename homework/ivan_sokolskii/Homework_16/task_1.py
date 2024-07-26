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
query_student_name = 'SELECT * FROM students'
cursor.execute(query_student_name)
student_data = cursor.fetchall()
print(student_data)
names_in_db = []
second_name_in_db = []
group_id_in_db = []
for i in student_data:
    names_in_db.append(i['name'])
    second_name_in_db.append(i['second_name'])
    group_id_in_db.append(i['group_id'])
print(names_in_db)
print(second_name_in_db)
print(group_id_in_db)

current_directory = os.getcwd()
file_path = os.path.abspath(os.path.join(current_directory, '../..', 'eugene_okulik/Lesson_16/hw_data', 'data.csv'))
data_file = collections.defaultdict(list)
with open(file_path, newline='') as csv_file:
    data = csv.DictReader(csv_file)
    for row in data:
        print(row)
        for key, value in row.items():
            data_file[key].append(value)
data_file = dict(data_file)
print(data_file)
# names_in_file = data_file['name']
# second_name_in_file = data_file['second_name']
# group_title_in_file = data_file['group_title']
#
# print(names_in_file)
# print(second_name_in_file)
# print(group_title_in_file)
#
# diff_name = list(set(names_in_file) - set(names_in_db))
# print(diff_name)



# for line in data_file:
#






db.close()
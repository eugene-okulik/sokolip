# Task 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
# Task 2
result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'
index_1 = result_1.index(":") + 2
num_1 = int(result_1[index_1:])
print(num_1 + 10)
index_2 = result_2.index(":") + 2
num_2 = int(result_2[index_2:])
print(num_2 + 10)
index_3 = result_3.index(":") + 2
num_3 = int(result_3[index_3:])
print(num_3 + 10)
# result_number_1 = int(result_1.split(":")[-1].strip())
# result_number_2 = int(result_2.split(":")[-1].strip())
# result_number_3 = int(result_3.split(":")[-1].strip())
# print(result_number_1 + 10)
# print(result_number_2 + 10)
# print(result_number_3 + 10)
# Task 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
student_1, student_2, student_3 = students
subject_1, subject_2, subject_3 = subjects
print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
# output_text = 'Students {0}, {1}, {2} study these subjects: {3}, {4}, {5}'
# print(output_text.format((student_1), (student_2), (student_3), (subject_1), (subject_2), (subject_3)))

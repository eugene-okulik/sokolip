# Task 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
# Task 2
result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'
result_number_1 = int(result_1.split(":")[-1].strip())
result_number_2 = int(result_2.split(":")[-1].strip())
result_number_3 = int(result_3.split(":")[-1].strip())
print(result_number_1 + 10)
print(result_number_2 + 10)
print(result_number_3 + 10)
# Task 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
student_1, student_2, student_3 = students
subject_1, subject_2, subject_3 = subjects
print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
# output_text = 'Students {0}, {1}, {2} study these subjects: {3}, {4}, {5}'
# print(output_text.format((student_1), (student_2), (student_3), (subject_1), (subject_2), (subject_3)))

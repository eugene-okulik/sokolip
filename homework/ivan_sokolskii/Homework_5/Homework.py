# Task 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
# Task 2
result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'
num_1 = int(result_1[19:22])
num_1 += 10
num_2 = int(result_2[19:23])
num_2 += 10
num_3 = int(result_3[-1])
num_3 += 10
print(num_1, num_2, num_3)
# Task 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
student_1, student_2, student_3 = students
subject_1, subject_2, subject_3 = subjects
output_text = 'Students {0}, {1}, {2} study these subjects: {3}, {4}, {5}'
print(output_text.format((student_1), (student_2), (student_3), (subject_1), (subject_2), (subject_3)))

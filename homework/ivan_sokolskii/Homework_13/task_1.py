import os
from datetime import datetime
current_directory = os.getcwd()
file_path = os.path.abspath(os.path.join(current_directory, '../..', 'eugene_okulik/hw_13', 'data.txt'))

def read_file():
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    with open('data2.txt', 'a') as new_file:
        for line in
        data_line = data_line.split(' - ')
        new_file.write(data_line)

















# first_part = data_line[0]
# print(first_part)
# date_1= first_part[3:22]
#
# print(date_1)
# date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")






#
#
# for data_line in read_file():
#     with open('data2.txt', 'a') as new_file:



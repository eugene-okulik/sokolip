import os
import datetime
current_directory = os.getcwd()
file_path = os.path.abspath(os.path.join(current_directory, '../..', 'eugene_okulik/hw_13', 'data.txt'))
with open(file_path, 'r') as data_file:
    lines = data_file.readlines()

for line in lines:
    parts = line.strip().split(' - ')
    if len(parts) == 2:
        date_str, action = parts
        date_str = ' '.join(date_str.split(' ')[1:])
        date_format = "%Y-%m-%d %H:%M:%S.%f"
        date = datetime.datetime.strptime(date_str, date_format)
        action = parts[1]
        if 'распечатать эту датуб но на неделю позже' in action:
            new_date = date + datetime.timedelta(weeks=1)
            print(new_date.strptime(date_format))
        elif 'распечатать какой это будет день недели' in action:
            day_of_week = date.weekday()
            days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
            print(days[day_of_week])
        elif 'сколько дней назад была эта дата':
            today = datetime.datetime.now()
            diff = (today - date).days
            print(diff)

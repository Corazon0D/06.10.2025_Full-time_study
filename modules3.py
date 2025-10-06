# использум random() (от 0,000000...1 до 0,9999999999...)

# from random import random, randint
#
# result = []
#
# for i in range(6):
#     temp = random() + randint(0, 6)
#     # result.append(round(temp, 1)) # Либо так
#     result.append(f'{temp:.1f}')  # Либо так
# print(*result, sep=', ')

import datetime as dt

# Получениея текущих даты и времени из определённой системы
print(dt.datetime.now()) # выводит дату и время
print(dt.datetime.now().date()) # вычленяем только дату
print(dt.datetime.now().time()) # вычленяем только время

# Для вывода строки из формата времени используем
raw_time = dt.datetime.now() # В формате datetime
date_as_string = raw_time.strftime('Сегодня: %d.%m.%Y') # По-человечески день месяц год
time_as_string = raw_time.strftime('А время: %H : %M: %S')
print(date_as_string)
print(time_as_string)

# Создание объекта с датой
new_date = dt.date(2021, 11, 27)
d_t = new_date.strftime('%d.%m.%Y')
print(type(new_date))
print(d_t)
print(type(d_t))

# Создание объекта с временим
new_time = dt.time(11, 30, 15)
print(new_time)
print(type(new_time))

new_date_1 = dt.date(1941, 6, 22)

new_date_2 = dt.date(1945, 5, 9)

result = new_date_2 - new_date_1
print(result.days)
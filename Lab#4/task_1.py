# Задание 1:  Импорт стандартных модулей

# 1.	Импортируйте модуль math и используйте функцию sqrt() для вычисления квадратного корня.
# 2.	Используйте модуль datetime для отображения текущей даты и времени.


from math import sqrt
from datetime import datetime

current_date_and_time = datetime.now()

number = 25
num_sqrt = sqrt(number)

print(current_date_and_time)
print()
print(num_sqrt)



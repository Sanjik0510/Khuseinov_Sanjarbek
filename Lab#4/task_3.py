# Задание 3: Создание и использование пакетов

# 1.	Создайте пакет, содержащий несколько модулей. Каждый модуль должен выполнять определённую задачу (например, операции с числами, работа со строками и т.д.).
# 2.	Продемонстрируйте, как импортировать различные модули из вашего пакета в другой файл Python.


from my_package.multiply import *
from my_package.strings import *
from my_package.Users import user_input

print(multiply(1,2,3,4), sm(1,2,3,4)); print()

print(integer('2135!'))
print()
print(integer('13523')), print()

user_input('...')
print(open('users_input.txt', 'r', encoding = 'utf-8').read())


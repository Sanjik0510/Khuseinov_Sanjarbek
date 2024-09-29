# Задание 1:  Открытие и чтение файла

# 1.	Создайте текстовый файл example.txt и заполните его несколькими строками текста.
# 2.	Напишите функцию на Python, которая открывает файл example.txt в режиме чтения и выводит его содержимое на экран.
# 3.	Используйте разные методы чтения файла: чтение всего файла сразу, построчное чтение, реализуйте выбор типа чтения в принимаемых аргументах функции.

def open_files(name, read='r', encoding='utf-8'):
    with open(name, 'r', encoding = encoding) as file:
        if read == 'r': 
            return file.read()
        if read == 'rls':
            return list(line.strip() for line in file)
        
    
example = open_files('Lab#3\example.txt')
example_2 = open_files('Lab#3\example.txt', 'rls')

print(example)
print()
print(example_2)



# Задание 2:  Запись в файл

# 1.	Напишите программу, которая запрашивает у пользователя текст и записывает его в новый файл user_input.txt.
# 2.	Реализуйте функционал добавления текста в существующий файл, не удаляя его предыдущее содержимое.

def user_input(text):
    with open(r'Lab#3\user_input.txt', 'w', encoding = 'utf-8') as file:
        file.write(text)
    
    
user = user_input(input("Введите текст: "))
print()
print(open(r'Lab#3\user_input.txt', 'r', encoding = 'utf-8').read())




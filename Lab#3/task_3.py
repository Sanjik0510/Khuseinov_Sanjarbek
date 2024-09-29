# Задание 3:  Запись в файл

# 1.	Модифицируйте программу из Задания 1 так, чтобы она корректно обрабатывала исключение, возникающее при попытке открыть несуществующий файл.
# Вместо вывода ошибки программа должна выводить пользователю понятное сообщение.

# 	Используйте в блоке try except следующий класс исключений: FileNotFoundError.

def open_files(name, read='r', encoding='utf-8'):
    try:
        with open(name, 'r', encoding = encoding) as file:
            if read == 'r': 
                return file.read()
            if read == 'rls':
                return list(line.strip() for line in file)
    except FileNotFoundError:
        print("Файл не найден")
            
            
open_files('asdlfkh')



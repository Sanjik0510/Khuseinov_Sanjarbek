# Задание 3: Использование функций для решения алгоритмических задач

# Напишите функцию is_prime, которая определяет, является ли число простым, и возвращает True или False соответственно.
def is_prime(number):
    return not any(number%i==0 for i in range(2,int(number**0.5) + 1))

print(is_prime(29))
print(is_prime(38))
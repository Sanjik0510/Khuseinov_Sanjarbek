def greet(name):
    print('Привет,', name)
    
def square(number):
    return number**2

def max_of_two(x, y):
     return max(x, y)

def describe_person(name, age=30):
    print(f'Имя: {name}', f'Возраст: {age}', sep='\n')
    
def is_prime(number):
    return not any(number%i==0 for i in range(2,int(number**0.5) + 1))


greet('Санжарбек')

print(square(5))

print(max_of_two(27, 8))

describe_person("Sanjarbek", 18)

print(is_prime(21354579137))
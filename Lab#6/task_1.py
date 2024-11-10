# 1.	Создайте класс UserAccount, который представляет аккаунт пользователя с атрибутами: имя пользователя (username), электронная почта (email) и приватный атрибут пароль (password).
# 2.	Используйте конструктор __init__ для инициализации этих атрибутов.
# 3.	Реализуйте метод set_password(new_password), который позволяет безопасно изменить пароль аккаунта.
# 4.	Реализуйте метод check_password(password), который проверяет, соответствует ли введённый пароль текущему паролю аккаунта и возвращает True или False.
# 5.	Создайте объект класса UserAccount, попробуйте изменить пароль и проверить его с помощью методов set_password и check_password.

class UserAccount:
    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.__password = password
        
    def set_password(self, new_password):
        self.__password = new_password
        
    def check_password(self, password):
        check = self.__password == password
        return check
    
    
user = UserAccount("anonymous", "anonymous0001@laptop.net", "a0n1o2n3y4m5o6u7s!")

# print(user.__password) #AttributeError: 'UserAccount' object has no attribute '__password'

user.set_password('01234567!')

check_password_0 = user.check_password('a0n1o2n3y4m5o6u7s!')
check_password_1 = user.check_password('01234567!')

print(check_password_0, check_password_1, sep='\n')



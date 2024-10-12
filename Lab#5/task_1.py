# 1.	Определите класс Book, который имеет три атрибута: title (название), author (автор), и year (год издания).
# 2.	Добавьте метод get_info(), который возвращает информацию о книге в формате: "Название книги: [title], Автор: [author], Год издания: [year]".

class Book:
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def get_info(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}'
    
    
first_book = Book("Преступление и наказание","Фёдор Михайлович Достоевский", "1865")

second_book = Book("Маленький принц", "Антуан де Сент-Экзюпери", "1943")

print(first_book.get_info())
print()
print(second_book.get_info())
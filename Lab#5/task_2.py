# 1.	Определите класс Circle для представления круга.
# 2.	Используйте конструктор __init__ для инициализации радиуса круга (radius).
# 3.	Добавьте метод get_radius(), который возвращает значение радиуса.
# 4.	Добавьте метод set_radius(new_radius), который позволяет изменить радиус круга.
# 5.	Создайте объект класса Circle, измените его радиус и выведите новый радиус на экран

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def get_radius(self):
        return self.radius
        
    def set_radius(self, new_radius):
        self.radius = new_radius
            

object = Circle(10)
print(object.get_radius())

object.set_radius(5)
print(object.get_radius())




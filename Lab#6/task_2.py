# 1.	Определите базовый класс Vehicle с атрибутами: make (марка) и model (модель), а также методом get_info(), который возвращает информацию о транспортном средстве.
# 2.	Создайте класс Car, наследующий от Vehicle, и добавьте в него атрибут fuel_type (тип топлива). Переопределите метод get_info() таким образом, чтобы он включал информацию о типе топлива.

class Vehicle:
    def __init__(self, mark, model) -> None:
        self.mark = mark
        self.model = model
        
    def get_info(self):
        vehicle_info = {"mark": self.mark, "model": self.model}
        return vehicle_info
        
    
class Car(Vehicle):
    def __init__(self, mark, model, fuel_type) -> None:
        super().__init__(mark, model)
        self.fuel_type = fuel_type
        
    def get_info(self):
        vehicle_info = Vehicle.get_info(self) | {"fuel_type": self.fuel_type}
        return vehicle_info
    
car = Car("Changan",'Uni-V','petrol')

car_info = car.get_info()

print(car_info)


class Employee:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        
    def get_info(self):
        return {'Name': self.name, 'ID': self.id}
    

class Manager(Employee):
    def __init__(self, name, id, department) -> None:
        super().__init__(name, id)
        self.department = department 
        
    def manage_project(self):
        return "управление проектами"
    
    def get_info(self):
        return super().get_info() | {'Department': self.department}
    

class Technician(Employee):
    def __init__(self, name, id, spacialization) -> None:
        super().__init__(name, id)
        self.spacialization = spacialization
        
    def perform_maintenance(self):
        return "выполнение технического обслуживания"
    
    def get_info(self):
        return super().get_info() | {"Spacialization": self.spacialization}
    

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, spacialization) -> None:
        self.name = name
        self.id = id
        self.department = department
        self.spacialization = spacialization
        self.subordinates = []
        
    def add_employer(self, *coworkers):
        self.subordinates.extend(coworkers)
        
    def get_team_info(self):
        info = list()
        team = self.subordinates
        
        for i in range(len(team)):
            info.append(team[i].get_info())
        
        return info

emp0 = Employee('Name_0', '5234' )
emp1 = Manager("Name_1", 1, 'deparment_1')
emp2 = Technician('Name_2', 2, 'Technician')
emp3 = TechManager('Name_3', 3, 'deparment_3', 'TechManager')

emp3.add_employer(emp0, emp1, emp2)

print(emp0.get_info(), emp1.get_info(), emp2.get_info(), emp3.get_info(), emp3.get_team_info(), sep='\n')
 
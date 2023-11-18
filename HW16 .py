"""class Vehicle():
    def __init__ (self,model,year):
        self.model=model
        self.year=year

class Car(Vehicle):
    def __init__(self, model, year,fuel_type):
        super().__init__(model, year)
        self.fuel_type=fuel_type
    
    def info (self):
        return f'Модель - {self.model}\nГод выпуска - {self.year}\nТип топлива - {self.fuel_type}\n'
    
car1=Car('L200',2022,'Бензин')
car2=Car('QX60',2022,'Бензин')

print(car1.info())
print(car2.info())"""

#2
'''from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def living_creatures(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird (Animal,Flyable):
    def __init__(self,name):
        self.name=name

    def living_creatures(self):
        return f'{self.name} является живым существом'
    
    def fly(self):
        return f'{self.name} умеет летать'
    
bird1=Bird('Канарейка')
bird2=Bird('Попугай')
print(bird1.living_creatures())
print(bird1.fly())
print(bird2.living_creatures())
print(bird2.fly())'''

#3
class Vehicle():
    def __init__ (self,model,year):
        self.model=model
        self.year=year

class Car(Vehicle):
    def __init__(self, model, year,fuel_type):
        super().__init__(model, year)
        self.fuel_type=fuel_type
    
    def info (self):
        return f'Модель - {self.model}\nГод выпуска - {self.year}\nТип топлива - {self.fuel_type}\n'
    
class Toyota(Car):
    def __init__(self, model, year, fuel_type,model_name,fuel_consumption):
        super().__init__(model, year, fuel_type)
        self.model_name=model_name
        self.fuel_efficiency=fuel_consumption
    
    def info(self):
        return f'{self.model} от Тойоты, модель: {self.model_name}, была выпущена в {self.year}\n В качестве топлива использует {self.fuel_type},\nРасход топлива на 100км - {self.fuel_efficiency} '

class Ford(Car):
    def __init__(self, model, year, fuel_type,model_name,fuel_consumption):
        super().__init__(model, year, fuel_type)
        self.model_name=model_name
        self.fuel_efficiency=fuel_consumption
    
    def info(self):
        return f'{self.model} от компании Форд, модель: {self.model_name}, была выпущена в {self.year}\n В качестве топлива использует {self.fuel_type},\nРасход топлива на 100км - {self.fuel_efficiency} '

class Tesla(Car):
    def __init__(self, model, year, fuel_type,model_name,fuel_consumption):
        super().__init__(model, year, fuel_type)
        self.model_name=model_name
        self.fuel_efficiency=fuel_consumption
    
    def info(self):
        return f'{self.model} от Tesla, модель: {self.model_name}, была выпущена в {self.year}\n В качестве топлива использует {self.fuel_type},\nРасход топлива на 1000км - {self.fuel_efficiency} '

car1=Toyota('Кросовер',2020, 'бензин', 'Yaris Cross',5)
car2=Ford('Пикап',2012,"дизель","Ranger",8)
car3=Tesla('Седан',2017,"электричество",'Roadster','1 полная зарядка')

print(car1.info())
print(car2.info())
print(car3.info())
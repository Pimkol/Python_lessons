#Практическое задание
#1
'''class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def description(self):
        print (f'Автомобиль марки: {self.brand} \nМодель: {self.model} \nГод выпуска: {self.year}\n')

car1= Car ('Mazda', 'CX-4', 2022)
car2= Car ('Mitsubishi','ASX',2022)
    
car1.description()
car2.description()'''


#2
'''class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary=salary
    
    def get_info(self):
        print (f'{self.name} \nВозраст:{self.age} \nЗаработная плата:{self.salary}\n')

per1=Employee('Иванов И.И.',35,150000)
per2=Employee('Смирнов С.С.',27,125000)
per3=Employee('Фролов Ф.Ф.', 42,147000)

per1.get_info()
per2.get_info()
per3.get_info()'''


#3
'''class Animal:
    def __init__(self) -> None:
        pass

    def speak(self):
        print('')

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()
    
    def speak(self):
        print('Мяу')
    
class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()

    def speak(self):
        print('Гав')

cat=Cat()
cat.speak()
dog=Dog()
dog.speak()'''

#4
class BankAccount:
    def __init__(self,balance,account_number):
        self.balance=balance
        self.account_number=account_number

    def info(self):
        return f'Номер счета: {self.account_number} \nТекущий баланс: {self.balance}'
    
    def deposit(self):
        sum=int(input('Введите  сумму для внесения на счет:'))
        self.balance+=sum
        return f' Текущий баланс: {self.balance}'
    
    def withdraw(self):
        dif=int(input('Введите сумму для снятия со счета:'))
        self.balance-=dif
        return f' Текущий баланс: {self.balance}'
    
class SavingAccount(BankAccount):
    def __init__(self, balance, account_number,interest_rate):
        super().__init__(balance, account_number)
        self.interest_rate=interest_rate

    def info(self):
        return f'Номер счета: {self.account_number} \nТекущий баланс: {self.balance}'
        
    def add_interest(self):
        rate=(self.balance*self.interest_rate)/100
        self.balance+=rate
        return f'Сумма вознаграждения по вкладу:{rate} (ГЭСВ {self.interest_rate}%)\nТекущий баланс: {self.balance}'

num1=BankAccount(250500,'KZ341412515143') #расчетный счет
num2=SavingAccount(135687,'KZ876532654334',3) #депозитный счет

choi=int(input('Для выбора операций по расчетному счету введите 1, для депозитного счета: 2'))
if choi==1:
    print(num1.info())
    choi2=int(input('Для пополнения баланса введите 1, для снятия средств: 2'))
    if choi2==1:
        print(num1.deposit())
    else:
        print(num1.withdraw())
else:
    print(num2.info())
    print(num2.add_interest())

    
    






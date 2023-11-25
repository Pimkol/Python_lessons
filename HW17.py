#1
from abc import ABC, abstractmethod
'''class AbcArg(ABC):
    @abstractmethod
    def sum (self):
        pass
    @abstractmethod
    def sub(self):
        pass
    def div(self):
        pass
    def mul(self):
        pass

class Num(AbcArg):
    def __init__(self,first_arg, second_arg):
        self.first_arg=first_arg
        self.second_arg=second_arg
    def sum(self):
        return self.first_arg+self.second_arg
    def sub(self):
        return self.first_arg-self.second_arg
    def div(self):
        return self.first_arg/self.second_arg
    def mul(self):
        return self.first_arg*self.second_arg

#rez=[Num('первый аргумент',"второй аргумент"), Num(16,3), Num(15.3,2.2)]  #не поняла ка ерализовать для строк
rez=[Num(16,3), Num(15.3,2.2)] 
for r in rez:
    print(f'результат сложения: {r.sum()}')
    print(f'результат вычитания: {r.sub()}')
    print(f'результат деления: {r.div()}')
    print(f'результат умножения: {r.mul()}')'''

#2
'''class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2
    
class Rectangle (Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def area(self):
        return self.width*self.height
    
class Triangle(Shape):
    def __init__(self,height,side):
        self.height=height
        self.side=side
    def area(self):
        return (self.height*self.side)/2
    
shapes=[Circle(7),Rectangle(4,8),Triangle(5,7)]
for shape in shapes:
    print(f'Площадь:{shape.area()}')  '''

#3
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def draw(self):
        print('Нарисован круг')

class Rectangle(Drawable):
    def draw(self):
        print('Нарисован прямоугольник')

shapes=[Circle(),Rectangle()]
for shape in shapes:
    shape.draw()
  


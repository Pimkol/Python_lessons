#1
'''def divade(x,y):
    if y==0:
        raise ZeroDivisionError ('Вычисление невозможно - на ноль делить нельзя')
    return x/y

x=int(input('Введите делимое: '))
y=int(input('Введите делитель: '))
try:
    rez=divade(x,y)
except ZeroDivisionError:
    print (f'Ошибка: {ZeroDivisionError}')'''

#2
'''class ValidationError(Exception):
    def __init__(self, message,code):
        super().__init__(message)
        self.code=code

def wrong(name):
    try:
        for i in range(len(name)):
            if name[i]=='#' or name[i]=='a' or name[i]=='!':
                raise ValidationError('Некорректный символ ',name[i])
    except ValidationError as e:
        print(f'Ошибка! В Имени не может использоваться символ - {e.code}')

    
name=input('Введите имя пользователя:')
wrong(name)'''

#3
'''import time

class Timer:
    def __enter__(self):
        self.start_time=time.time()
        return self
    
    def __exit__(self,*args):
        self.end_time=time.time()
        elapsed_time=self.end_time-self.start_time
        print (f'Время выполнения:{elapsed_time} сек')

with Timer():
    print('Привет')
    time.sleep(2)
    z=int(input('Введите число: '))
    for i in range(z):
        print('Как дела?')
        time.sleep(1)'''


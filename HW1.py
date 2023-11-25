#Вычисление среднеарифметического значения чисел
print('среднеарифметическое значение трех чисел')
a=int(input("a=",))
b=int(input("b=",))
c=int(input("с=",))
print("среднее значение:",(a+b+c)/3)


#Имя и город
'''name='Olga'
city='Karaganda'
print(name, ' from ', city)'''


#Интервью
'''name=str(input('Как Вас зовут? ',))
soname=str(input('Ваша фамилия ',))
city=str(input('Из какого Вы города? ',))
age=int(input('Сколько Вам лет? ',))
work=str(input('Кем Вы работаете? ',))
print('Привет! Меня зовут ',name, ' ', soname,'. Мне ', age)
print('Я живу в городе ', city)
print('Сейчас я работаю ', work)'''


#Короткая история
'''name='Olga'
City='Karaganda'
age=29
hobby='I love to read, especially science fiction.'
fbooks="My favorite writer is Orson Scott Card, but I'm also a Harry Potter fan."
print("Hi! I'm ", name)
print('I live in ', City, 'all my life.')
print("I'm ", age, 'and ', hobby)
print(fbooks)'''


#Вычисление площади и длины окружности
'''import math
print('Площадь и длина окружности')
r=int(input('Радиус окрожность: R=',))
z=int(input('Укажите количество знаков после запятой:',))
c=2*math.pi*r
s=math.pi*r*r
c=round(c,z)
s=round(s,z)
print('Длина окружности:',c)
print('Площадь окружности:' ,s)'''


#Прогноз погоды
'''yes='да'
no='нет'
a=(input('Сегодня солнечно? да/нет: ',))
if a==yes:
    is_sunny=True
else:
    is_sunny=False
if is_sunny==True:
    print('Сегодня солнечно!')
else:
    print('Сегодня пасмурно')'''

#Прогноз погоды*2
'''a=(input('Сегодня солнечно? да/нет: ',))
temerature=float(input('Введите температуру воздуха:',))
if a=='да':
    is_sunny=True
else:
    is_sunny=False
if temerature > 15:
    warm=True
else:
    warm=False
good=is_sunny and warm
normal=is_sunny or warm 
bad=not is_sunny and not warm   
if good==True and normal==True:
    print('Отличная погода: Сегодня тепло и солнечно!')
if good==False and normal==True:
    print('Неплохая погода! Хорошего дня!')
else:
    print('Сегодня холодно и пасмурно. Одевайтесь теплее!')'''





#Практическое задание 
#1
'''import math

r=int(input('Введите радиус окружности:'))
print(f'Площадь круга радиусом {r} равна {math.pi*r**2:.2f}')'''

#2
'''n=int(input('Введите число:'))
d=2
while n%d!=0:
    d+=1
if d==n:
    print('Число простое')
else:
    print('Число не является простым')'''

#3
'''def h3(a,b):
    s=(a*b)/2
    return s

osn=int(input('Введите значение основания треугольника:'))
h=int(input('Введите высоту треугольника:'))
s=h3(osn,h)
print(f'Площадь треугольника с основанием {osn}  и высотой {h} равна ',s)'''

#4
'''import datetime

today=datetime.date.today()
end_date = today + datetime.timedelta(days=7)
print('Сегодня - ',today)
print('Через 7 дней будет ', end_date)'''

#5
'''import datetime

date1=input('Введите первую дату в формате ДД/ММ/ГГГГ:')
date1_d=datetime.datetime.strptime(date1, "%d/%m/%Y")
date2=input('Введите вторую дату в формате ДД/ММ/ГГГГ:')
date2_d=datetime.datetime.strptime(date2, "%d/%m/%Y")
raz=date2_d-date1_d
print(f'Разница между датами {raz.days} дней ')'''

#Практическое задание 2
#1
'''import datetime

date=input('Введите дату в формате ДД/ММ/ГГ:')
date1=datetime.datetime.strptime(date, '%d/%m/%y')
if date1.weekday()==0:
    print ('Понедельник')
elif date1.weekday()==1:
    print('Вторник')
elif date1.weekday()==2:
    print('Среда')
elif date1.weekday()==3:
    print('Четверг')
elif date1.weekday()==4:
    print('Пятница')
elif date1.weekday()==5:
    print('Суббота')
else:
    print('Воскресенье')'''

#2
'''import random

rand=random.randint(1,6)
p_num=int(input('Угадайте число, выпавшее на игральной кости:'))
if p_num==rand:
    print('На игральной кости выпало ',rand)
    print('Вы победили')
else:
    print('На игральной кости выпало ',rand)
    print('Вы проиграли')'''

#3
'''import random, string

a=int(input('количество букв  в имени:'))
r_name=str
for i in range(a):
    print(random.choice(string.ascii_letters),end='')
    #r_name+=random.choice(string.ascii_letters)
#print (r_name)'''

#4
'''import random

list=['Петя', 'Вася','Света','Лена','Ира','Миша']
winer=random.choice(list)
print('Победитель ',winer)'''

#5
'''import datetime, time

#nw=datetime.datetime.now()

for i in range(1,60):
    nw=datetime.datetime.now()
    time_nw=nw.time()
    print(time_nw.strftime("%H:%M:%S"))
    time.sleep(1)'''

#Практическое задание 3
#1  
'''import datetime,time

def am():
    a=datetime.datetime.now()
    time_am=a.time()
    print(time_am.strftime('%I:%M:%S %p'))

def h24():
    a=datetime.datetime.now()
    time24=a.time()
    print(time24.strftime('%H:%M:%S'))

z=int(input('Для выбора формата вывода времени введите 1: AP/PM, 2: 24 часа:'))
if z==1:
    print(am())
else:
    print(h24())'''

#2
#Не совсем поняла как указать для рандома выбор из дат






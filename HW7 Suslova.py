#практическое задание
'''def sum(a,b):
    rez=a+b
    return print(rez)

x=int(input('Введите первое число:'))
y=int(input('Введите второе число:'))
sum(x,y)'''

#факториал
'''def factorial(n):
    f=1
    for i in range (1, n+1):
        f*=i
    return print (f'Факториал числа {n} равен {f}')

x=int(input('Введите число:'))
factorial(x)'''

#конвертация температуры
'''def conv_C_F(c):
    f=(c*1.8)+32
    return print(f'{c} градусов по Цельсию равны {f:.2f} по Фарингейту')
    
def  conv_F_C(f):
    c=(f-32)/1.8
    return print(f'{f} градусов по Фарингейту равны {c:.2f} по Цельсию')

t=int(input('Введите температуру:'))
print('Для перевода температуры C->F введите 1 \n Для перевода F->C введите 2')
v=int(input('Ваш выбор:'))
if v==1:
    conv_C_F(t)
else:
    conv_F_C(t)'''

#НОК
'''def NOD(a,b):
    while a!=b: #алгоритм Евклида
        if a>b:
            a-=b
        else:
            b-=a
    return a

x=int(input('Введите первое число:'))
y=int(input('Введите второе число:'))
if x==y:
    z=x
else:
    z=NOD(x,y)
nok=x*y/z
print(f'Наименьшее общее кратное чисел {x} и {y} равен {nok}')'''

#ежемесячный расчет по кредиту
"""'''def ann_p(kre,mes,proc): #аннуитетный платеж, ошибка в формуле
    e_pl=kre*(proc+(proc/(1+proc)-mes-1))
    return e_pl'''
    
def dif_p(kre,mes,proc): #диференцированный платеж
    e_pl=kre/mes+kre*proc/12
    return e_pl

k=int(input('Введите сумму займа:'))
m=int(input('Введите срок займа:'))
p=int(input('Введите годовую процентную ставку:'))
#vid=int(input('Если Вас интересует аннуитетный платеж нажмите 1, иначе 2:'))
#if vid==1:
#    ep=ann_p(k,m,p)
#else:
ep=dif_p(k,m,p)
print(ep)"""

#Палиндром
'''def pal(a):
    a1=''
    l=len(a)
    for i in range (1,l+1):
        a1+=a[-i]
    return a1

x=input('Введите число:')
gx=pal(x)
if x==gx:
    print(f'Число {x} является палиндромом')
else:
    print(f'Число {x} не является палиндромом, т.к. наоборот читается как {gx}')'''



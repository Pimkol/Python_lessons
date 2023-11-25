#Практическое задание 1
#четные от 0 до 20
'''for x in range(21):
    rez=x%2
    if rez==0:
        print(x)'''


#таблица умножения
'''n=int(input('Введите число:'))
for i in range (11):
    print(f'{i}*{n}={i*n}')'''

#Практическое задание 2
#вывод по буквам
'''name=('Python')
for l in name:
    print(l)'''

#сумма нечетных чисел от 1 до 100
'''count=int(1)
x=int(0)
while count<=100:
    rez=count%2
    if rez!=0:
        x=x+count
    count+=1
print(f'Сумма нечетных числе в последовательности от 1 до 100 = {x}')'''

#Практическое задание 3
#четные в пользовательской последовательности от 0
'''n=int(input('Введите число:'))
for x in range (n+1):
    rez=x%2
    if rez==0:
        print(f'{x}')'''

#сумма чисел пользовательской последовательности
'''count=int(1)
rez=int(0)
n=int(input('Введите число:'))
while count<=n:
    rez+=count
    count+=1
print(f'Сумма чисел в последовательности от 1 до {n} равна {rez}')'''

#Практическое задание 4
#Пирамида
'''z='*'
for i in range (5):
    for j in range (1):
        print(z)
        z+='*'
'''

#таблица умножения от 1 до 5
'''for i in range (6):
    for j in range(6):
        if i!=0 and j!=0:
            print(f'{j}*{i}={j*i}')
    print('\n')'''

#Простые числа -
"""n=int(input('Введите число:'))
rez_n=int(0)
rez1=int(0)
print(f'В диапазоне от 2 до {n} имеются следующие простые числа:')
for i in range (2,n+1):
    if n%i==0:
        rez_n+=1  #проверка введенного числа
    for j in range (1,n+1):
            if i%j==0: #проверка чисел в диапазоне
                rez1+=1
    if rez1==2:
         print(i)
         rez1=0
if rez_n==2:
    print(f'Число {n} простое')
else:
    print(f'Число {n} не простое')"""

#Практическое задание *
#четные в пользовательской последовательности от 1
'''n=int(input('Введите число:'))
for x in range (1,n+1):
    rez=x%2
    if rez==0:
        print(f'{x}')'''


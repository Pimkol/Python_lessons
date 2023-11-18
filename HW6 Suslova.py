#Практическое задание 1
#оценка
'''x=int(input('Введите оценку от 1 до 10:'))
if x>=1 and x<=3:
    print('Плохо')
elif x>=4 and x<=6:
    print('Удовлетворительно')
elif x>=7 and x<=9:
    print('Хорошо')
elif x==10:
    print('Отлично')
else:
    print('Некорректная оценка')'''

#время
'''time=float(input('Введите время в формате чч.мм:'))
if time>=6 and time<=12:
    print('Доброе утро')
elif time>12 and time<=18:
    print('Добрый день')
elif time>18 and time<=24:
    print('Добрый вечер')
else:
    print('Спокойной ночи')'''

#Практическое задание 2
#Проверка деления на 3
'''x=int(input('Введите число:'))
for i in range(1,x+1):
    rez=i%3
    if rez==0:
        print (f'Число {i} делится на 3 без остатка')'''
    

#среднеарифметическое
"""count=0
num_listo=[]
num_listp=[]
x=int
sum=0
while x!=0:
    x=int(input('введите числа, для завершения введите 0:'))
    if x<0:
        num_listo.append(x)
    else:
        count+=1
        num_listp.append(x)
if num_listp[-1]==0:
    num_listp.pop()
for i in range(len(num_listp)):
    sum+=num_listp[i]
sr=sum/(count-1)
print (num_listp,num_listo)
print('Среднеарифметическое значение положительных чисел в введенной последовательности равно:', sr)"""

#Практическое задание 3
#Ёлочка
'''size=int(input('Введите ширину ёлочки:'))
vet=0
while vet!=2:
    num=(2*size)
    for i in range (0,size):
        for j in range (0,num):
            print(end=' ')
        num-=1
        for j in range (0,i+1):
            print('*',end=' ')
        print(' ')
    vet+=1'''
 

#?
'''image=[[(255,0,0),(0,255,0),(0,0,255)],
       [(0,255,255),(255,0,255),(255,255,0)]]    
for row in image:
    for pixel in row:
        print(pixel)'''

#Попытка завести шахматную доску в массив, вывод массива выводит по 1 символу в строке
'''ches=[]*8
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            ches.append('|_|')
        else:
            ches.append('|w|')
    #if i==8 and j==6:
    #    print('К')
    #print()
#print()
for i in range (0, len(ches)):
    for j in range (0, len(ches[i])):
        print(ches[i][j],end='')   
        if i==7 and j==6:
            print('К')  #попытка добавить шахматную фигуру
    print()'''

#шахматы без фигур
'''for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            print('|_|',end='')
        else:
            print('|w|',end='')
    print()'''

#сортировка
'''x=int
spis=[]
n=int(input('Введите количество чисел для сравнения:'))
for i in range(n):
    x=input('введите числа:')
    spis.append(x)
print('список несортированных чисел: \n',spis)
for i in range(n-1):
    for j in range(n-i-1):
        if spis[j] > spis[j+1]:
            spis[j], spis[j+1] = spis[j+1], spis[j]
print('числа в порядке возрастания: \n',spis)
for i in range(n-1):
    for j in range(n-i-1):
        if spis[j] < spis[j+1]:
            spis[j], spis[j+1] = spis[j+1], spis[j]
print('числа в порядке убывания: \n',spis)'''

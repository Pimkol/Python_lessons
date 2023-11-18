#Практическое задание
#01
'''num=[3,7,2]
sum=0
x=len(num)
i=1
while i < x:
    sum+=num[i]
    i+=1
print('сумма чисел:', sum)
sr=sum/x
print('Среднее значение:',sr)'''

#02
'''work=()
fio=[]
a=str
print('Далее введите данные сотрудников. для выхода введите 0')
while a!='0':
    a=input('Введите ФИО сотрудника:')
    fio.append(a)
fio.pop()
work=tuple(fio)
print(work)'''

#03
'''spis=['самолет','поезд','вертолет','ворона','шмель']
print('найдите лишнее слово в списке:',spis)
x=input('Ваш ответ:')
z=spis.count(x)
if x=='поезд':
    spis.remove(x)
    print('Все верно! поезд не летает. Теперь список слов выглядит так:', spis)
else:
    if z>0:
        spis.remove(x)
        print('ответ неверный, теперь список выглядит так:' ,spis)  
    else:      
        print('ответ неверный. такого варианта нет')'''

#04
'''frut=['банан','яблоко','аппельсин','киви','грейпфрут','слива']
print(frut)
for f in frut:
    x=len(f)
    if x<=5:
        frut.remove(f)
print('новый список',frut)'''

#05
'''stud_f=[]
a=str
i=0
j=0
print('введите данные. Для выхода введите 0')
while a!='0':
    a=input('Введите фамилию студента:')
    if a!='0':
        stud_f.append(a)
        b=input('введите оценку:')
        stud_f.append(b)
print(stud_f)'''

#05
'''st1=('Иванов','90')
st2=('Петров','83')
st3=('Сидоров','85')
stud=[st1,st2,st3]
print(stud)'''

#06, 07
'''ret=[]
kv=int
sum=0
for i in range (1,21):
    z=i%2
    if z==0:
        ret.append(i)
print(ret)
for i in range (len(ret)):
    kv=ret[i]**2
    sum+=kv
print('Сумма квадратов:',sum)'''

#08 ???
'''import random
matrix=[[],[],[]]
#z=int
for i in matrix:
    for j in range(3):
        z=random.randint(0,9)
        matrix.insert(j,z)
print(matrix,z)'''

#08 ???
'''matrix=[[1,5,8],[3,9,5],[1,4,7]]
opr=int(matrix[0][0]*matrix[1][1]*matrix[2][2]+matrix[0][1]*matrix[1][2]*matrix[2][0]+matrix[0][3]*matrix[1][0]*matrix[2][1]-matrix[0][2]*matrix[1][1]*matrix[2][0]-matrix[0][0]*matrix[1][2]*matrix[2][1]-matrix[0][1]*matrix[1][0]*matrix[2][2])
for i in matrix:
    print(matrix[i],"\n")
print(opr)'''





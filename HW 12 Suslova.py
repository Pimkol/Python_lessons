#Практическое задание
#1
'''import math_operations as m

a=int(input('Введите первое число:'))
b=int(input('Введите второе число:'))

ans=input('Укажите, какую уперацию выполнить (+,-,*,/):')
if ans=='+':
    res=m.add(a,b)
    print(f'Результат сложения {a} и {b} равен {res}')
elif ans=='-':
    if a<b:
        ans1=input(f'Число {a} < {b}. Вы действительно хотите отнять большее число от меньшего? (+/-)')
        if ans1=='+':
            res=m.sub(a,b)
            print(f'Результат {a}-{b} равен {res}')
        else:
            res=m.sub(b,a)
            print(f'Результат {b}-{a} равен {res}')
    else:
        res=m.sub(a,b)
        print(f'Результат {a}-{b} равен {res}')
elif ans=='*':
    res=m.mul(a,b)
    print(f'Результатом умножения {a} и {b} является {res}')
else:
    if a<b:
        ans1=input(f'Число {a} < {b}. Вы действительно хотите разделить меньшее число на большее? (+/-)')
        if ans1=='+':
            res=m.div(a,b)
            print(f'Результат {a}/{b} равен {res}')
        else:
            res=m.div(b,a)
            print(f'Результат {b}/{a} равен {res}')
    else:
        res=m.div(a,b)
        print(f'Результат {a}/{b} равен {res}')'''


#2
import text_operations as t_o

text=input('Введите текст:')
oper=input('Для выбора операции введите ее номер: \n 1. Подсчитать количество символов в строке; \n 2. Подсчитать количество слов в строке; \n 3. Изменить регистр строки.\n')
if oper=='1':
    res=t_o.st_len(text)
    print(f'В строке {res} символов')
elif oper=='2':
    res=t_o.word_count(text)
    print(f'В строке {res} слов')
else:
    res=t_o.change_up_down(text)
    print('Регистр изменен \n',res)






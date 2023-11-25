#Длина имени
'''name='Ольга'
print(len(name))'''

#Разделение и объединение строк
'''string='А роза упала на лапу на лапу азора'
str_split=string.split()
str_join='-'.join(str_split)
print(str_split)
print(str_join)'''

#Замена слова
'''text='А роза упала на лапу азора'
new=text.replace('а','о')
print(new)'''

#Извлечение имени пользователя из адреса
'''email=str(input('Введите Ваш Email:',))
i=email.index('@')
name=email[0:i]
print('Имя пользователя:',name)'''

#Калькулятор
v=str(input('Введите выражение:',))
if '+' in v:
    i=v.index('+')
    a1=int(v[0:i])
    b2=int(v[i:])
    rez=f"Сумма чисел {a1} и {b2} равна {a1+b2}"
elif '/' in v:
    j=v.index('/')
    a1=int(v[0:j])
    b2=int(v[j+1:])
    rez=f"Результатом деления {a1} на {b2} является {a1/b2:.2f}"
elif '-' in v:
    j=v.index('-')
    a1=int(v[0:j])
    b2=int(v[j+1:])
    rez=f"Разность чисел {a1} и {b2} равна {a1-b2}"
elif '*' in v:
    j=v.index('*')
    a1=int(v[0:j])
    b2=int(v[j+1:])
    rez=f"Результатом произведения чисел {a1} и {b2} является {a1*b2}"
print(rez)




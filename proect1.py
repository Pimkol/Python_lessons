#Календарь
import datetime

calendar=dict()
with open("text.txt", "r") as file:
    for line in file:
        print(line, end="")

def add_notes(date,event):
    calendar[date]=event
    
def search(date):
    z=0
    with open("text.txt", "r") as my_file:  #поиск в файле не работает
        for word in my_file.read().split():
            #for key,value in calendar.items():
            if word == date:
                z+=1
                print(date)
    for key,value in calendar.items():
        if key==date or z!=0:
            print (f'У Вас запланированно событие на {key}: \n{value}')
        else:
            print(f'На {date} ничего не запланированно')

''' 
def search():
    date=input('Введите дату в формате ДД/ММ/ГГГГ: ')
    z = 0
    with open("text.txt", "r") as my_file:
        for line in my_file:
            if date in line:
                z += 1
                print(line.strip())  # Выводим строку, в которой найдено совпадение
                break  # Прерываем цикл после первого совпадения
    for key, value in calendar.items():
        if key == date or z != 0:
            print(f'У Вас запланировано событие на {key}: \n{value}')
        else:
            print(f'На {date} ничего не запланировано')
'''

def del_note(date):
    for key in calendar.keys():
        if key==date:
            del calendar[key]
            print('Запись удалена')
        else:
            print('Запись для удаления не найдена')

def n_day(today,end_date):   
    for key,value in calendar.items():
        if key in range(today,end_date): # не работает, скорее всего нужна другая проверка, не могу придумать какая
            print(f'{key}:{value}\n')

with open("text.txt", "r") as file:
    for line in file:
        print(line, end="")
dat=input('Введите дату в формате ДД/ММ/ГГГГ: ')
d=datetime.datetime.strptime(dat, "%d/%m/%Y")
note=input('заметка:\n')
add_notes(dat,note)
'''
ans=int(input('Чтобы добавить еще запись введите 1; \n Для поиска введите 2; \nЧтобы удалить запись введите 3; \n Для просмотра записей введите 4;\n Для выхода из программы нажмите 5;\n'))
while ans != 5:
    if ans == 1:
        search()
        '''
        d=datetime.datetime.strptime(dat, "%d/%m/%Y")
        note=input('заметка:\n')
        add_notes(dat,note)...'''
'''


ans=int(input('Чтобы добавить еще запись введите 1; \n Для поиска введите 2; \nЧтобы удалить запись введите 3; \n Для просмотра записей введите 4;\n'))
if ans == 1:
    dat=input('Введите дату в формате ДД/ММ/ГГГГ: ')
    d=datetime.datetime.strptime(dat, "%d/%m/%Y")
    note=input('заметка:\n')
    add_notes(dat,note)

    #print(d)
elif ans==2:
    dat=input('Введите искомую дату в формате ДД/ММ/ГГГГ: ')
    d=datetime.datetime.strptime(dat, "%d/%m/%Y")
    search(d)
elif ans==3:
    dat=input('Введите искомую дату в формате ДД/ММ/ГГГГ: ')
    d=datetime.datetime.strptime(dat, "%d/%m/%Y")
    del_note(d)
else:
    count=int(input('Введите количество дней для вывода записей за период:'))
    today=datetime.date.today()
    end_date = today + datetime.timedelta(days=count)
    n_day(today,end_date)
#print(calendar)


file = open('text.txt', 'a')
for key, value in calendar.items():
  file.write(f'{key}, {value}\n')
file.close()

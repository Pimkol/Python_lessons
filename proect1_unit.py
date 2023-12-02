
def add_notes(): #Добавление записи и запись в файл
    date=input('Введите дату в формате ДД/ММ/ГГГГ: ')
    #d=datetime.datetime.strptime(dat, "%d/%m/%Y")
    note=input('Заметка:\n')
    calendar[date]=note
    
 
def search():
    date=input('Введите дату в формате ДД/ММ/ГГГГ: ')
    z = 0
    with open("text.txt", "a") as my_file:
        for line in my_file:
            if date in line:
                z += 1
                print(f'\nУ Вас запланированно событие:  {line.strip()}\n')  # Выводим строку, в которой найдено совпадение
                break  # Прерываем цикл после первого совпадения
    if z==0:
        print ('\nНичего не запланированно\n')



def del_note():  #Удаление записи не работает. Попробовала разделить каждое значение строки, чтобы создать новый словарь и перезаписать файл, но в итоге файл очищается полностью
    date=input('Введите дату в формате ДД/ММ/ГГГГ: ')
    z = 0
    with open("text.txt", "r") as my_file:
        for line in my_file:
            #key,*value = line.split(',') # Разделяем каждую строку 
            #vr[key]=value
            key = line.split(", ")
            value = line.split(", ")
            vr[key]=value

        if date == date:
            del vr[key]
            print ('Запись удалена')

    with open('text.txt', 'w') as my_file:
        for key, value in vr.items():
            my_file.write(f'{key}, {value}\n')

def n_day():  
    with open("text.txt", "r") as file: #Все имеющиеся записи
        for line in file:
            print(line, end="") 
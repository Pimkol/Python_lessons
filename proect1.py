#Календарь
import datetime
import proect1_unit as p

calendar=dict()
vr=[]
with open("text.txt", "r") as file: #Все имеющиеся записи
    for line in file:
        print(line, end="")



ans=int(input('Чтобы добавить еще запись введите 1; \n Для поиска введите 2; \nЧтобы удалить запись введите 3; \n Для просмотра записей введите 4;\n Для выхода из программы нажмите 5;\n'))
while ans != 5:
    if ans == 1:
        p.add_notes()
        ans=int(input('Чтобы добавить еще запись введите 1; \n Для поиска введите 2; \nЧтобы удалить запись введите 3; \n Для просмотра записей введите 4;\n Для выхода из программы нажмите 5;\n'))
    elif ans == 2:
        p.search()
        ans=int(input('Чтобы добавить еще запись введите 1; \n Для поиска введите 2; \nЧтобы удалить запись введите 3; \n Для просмотра записей введите 4;\n Для выхода из программы нажмите 5;\n'))
    elif ans == 3:
        p.del_note()
        ans=int(input('Чтобы добавить еще запись введите 1; \n Для поиска введите 2; \nЧтобы удалить запись введите 3; \n Для просмотра записей введите 4;\n Для выхода из программы нажмите 5;\n'))
    elif ans == 4:
        p.n_day()
        ans=int(input('Чтобы добавить еще запись введите 1; \n Для поиска введите 2; \nЧтобы удалить запись введите 3; \n Для просмотра записей введите 4;\n Для выхода из программы нажмите 5;\n'))
    elif ans == 5:
        break
    

file = open('text.txt', 'a')
for key, value in calendar.items():
    file.write(f'{key}, {value}\n')
file.close()

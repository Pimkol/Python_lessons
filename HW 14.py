#Календарь
'''import datetime

calendar=dict()

def add_notes(date,event):
    calendar[date]=event
    
def search(date):
    for key,value in calendar.items():
        if key==date:
            print (f'У Вас запланированно событие на {key}: \n{value}')
        else:
            print(f'На {date} ничего не запланированно')

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

dat=input('Введите дату в формате ДД/ММ/ГГГГ: ')
d=datetime.datetime.strptime(dat, "%d/%m/%Y")
note=input('заметка:\n')
add_notes(d,note)
ans=int(input('Чтобы добавить еще запись введите 1; \n Для поиска введите 2; \nЧтобы удалить запись введите 3; \n Для просмотра записей введите 4;\n'))
if ans == 1:
    dat=input('Введите дату в формате ДД/ММ/ГГГГ: ')
    d=datetime.datetime.strptime(dat, "%d/%m/%Y")
    note=input('заметка:\n')
    add_notes(d,note)
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
    n_day(today,end_date)'''

#Попытка со вложенными классами
'''class Calendar: 
    class DayPlan:
        def __init__(self,date,task): #,day_name,task):
            self.date=date
            #self.day_name=day_name
            self.task=task
    
        def add_plan (self):
            date1=input('Введите дату в формате ДД/ММ/ГГГГ: ')
            self.date=datetime.datetime.strptime(date1, "%d/%m/%Y")
            add_day=Calendar({self.date:self.task}) #Вот об этом был вопрос. По плану календарь это список а DayPlan словарь
            self.task=input('Введите заметку:\n')'''


#товары на складе
'''storage=[]
class InventoryItem:
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price

    """def add_card(self):
        obj=[]
        for i in range (3):
            name=input('Название товара: ')
            quantity=int(input('Количество: '))
            price=int(input('Цена: '))
            obj[i]=InventoryItem(name,quantity,price)
        storage.append([name,quantity,price])"""
    
    def add_count(self, amount):
            self.quantity += amount
            print(f"Количество товара {self.name} увеличено на {amount}. Итого количество на складе:{self.quantity}")

    def div_count(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"Количество товара {self.name} уменьшено на {amount}.Итого количество на складе:{self.quantity}")
        else:
            print(f"Невозможно уменьшить количество товара {self.name} на указанное количество.")

    def cost1 (self):
        cost=self.quantity*self.price
        print(f'Общая стоимость товара {self.name}:{cost}')



prod1=InventoryItem('potato',100,20)
prod2=InventoryItem('tomato',50,35)
prod3=InventoryItem('onion',70,18)
#storage.append(prod1)
"""count=int(input('Введите количчество товаров которые хотите внести: '))
for i in range(count):
    add_card()
print (storage)"""

#print(storage)
ans=int(input('Увеличить количество товара:1\nУменьшить количество товара:2\nРассчитать стоимость товара:3\n'))
ans1=int(input('Товар: 1-potato, 2-tomato, 3-onion'))
if ans==1:
    z=int(input('На какое количество увеличить?'))
    if ans1==1:
        prod1.add_count(z)
    elif ans==2:
        prod2.add_count(z)
    else:
        prod3.add_count(z)
elif ans==2:
    z=int(input('На какое количество уменьшить?'))
    if ans1==1:
        prod1.div_count(z)
    elif ans==2:
        prod2.div_count(z)
    else:
        prod3.div_count(z)
else:
    if ans1==1:
        prod1.cost1()
    elif ans==2:
        prod2.cost1()
    else:
        prod3.cost1()'''


#крестики-нолики
map=[0,1,2,
     3,4,5,
     6,7,8]
comb=[[0,1,2],[3,4,6],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def print_map():
    print(map[0],end=' ')
    print(map[1],end=' ')
    print(map[2])
    print(map[3],end=' ')
    print(map[4],end=' ')
    print(map[5])
    print(map[6],end=' ')
    print(map[7],end=' ')
    print(map[8])

def steps(step,symbol):
    ind=map.index(step)
    #if map[ind]=='X' or map[ind]=='O':  #Проверка  не сработала, не знаю как исправить
     #   print('Ячейка занята. Теперь вы пропускаете ход')
    #else:
    map[ind]=symbol
   

def rez():
    win=''
    for i in comb:
        if map[i[0]]==map[i[1]] and map[i[1]]==map[i[2]]:
            win=map[i[0]]
    return win

game_over=False
player1=True

while game_over==False:
    print_map()
    if player1==True:
        symbol='X'
        step=int(input('Игрок 1, ваш ход:'))
    else:
        symbol='O'
        step=int(input('Игрок 2, ваш ход:'))
    
    steps(step,symbol)
    win=rez()
    if win!='':
        game_over=True
    else:
        game_over=False
    player1=not(player1)

print_map()
print ('Победил', win)



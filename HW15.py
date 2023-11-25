#1
'''class Percon():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduse (self):
        return f'Добрый день, {self.name}! Ваш возраст {self.age}'
    
person1=Percon('Ольга',29)
print(person1.introduse())'''

#2
'''class IntShop:
    def __init__(self,name,description,price):
        self.name=name
        self.description=description
        self.price=price
    
    def chenge_des(self):
            note=input(f'Введите описание для товара {self.name}')
            self.description=note
            print(f"Товар: {self.name}\n{self.description}")

    def chenge_price(self):
        amount=input(f'Введите новую цену для товара {self.name}')
        self.price = amount
        print(f"Цена товара {self.name} изменилась. Новая цена {self.price}.")


prod1=IntShop('Т.Пратчет "Держи марку"','',2000)
prod2=IntShop('Н.Гейман "Сэндмен"','',3500)
prod3=IntShop('А. Сапковский "Ведьмак"','',1800)

prod1.chenge_des()
prod2.chenge_des()
prod3.chenge_des()

prod1.chenge_price()
prod2.chenge_price()
prod3.chenge_price()'''

#3
class Book():
    def __init__(self,title,autor,publikation_year,is_avalable):
        self.title=title
        self.autor=autor
        self.publikation_year=publikation_year
        self.is_avalable=is_avalable
    
    def chechout(self):
        self.is_avalable=False  #Если выданно - false, если в библиотеке - true
       

    def chechin(self):
        self.is_avalable=True

    def info(self):
        if self.is_avalable==True:
            print(f'{self.title} автор:{self.autor}\nГод выпуска:{self.publikation_year}\nВ библиотеке')
        else:
            print(f'{self.title} автор:{self.autor}\nГод выпуска:{self.publikation_year}\nНа руках у читателя')

book1=Book('Гарри Поттер и филосовский камень',"Дж.К.Роулинг",1997,False)
book2=Book('Гарри Поттер и тайная комната',"Дж.К.Роулинг",1998,True)
book3=Book('Гарри Поттер и узник Азкабана',"Дж.К.Роулинг",1999,True)

book1.info()
book2.info()
book3.info()

v=int(input('Введите номер книги:'))
ans=int(input('для выдачи книги нажмите 1, для получения книги нажмите 2, для вывода информации по книгам в бибилиотеке нажмите 3\n'))
if ans==1:
    if v==1:
        book1.chechout()
    elif v==2:
        book2.chechout()
    else:
        book3.chechout()
elif ans==2:
    if v==1:
        book1.chechin()
    elif v==2:
        book2.chechin()
    else:
        book3.chechin()
else:
    book1.info()
    book2.info()
    book3.info()

book1.info()
book2.info()
book3.info()   




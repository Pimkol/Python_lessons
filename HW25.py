#25
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

# В данном коде допущены опечатки, не похоже на Вас, подправил и отметил

class User(Base):
    __tablename__='user'
    id=Column (Integer, Sequence('user_id_seq'), primary_key=True) #Здесь была в primary key
    name=Column(String(50))
    age=Column(Integer)

engine=create_engine('sqlite:///:memory:', echo=True) #Тут было не sqlite, а aqlite
Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)
session=Session()

person1=User(name='Python', age=50)
person2=User(name='Java', age=60)

session.add_all([person1,person2]) # Здесь советую добавлять не аргументами "(person1,person2)", а списком объектов
session.commit()

persons=session.query(User).all()
for person in persons:
    print(f'Персонаж: {person.id}, возраст: {person.age}')

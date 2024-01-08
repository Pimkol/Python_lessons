#скрипт наполнения простой таблицы-справочника из ограниченного количества значений
# задаем название таблицы
table_name = 'customer_states'

# задаем столбцы таблицы
column_names = ('id', 'name')

#создаем список данных - справочник значений
states = ['бронзовый', 'серебряный', 'золотой', 'VIP']

# задаем количество строк таблицы, которое хотим заполнить - для таблицы-справочника это количество значений списка данных
k = len(states)

# генерация и запись DML-скрипта в файл
filename = f'{table_name}.sql' # формируем название выходного файла
with open(filename, 'w') as f: #открытие файла для записи
    # формируем строку с названиями столбцов
    columns_str = ', '.join(f'"{column}"' for column in column_names)
    for i in range(k):
        # генерируем значения для каждого столбца       
        # формируем список со значениями
        values = [i+1, f"'{states[i]}'"]
        # формируем строку со значениями
        values_str = ', '.join(str(value) for value in values)
        # формируем и записываем DML-запрос в файл
        insert_query = f'INSERT INTO "{table_name}" ({columns_str}) VALUES ({values_str});\n'
        print(insert_query) #вывод на консоль - для проверки и отладки
        f.write(insert_query) #запись в файл
    f.close() #закрытие файла

# Скачиваем файл на локальную машину
files.download(filename)

CREATE TABLE "order_states"(
"id" INTEGER NOT NULL,
"name" CHAR(255) NOT NULL
);
ALTER TABLE
"order_states" ADD PRIMARY KEY("id");
CREATE TABLE "product"(
"id" INTEGER NOT NULL,
"name" CHAR(255) NOT NULL,
"provider" INTEGER NOT NULL,
"price" DOUBLE PRECISION NOT NULL,
"quantity" INTEGER NOT NULL
);
ALTER TABLE
"product" ADD PRIMARY KEY("id");
CREATE TABLE "orders"(
"id" INTEGER NOT NULL,
"customer" INTEGER NOT NULL,
"state" INTEGER NOT NULL,
"delivery" INTEGER NOT NULL,
"sum" DOUBLE PRECISION NOT NULL,
"date" DATE NOT NULL
);
ALTER TABLE
"orders" ADD PRIMARY KEY("id");
CREATE TABLE "order_product"(
"id" INTEGER NOT NULL,
"order" INTEGER NOT NULL,
"product" INTEGER NOT NULL,
"quantity" INTEGER NOT NULL
);
ALTER TABLE
"order_product" ADD PRIMARY KEY("id");
CREATE TABLE "customer_states"(
"id" INTEGER NOT NULL,
"name" CHAR(255) NOT NULL
);
ALTER TABLE
"customer_states" ADD PRIMARY KEY("id");
CREATE TABLE "customer"(
"id" INTEGER NOT NULL,
"name" CHAR(255) NOT NULL,
"email" CHAR(255) NOT NULL,
"phone" CHAR(255) NOT NULL,
"state" INTEGER NOT NULL
);
ALTER TABLE
"customer" ADD PRIMARY KEY("id");
CREATE TABLE "delivery"(
"id" INTEGER NOT NULL,
"date" DATE NOT NULL,
"address" TEXT NOT NULL,
"price" DOUBLE PRECISION NOT NULL
);
ALTER TABLE
"delivery" ADD PRIMARY KEY("id");
CREATE TABLE "provider"(
"id" INTEGER NOT NULL,
"name" CHAR(255) NOT NULL,
"phone" CHAR(255) NOT NULL,
"email" CHAR(255) NOT NULL,
"address" TEXT NOT NULL
);
ALTER TABLE
"provider" ADD PRIMARY KEY("id");
ALTER TABLE
"order_product" ADD CONSTRAINT "order_product_order_foreign" FOREIGN KEY("order") REFERENCES "orders"("id");
ALTER TABLE
"product" ADD CONSTRAINT "product_provider_foreign" FOREIGN KEY("provider") REFERENCES "provider"("id");
ALTER TABLE
"orders" ADD CONSTRAINT "orders_delivery_foreign" FOREIGN KEY("delivery") REFERENCES "delivery"("id");
ALTER TABLE
"orders" ADD CONSTRAINT "orders_state_foreign" FOREIGN KEY("state") REFERENCES "order_states"("id");
ALTER TABLE
"customer" ADD CONSTRAINT "customer_state_foreign" FOREIGN KEY("state") REFERENCES "customer_states"("id");
ALTER TABLE
"order_product" ADD CONSTRAINT "order_product_product_foreign" FOREIGN KEY("product") REFERENCES "product"("id");
ALTER TABLE
"orders" ADD CONSTRAINT "orders_customer_foreign" FOREIGN KEY("customer") REFERENCES "customer"("id");
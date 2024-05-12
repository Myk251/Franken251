# GET, POST, PATCH, DELETE та OPTIONS API

import os
from peewee import Model, CharField, TextField, AutoField, DateTimeField, SqliteDatabase

# Ініціалізація шляху до даних
app_dir = os.path.dirname(os.path.abspath(__file__)) # абсолютний шлях
db_path = os.path.join(app_dir, '../../Data', 'technique.db')
db = SqliteDatabase(db_path)


# Опис моделі
class Model(Model):
    id = AutoField()  # Автоінкрементне первинне ключове поле
    name = CharField() # назва пристрою
    desc = TextField() # опис пристрою
    status = CharField() # статус наявності (в наявності чи ні)
    date_time = DateTimeField() # коли було створенно запис

    class Meta:
        database = db


# Створення БД та таблиць в тому випадку , якщо вона не ще не створена
def initialize_technique_db():
    db.connect()
    db.create_tables([Model], safe=True)
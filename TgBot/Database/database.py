import pymysql
from .configDB import *

class Database:

    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host=HOST,
                user=USER,
                password=PASSWORD,
                database=DATABASE
            )
            print("Подключение успешно установлено.")
        except Exception as ex:
            print(f"Ошибка подключения: {ex}")   

    def get_connection(self):
       if self.connection.open:
           print("Подключение установлено")
       else:
           print("Подключение не установлено")
       return self.connection.open

    def close_connection(self):
        if self.get_connection():
            self.connection.close()
            print("Подключение разорвано.")
        else:
            print("Нет активного соединения для разрыва.")

    def set_query(self,name,PhoneNumber, Address):
        if not self.get_connection():
            self.connection.connect()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO clients (Name, Address, PhoneNumber) VALUES ('{name}','{Address}','{PhoneNumber}')")
                self.connection.commit()
                print("Успешно добавлен")
                self.connection.close()
        except Exception as ex:
            print(f"Ошибка выполнения запроса: {ex}")
            return None

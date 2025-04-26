import psycopg2
import os
import csv
from typing import List, Tuple

class User:
    def __init__(self, full_name, phone_number):
        self.full_name = full_name
        self.phone_number = phone_number

    def get_listed_data(self) -> tuple:
        return (self.full_name, self.phone_number)

class DatabaseManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="new_database",
            user="myuser",
            password="myuser",
            host="localhost",
            port="5432"
        )        
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

class PhoneBook:
    db: DatabaseManager

    def __init__(self):
        self.db = DatabaseManager()
        self.create_phone_book()
    
    def create_phone_book(self):
        self.db.cur.execute(
            '''
                CREATE TABLE IF NOT EXISTS phone_book(
                    id serial primary key,
                    full_name VARCHAR(255) not null,
                    phone_number VARCHAR(255) not null
                );
            '''
        )

    def upload_from_csv(self, file_path):
        if not os.path.exists(path=file_path):
            print("Path not exists")
            return
        if os.path.splitext(file_path)[-1] != '.csv':
            print("You can upload data only from csv files")
            return

        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                user = User(full_name=row[0], phone_number=row[1])
                self.write_or_update_contact(user=user)

    def write_or_update_contact(self, user: User):
        select_user_query = "SELECT * FROM phone_book WHERE full_name=%s OR phone_number=%s"
        self.db.cur.execute(select_user_query, user.get_listed_data())
        
        users = self.db.cur.fetchall()

        if len(users) == 0:
            self.insert_data(user=user)
            print("User Created")
            return

        if users.count(user.get_listed_data()) > 0 :
            print("No data to updated")
            return
        
    def update_by_phone_number(self, phone_number):
        select_user_query = "SELECT * FROM phone_book WHERE phone_number=%s"
        self.db.cur.execute(select_user_query, (phone_number))
        
        users = self.db.cur.fetchall()

        if len(users) == 0:
            print("No user found")
            return
        
        new_name = input("Write new name: ")

        update_query = "UPDATE phone_book SET full_name=%s"
        self.db.cur.execute(update_query, new_name)
        self.db.conn.commit()

    def create_user(self):
        full_name = input("Write full name: ")
        phone_number = input("Write phone number: ")

        user = User(full_name=full_name, phone_number=phone_number)

        self.insert_data(user=user)

    def list_user(self, options:str = "") -> list:
        select_user_query = "SELECT * FROM phone_book"
        if len(options) != 0:
            select_user_query += " WHERE phone_number ILIKE %s OR full_name ILIKE %s"
            self.db.cur.execute(select_user_query, ("%" + options + "%", "%" + options + "%"))
        else:
            self.db.cur.execute(select_user_query)

        users = self.db.cur.fetchall()
        return users

    def print_users(self, options: str=""):
        users = self.list_user(options=options)
        for user in users:
            print(*user, sep=" | ")

    def update_user_by_id(self):
        users = self.list_user()
        try:
            user_id = int(input("Type user id: "))
            self.db.cur.execute("SELECT * FROM phone_book WHERE id = %s", (user_id,))
            user_data = self.db.cur.fetchone()
        
            if not user_data:
                print(f"No user found with ID {user_id}")
                return
        
            print(f"Current data: ID: {user_data[0]} | Name: {user_data[1]} | Phone: {user_data[2]}")
        
            action = input("Update user? (YES/NO): ").upper()
            if action == "YES":
            # Создаем объект User с текущими данными
                current_user = User(full_name=user_data[1], phone_number=user_data[2])
            # Вызываем update_user с ID и объектом User
                self.update_user(user_id=user_data[0], user=current_user)
        except ValueError:
            print("Invalid ID format")
        # id = int(input("Type user id:\n"))
        # user = users[id - 1]
        # print(*user)
        
        # action = input("Update user? | YES | NO |\n")
        # if action == "YES":
        #     self.update_user(user=User(full_name=user[0], phone_number=user[1]))

    def insert_data(self, user: User):
        postgres_insert_query = """ INSERT INTO phone_book(full_name, phone_number)
                                    VALUES (%s,%s)"""
        self.db.cur.execute(postgres_insert_query, user.get_listed_data())
        self.db.conn.commit()
        print("User Created")

    def update_user(self, user_id: int, user: User):
        new_name = input("Type new name or keep empty:\n")
        new_phone_number = input("Type new phone number or keep empty:\n")

        update_name = new_name if new_name else user.full_name
        update_phone = new_phone_number if new_phone_number else user.phone_number

        try:
            self.db.cur.execute(
                "UPDATE phone_book SET full_name = %s, phone_number = %s WHERE id = %s",
                (update_name, update_phone, user_id)
            )
            self.db.conn.commit()
            print("User updated successfully")
        except Exception as e:
            print(f"Error updating user: {e}")
            self.db.conn.rollback()
        # if len(new_name.strip()) == 0:
        #     new_name = user.full_name
        
        # if len(new_phone_number.strip()) == 0:
        #     new_phone_number = user.phone_number

        # update_query = 'UPDATE phone_book SET full_name=%s, phone_number=%s WHERE id=%s'
        # self.db.cur.execute(update_query, (new_name, new_phone_number))
        # self.db.conn.commit()

    def search_user(self):
        search_term = input("Write name or phone number:\n")
        self.print_users(options=search_term)

    def get_paginated_data(self, limit: int, offset: int) -> List[Tuple]:
        self.db.cur.execute(
            "SELECT * FROM phone_book ORDER BY id LIMIT %s OFFSET %s",
            (limit, offset)
        )
        return self.db.cur.fetchall()
    
    def delete_by_name_or_phone(self, search_term: str):
        self.db.cur.execute(
            "DELETE FROM phone_book WHERE full_name ILIKE %s OR phone_number ILIKE %s",
            (f"%{search_term}%", f"%{search_term}%")
        )
        self.db.conn.commit()
        print(f"Deleted {self.db.cur.rowcount} records")

    def insert_many_users(self, users: list):
        for user in users:
            self.db.cur.execute(
                "CALL insert_many_users(%s, %s)",
                (user[0], user[1])
            )
        self.db.conn.commit()
                

phone_book = PhoneBook()

while True:
    print("CHOOSE ACTION | q - QUIT | n - NEW CONTACT | u - UPDATE USER BY ID |\n| l - LIST USERS | s - SEARCH USERS BY PHONE NUMBER OR NAME | d - DELETE DATA |\n| p - PAGINATE DATA | csv - UPLOAD FROM CSV | m - INSERT MANY USERS")
    action = input("Type your action:\n").lower()
    if action == "q":
        break
    elif action == "n":
        phone_book.create_user()
    elif action == "u":
        phone_book.update_user_by_id()
    elif action == "l":
        phone_book.print_users()
    elif action == "s":
        phone_book.search_user()
    elif action == 'd':
        term = input("Enter name or phone to delete: ")
        phone_book.delete_by_name_or_phone(term)
    elif action == 'p':
        limit = int(input("Limit: "))
        offset = int(input("Offset: "))
        users = phone_book.get_paginated_data(limit, offset)
        for user in users:
            print(*user, sep=" | ")
    elif action == 'm':
        n = int(input("How many users do you want to insert?: "))
        users=[]
        for _ in range(n):
            full_name = input("Enter full name: ")
            phone_number = input("Enter phone_number: ")
            users.append([full_name, phone_number])

        phone_book.insert_many_users(users)
    elif action == "csv":
        path = input("Type path to csv file:\n")
        phone_book.upload_from_csv(path)

phone_book.db.close()
import psycopg2
import os
import csv

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
        full_name = input("Write full name")
        phone_number = input("Write phone number")

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
        id = int(input("Type user id:\n"))
        user = users[id - 1]
        print(*user)
        
        action = input("Update user? | YES | NO |\n")
        if action == "YES":
            self.update_user(user=User(full_name=user[0], phone_number=user[1]))

    def insert_data(self, user: User):
        postgres_insert_query = """ INSERT INTO phone_book(full_name, phone_number)
                                    VALUES (%s,%s)"""
        self.db.cur.execute(postgres_insert_query, user.get_listed_data())
        self.db.conn.commit()
        print("User Created")

    def update_user(self, user: User):
        new_name = input("Type new name or keep empty:\n")
        new_phone_number = input("Type new phone number or keep empty:\n")

        if len(new_name.strip()) == 0:
            new_name = user.full_name
        
        if len(new_phone_number.strip()) == 0:
            new_phone_number = user.phone_number

        update_query = 'UPDATE phone_book SET full_name=%s, phone_number=%s'
        self.db.cur.execute(update_query, (new_name, new_phone_number))
        self.db.conn.commit()

    def search_user(self):
        search_term = input("Write name or phone number:\n")
        self.print_users(options=search_term)
                

phone_book = PhoneBook()

while True:
    print("CHOOSE ACTION | q - QUIT | n - NEW CONTACT | u - UPDATE USER BY ID |\n| l - LIST USERS | s - SEARCH USERS BY PHONE NUMBER OR NAME | csv - UPLOAD FROM CSV |")
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
    elif action == "csv":
        path = input("Type path to csv file:\n")
        phone_book.upload_from_csv(path)

phone_book.db.close()
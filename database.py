import sqlite3


class DataBase:
    def __init__(self):
        self.con = ""
        self.cur = ""

    def create_database(self):
        self.con = sqlite3.connect("books.sql")
        self.cur = self.con.cursor()

        return self.cur

    def create_table(self):
        cur = self.create_database()
        cur.execute('''
            CREATE TABLE books
            (
                name, price, rating, in_stock
            )
        ''')

        return cur

    def insert_in_table(self, name, price, rating, in_stock):
        cur = self.create_table()
        column_values = '''
                INSERT INTO books
                VALUES (
                    ?, ?, ?, ?
                )
            '''
        data_tuple = (name, price, rating, in_stock)
        cur.execute(
           column_values,
           data_tuple
        )
        self.con.commit()

        return cur

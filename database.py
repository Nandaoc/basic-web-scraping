import sqlite3


class DataBase:
    def create_database(self):
        self.con = sqlite3.connect("books.sql")
        self.cur = self.con.cursor()

        return self.cur

    def create_table(self):
        cur = self.create_database()
        cur.execute('''
            CREATE TABLE books
            (
                name, price
            )
        ''')

        return cur

    def insert_in_table(self, cur, data):
        column_values = '''
                INSERT INTO books
                VALUES (
                    ?, ?
                )
            '''
        cur.execute(
           column_values,
           data
        )
        self.con.commit()

        return cur

# database = DataBase()
# table = database.create_table()
# cur = database.insert_in_table(table, ('name', 1, 2, True))
# for row in cur.execute('SELECT * FROM books ORDER BY price'):
#     print(row)
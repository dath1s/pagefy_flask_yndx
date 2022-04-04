import sqlite3

connection = sqlite3.connect('news.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
              (
              name TEXT, 
              message TEXT, 
              link Text)''')

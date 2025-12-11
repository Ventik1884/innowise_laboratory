import sqlite3

# Создание/подключение к базе данных
conn = sqlite3.connect('school.db')
conn.commit()
conn.close()
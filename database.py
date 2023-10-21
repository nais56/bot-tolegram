# database.py
import sqlite3
import config

# إعداد قاعدة البيانات
def setup_database():
    conn = sqlite3.connect(config.database_name)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, user_id INTEGER, product_url TEXT, discount_link TEXT)')
    conn.commit()

# إضافة بيانات منتج جديد
def insert_product(user_id, product_url, discount_link):
    conn = sqlite3.connect(config.database_name)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (user_id, product_url, discount_link) VALUES (?, ?, ?)', (user_id, product_url, discount_link))
    conn.commit()

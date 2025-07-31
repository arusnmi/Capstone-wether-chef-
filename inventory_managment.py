import sqlite3
from threading import local

# Create thread-local storage
thread_local = local()

def get_db():
        if not hasattr(thread_local, "connection"):
                thread_local.connection = sqlite3.connect('inventory_copy.db')
        
                thread_local.cursor = thread_local.connection.cursor()
        return thread_local.connection, thread_local.cursor

def Get_values_from_inven():
        connection, cursor = get_db()
        ingrefind = cursor.execute("SELECT Ingredient FROM my_table ")
        ingredeant_value = cursor.fetchall()
        return ingredeant_value
def show_values_from_inven(ingredient_name):
        connection, cursor = get_db()
        ingrefind = cursor.execute("SELECT Quantity FROM my_table WHERE Ingredient = ?", (ingredient_name,))
        ingredeant_value = ingrefind.fetchone()
        return ingredeant_value
def Update_values_inven(ingredient_name, new_value):
        connection, cursor = get_db()
        cursor.execute("UPDATE my_table SET Quantity = ? WHERE Ingredient = ?", (new_value, ingredient_name))
        connection.commit()

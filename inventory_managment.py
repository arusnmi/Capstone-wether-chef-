import sqlite3

connection=sqlite3.connect('inventory.db')
cursor=connection.cursor()



def Get_values_from_inven(ingredient_name):
        ingrefind=cursor.execute("SELECT * FROM my_table WHERE Ingredient= ?",(ingredient_name,))
        ingredeant_value=cursor.fetchall()
        return ingredeant_value

def Update_values_inven(ingredient_name, new_value):
        cursor.execute("UPDATE my_table SET Quantity = ? WHERE Ingredient = ?", (new_value, ingredient_name))
        connection.commit()
        

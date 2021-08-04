"""CHANGE YOUR TABLES TO MATCH WHAT IS ON YOUR COURIER AND PRODUCT LIST UPDATE THE PRODUCTS LIST AND
COURIER LIST SO THEY UPDATE AT THE LOCAL LIST AND THE DATABASE

ORDERS TABLE SHOULD MATCH WITH THIS "Customer Name","Customer Address", "Customer Phone","Courier","Order Status" THEN INSERT TO 
DATABASE ALSO REFORMAT THE DATA BASE TO 1NF 2NF 3NF ETC"""

import pymysql 
import os 
from dotenv import load_dotenv
import csv 

courier_list = [{"name": "Bob","phone":79222023},{"name": "Jack","phone":79221323},{"name": "Jake","phone":79282323},{"name": "Juss","phone":79223323},{"name": "Jason","phone":79282323},{"name": "Susan","phone":79122323}]
product_list = [{"item":"Daytona","price":15000}, {"item":"Daydate","price":11000},{"item":"natuilus","price":60000},{"item":"Royal Oak","price":25000},{"item":"Aquaracer","price":1500}, {"item":"Submariner","price":15000}]
live_orders = []
order_status = ["preparing","out for delivery","delivered"]
order_dict = {"Customer_name":None,"Customer_address":None,"Customer_phone":None,"courier":None,"order_status":None}


class database:
    def __init__(self)-> str:
        load_dotenv()
        host = os.environ.get("mysql_host")
        user = os.environ.get("mysql_user")
        password = os.environ.get("mysql_pass")
        database = os.environ.get("mysql_db")
        self.mydb = pymysql.connect(
        host,
        user,
        password,
        database,
        )
        self.cursor = self.mydb.cursor()
    
    def get_orders(self):
        sql = "SELECT * FROM orders"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for i in result:
            print(i)
            self.mydb.commit()
        print(live_orders)
    
    def get_products(self):
        sql = "SELECT * FROM products"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for i in result:
            print(i)
            self.mydb.commit()
    
    def get_courier(self):
        sql = "SELECT * FROM courier"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for i in result:
            print(i)
            self.mydb.commit()

    def add_product(self):
        new_item = input("What would you like to add?\n")
        new_item_value = input("what is the price\n")
        sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
        val = ( new_item, new_item_value)
        self.cursor.execute(sql, val)
        self.mydb.commit()
        print(self.cursor.rowcount, "record inserted.")
    
    def update_product(self):
        change1 = input("whats the new name")
        change2 = input("What the new price ")
        change3 = input('old name')
        change4 = input('old price')
        sql = f"UPDATE products SET name='{change1}', price='{change2}' WHERE name='{change3}' AND price='{change4}'"
        self.cursor.execute(sql)
        self.mydb.commit()
        print(self.cursor.rowcount, "record updated.")
    
    def delete_product(self):
        delete = input("what is the name?\n")
        sql = f"DELETE FROM products WHERE name = '{delete}'"
        self.cursor.execute(sql)
        self.mydb.commit()
        print(self.cursor.rowcount, "row deleted")
    
    def add_courier(self):
        new_item = input("What would you like to add?\n")
        new_item_value = input("what is the price\n")
        sql = "INSERT INTO courier (name, price) VALUES (%s, %s)"
        val = ( new_item, new_item_value)
        self.cursor.execute(sql, val)
        self.mydb.commit()
        print(self.cursor.rowcount, "record inserted.")
    
    def delete_courier(self):
        delete = input("what is the name?\n")
        sql = f"DELETE FROM courier WHERE name = '{delete}'"
        self.cursor.execute(sql)
        self.mydb.commit()
        print(self.cursor.rowcount, "row deleted")
        
    def update_courier(self):
        check = input("name or number?")
        if check == "name":
            change1 = input("What you want it to be")
            change2 = input('old name')
            sql = f"UPDATE courier SET name = '{change1}' WHERE name = '{change2}'"
            self.cursor.execute(sql)
            self.mydb.commit()
            print(self.cursor.rowcount, "record updated.")
        else:
            change1 = input("What you want it to be")
            change2 = input('old number')
            sql = f"UPDATE courier SET number = '{change1}' WHERE number = '{change2}'"
            self.cursor.execute(sql)
            self.mydb.commit()
            print(self.cursor.rowcount, "record updated.")
    def update_order(self):
        while True:
            sql = "SELECT * FROM orders"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            for i in result:
                print(i)
                self.mydb.commit()
            update_menu = int(input("Welcome to the update menu, press 1 for customer name 2 for address etc\n "))
            if update_menu == 1:
                change1 = input("new value")
                change2 = input("old value")
                sql = f"UPDATE orders SET customer_name='{change1}' WHERE customer_name='{change2}'"
                self.cursor.execute(sql)
                self.mydb.commit()
                print(self.cursor.rowcount, "record updated.")
                continue
            elif update_menu == 2:
                change1 = input("new value")
                change2 = input("old value")
                sql = f"UPDATE orders SET customer_address = '{change1}' WHERE customer_address='{change2}'"
                self.cursor.execute(sql)
                self.mydb.commit()
                print(self.cursor.rowcount, "record updated.")
                continue
            elif update_menu == 3:
                change1 = input("Old value")
                change2 = input("new value")
                sql = f"UPDATE orders SET customer_phone='{change1}' WHERE customer_phone='{change2}'"
                self.cursor.execute(sql)
                self.mydb.commit()
                print(self.cursor.rowcount, "record updated.")
                continue
            elif update_menu == 4:
                change1 = input("Old value")
                change2 = input("new value")
                sql = f"UPDATE orders SET live_orders='{change1}' WHERE live_orders='{change2}'"
                self.cursor.execute(sql)
                self.mydb.commit()
                print(self.cursor.rowcount, "record updated.")
                continue
            elif update_menu == 5:
                change1 = input("Old value")
                change2 = input("new value")
                sql = f"UPDATE orders SET courier='{change1}' WHERE courier='{change2}'"
                self.cursor.execute(sql)
                self.mydb.commit()
                print(self.cursor.rowcount, "record updated.")
                continue
            elif update_menu == 5:
                change1 = input("Old value")
                change2 = input("new value")
                sql = f"UPDATE orders SET order_status='{change1}' WHERE order_status='{change2}'"
                self.cursor.execute(sql)
                self.mydb.commit()
                print(self.cursor.rowcount, "record updated.")
                continue
            elif update_menu == 0:
                print('Exiting')
                break
        print(self.cursor.rowcount, "record updated.")
        self.cursor.close()
        self.mydb.close()
        
    def add_orders(self):
        print("To create a new value")
        current_order = dict(order_dict)
        customer_name =input("What is the name?\n")
        customer_address =input("What is the address?\n")
        customer_phone =input("What is the phone number?\n")
        current_order["Customer_name"] = customer_name
        current_order["Customer_address"] = customer_address
        current_order["Customer_phone"] = customer_phone
        print("You've added")
        print(current_order)
        for (i, item) in enumerate(courier_list, start=0):
            print(i, item)
        current_order["courier"] = input("What courier shall be assigned?\n")
        current_order["order_status"] = "Preparing"
        print("order status set to preparing")
        print(order_dict)
            # Create a list which stores item numbers so a courier can take more than one item
        for (i, item) in enumerate(product_list, start=1):
            print(i, item)
        order_products = [int(x) for x in input("The Order the courier is taking with a comma then a space please, very important pls pls \n").split(', ')]
        current_order["Order items"] = order_products
        print(order_products)
        str_ints = [str(x) for x in order_products]
        print(str_ints)
        ans = ','.join(str_ints)
        print(ans) #1,3
        current_order["Order items"] = ans
        live_orders.append(current_order)
        print("You've added")
        sql = "INSERT into orders (customer_name,customer_address,customer_phone,courier,order_status,live_orders) values (%s, %s, %s, %s, %s,%s)"
        val = [str(x) for x in list(current_order.values())]
        self.cursor.execute(sql,val)
        self.mydb.commit()
        print("Order added") 
    def update_order_list():
        for (i, item) in enumerate(live_orders, start=0):
                print(i, item)
        dict_index = int(input("what is the index\n"))
        live_orders[dict_index]['Customer_name'] = input('Who is the new customer?') or live_orders[dict_index]['Customer_name']
        live_orders[dict_index]['Customer_address'] = input('address?') or live_orders[dict_index]['Customer_address']
        live_orders[dict_index]['Customer_phone'] = input('What is the new number?') or live_orders[dict_index]['Customer_phone']
        live_orders[dict_index]['courier'] = input('What is the new courier?') or live_orders[dict_index]['courier']
        live_orders[dict_index]['order_status'] = input('What is the order status?') or live_orders[dict_index]['order_status']
            #Add a product
        print(live_orders[dict_index])
    def update_order_status():
        for (i, item) in enumerate(live_orders, start=0):
                print(i, item)
        for (i, item) in enumerate(order_status, start=0):
            print(i, item)
        order_index = int(input("What is the order number\n"))
        order_status_index =int(input("what is the updated status\n"))
        live_orders[order_index]["order_status"] = order_status[order_status_index]
        print(live_orders[order_index])
    def delete_order(self):
        delete = input("what is the name?\n")
        sql = f"DELETE FROM products WHERE name = '{delete}'"
        self.cursor.execute(sql)
        self.mydb.commit()
        print(self.cursor.rowcount, "row deleted")
        try:
            for (i, item) in enumerate(live_orders, start=0):
                    print(i, item)
            delete_input = int(input("What order would you like to delete?\n"))
            del(live_orders[delete_input])
            print(live_orders)
        except IndexError:
            print("No new orders")

# cursor.execute("CREATE TABLE products (productId INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price VARCHAR(255))")
# cursor.execute("CREATE TABLE courier (CourierId INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), number VARCHAR(255))")
# cursor.execute("CREATE TABLE orders (OrderId INT NOT NULL AUTO_INCREMENT PRIMARY KEY, customer_name VARCHAR(255), customer_address VARCHAR(255), customer_phone VARCHAR(255), courier VARCHAR(255), order_status VARCHAR(255), live_orders VARCHAR(255))")



def save_menu():
    try:
            with open('product.csv', 'a', newline='')  as output_file:
                keys = product_list[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                #dict_writer.writeheader()
                dict_writer.writerows(product_list)
            with open('courier.csv', 'a', newline='')  as f:
                keys = courier_list[0].keys()
                dict_writer = csv.DictWriter(f, keys)
                #dict_writer.writeheader()
                dict_writer.writerows(courier_list)
            with open('orders.csv', 'a', newline='')  as f:
                keys = live_orders[0].keys()
                print(live_orders)
                dict_writer = csv.DictWriter(f, keys)
                #dict_writer.writeheader()
                dict_writer.writerows(live_orders)
            print("Added and saved to the list")
    except FileNotFoundError:
        print('Doesnt exist')
        print("Exiting, Goodbye!") 
def first_menu():
    while True:
            
            #Product menu
            main_menu = int(input("Welcome to the Product \n Press 0 for Exit \n Press 1 to see the list\n Press 2 to add to the list\n Press 3 to replace at a certain index\n Press 4 to delete items\n"))
            print(main_menu)
            if main_menu == 0:
                print('returning to homescreen')
                break
            elif main_menu == 1:
                WatchGalore = database()
                WatchGalore.get_products()
                continue
            elif main_menu == 2:
                WatchGalore = database()
                WatchGalore.add_product()
                continue
            elif main_menu == 3:
                WatchGalore = database()
                WatchGalore.update_product()
                continue
            elif main_menu == 4:
                WatchGalore = database()
                WatchGalore.delete_product()
def second_menu():
    while True:
            #Courier menu
            main_menu = int(input("Welcome to the Product \n Press 0 for Exit \n Press 1 to see the list\n Press 2 to add to the list\n Press 3 to replace at a certain index\n Press 4 to delete items\n"))
            print(main_menu)
            if main_menu == 0:
                print('returning to homescreen')
                break
            elif main_menu == 1:
                WatchGalore = database()
                WatchGalore.get_courier()
                continue
            elif main_menu == 2:
                WatchGalore = database()
                WatchGalore.add_courier()
                continue
            elif main_menu == 3:
                WatchGalore = database()
                WatchGalore.update_courier()
                continue
            elif main_menu == 4:
                WatchGalore = database()
                WatchGalore.delete_courier()
                continue
def third_menu():
    while True:
        main_menu = int(input("Welcome to the Order menu\n Press 0 for Exit\n Press 1 to see live orders\n Press 2 to add orders\n Press 3 to update order status\n Press 4 to update an order\n Press 5 to delete a order\n"))
        if main_menu == 0:
            print("EXIT")
            break
        elif main_menu == 1:
            WatchGalore = database()
            WatchGalore.get_orders()
            continue
        elif main_menu == 2:
            WatchGalore = database()
            WatchGalore.add_orders()
        elif main_menu == 3: #update existing order status
            WatchGalore = database()
            WatchGalore.update_order_status()
        elif main_menu == 4: #update whole order
            WatchGalore = database()
            WatchGalore.update_order_list()
            while True:
                WatchGalore = database()
                WatchGalore.update_order()
                break
        elif main_menu == 5: #delete order
            WatchGalore = database()
            WatchGalore.delete_order()
            continue
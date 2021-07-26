""""I NEED TO CHANGE THE WAY I ADD ORDERS CURRENTLY I APPEND THEM TO THE DICTIONARY LIST WITHIN THIRDMENU() HOWEVER 
THIS CAN NOT BE ACCESSED OUTSIDE THAT FUNCTION SO I NEED TO CREATE A LIST OF DICTIONARIES WHICH APPEND OUTSIDE THE 
FUNCTION SO IT CAN BE ACCESSED GLOBALLY AND BE USED TO SAVE TO A CSV FILE AS ONLY THE LAST ORDER IS SAVING 
I ALSO NEED TO APPEND NOT WRITE PERMISSONS ON THESE FILES"""
import csv
from typing import OrderedDict


courier_list = [{"name": "Bob","phone":79222023},{"name": "Bob","phone":79221323},{"name": "Bob","phone":79282323},{"name": "Bob","phone":79223323},{"name": "Bob","phone":79282323},{"name": "Bob","phone":79122323}]
product_list = [{"item":"Daytona","price":15000}, {"item":"Daydate","price":11000},{"item":"natuilus","price":60000},{"item":"Royal Oak","price":25000},{"item":"Aquaracer","price":1500}]
order_keys = ["Customer Name","Customer Address", "Customer Phone","Courier","Order Status","Order items"]
live_orders = []
order_status = ["preparing","out for delivery","delivered"]
order_dict = {"Customer_name":None,"Customer_address":None,"Customer_phone":None,"courier":None,"order_status":None}
counter = 0 
# def create_order_letters():
#     for i in random.choices(string.ascii_lowercase, k=6):
#         print(i.upper(),end="")
# def create_order_number():
#     for i in random.choices(range(6)):
#         print(i,end="")
#Append instead of write
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
                for i in product_list:
                    print(i)
                continue
            elif main_menu == 2:
                new_item = input("What would you like to add?\n")
                new_item_value = input("what is the price")
                d = {"item":new_item,"price":new_item_value}
                product_list.append(d)
                print(product_list)
                continue
            elif main_menu == 3:
                for (i, item) in enumerate(product_list, start=0):
                    print(i, item)
                    new_index = int(input("What index\n"))
                    new_item = input("What would you like to add?\n")
                    new_item_value = input("what is the price\n")
                    j = {"item":new_item,"price":new_item_value}
                    product_list[new_index] = j
                    print(product_list)
                    continue
            elif main_menu == 4:
                delete = int(input("what is the index?\n"))
                del product_list[delete]
                print(product_list)
                continue
def second_menu():
    while True:
                #Courier menu
            smm = int(input("Welcome to the Courier menu\n Press 0 for Exit \n Press 1 to see the list\n Press 2 to add to the list\n Press 3 to replace at a certain index\n Press 4 to delete items\n"))
            print(smm)
            if smm == 0:
                print('returning to homescreen')
                break
            elif smm == 1:
                for i in courier_list:
                    print(i)
                continue
            elif smm== 2:
                new_courier = input("What would you like to add?\n")
                new_item_value = input("what is the price")
                d = {"name":new_courier,"phone":new_item_value}
                courier_list.append(d)
                print(courier_list)
                continue
            elif smm == 3:
                for (i, item) in enumerate(courier_list, start=0):
                    print(i, item)
                    new_index = int(input("What index\n"))
                    new_replacement_item =input("What would you like it to be\n") 
                    courier_list[new_index] = new_replacement_item
                    print(courier_list)
                    continue
            elif smm == 4:
                delete = int(input("what is the index?\n"))
                del courier_list[delete]
                print(courier_list)
                continue
def third_menu():
    # adjust order menu
    while True:
        main_menu = int(input("Welcome to the Order menu\n Press 0 for Exit\n Press 1 to see live orders\n Press 2 to add orders\n Press 3 to update order status\n Press 4 to update an order\n Press 5 to delete a order\n"))
        if main_menu == 0:
            print("EXIT")
            break
        elif main_menu == 1:
            print(live_orders)
            continue
        elif main_menu == 2:
            print("To create a new value")
            
            while True:
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
            #Create a list which stores item numbers so a courier can take more than one item
                for (i, item) in enumerate(product_list, start=1):
                    print(i, item)
                L = [int(x) for x in input("The Order the courier is taking with a comma then a space please, very important pls pls \n").split(', ')]
                current_order["Order items"] = L
                live_orders.append(current_order)
                print("You've added")
                print(live_orders)
                
                break 
        elif main_menu == 3: #update existing order status
            for (i, item) in enumerate(live_orders, start=0):
                print(i, item)
            for (i, item) in enumerate(order_status, start=0):
                print(i, item)
                order_index = int(input("What is the order number\n"))
                order_status_index =int(input("what is the updated status\n"))
                live_orders[order_index]["order_status"] = order_status[order_status_index]
                print(live_orders[order_index])
                break
        elif main_menu == 4: #update whole order
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
            continue
        elif main_menu == 5: #delete order
            for (i, item) in enumerate(live_orders, start=0):
                print(i, item)
            delete_input = int(input("What order would you like to delete?\n"))
            del(live_orders[delete_input])
            print(live_orders)
            continue
            
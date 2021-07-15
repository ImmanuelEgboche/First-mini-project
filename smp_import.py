courier_list = []
product_list = ["rolex", "bugatti",'patek phillipe','bmw','Q8','g63']

def save_menu():
    try:
            with open("product.txt", "w") as f:
                for i in product_list:
                    f.write(i)
                    f.write('\n')
            with open("courier.txt", 'w') as g:
                for j in courier_list:
                    g.write(j)
                    g.write('\n')
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
                new_value = input("What would you like to add?\n")
                product_list.append(new_value)
                print(product_list)
                continue
            elif main_menu == 3:
                for (i, item) in enumerate(product_list, start=0):
                    print(i, item)
                    new_index = int(input("What index\n"))
                    new_replacement_item =input("What would you like it to be\n") 
                    product_list[new_index] = new_replacement_item
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
                new_value = input("What would you like to add?\n")
                courier_list.append(new_value)
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
    updates = {}
    while True:
        main_menu = int(input("Welcome to the Order menu\n Press 0 for Exit \n Press 1 to see live orders\n Press 2 to add to the list\n Press 3 to replace at a certain index\n Press 4 to delete items\n"))
        if main_menu == 0:
            print("EXIT")
        elif main_menu == 1:
            orders = [updates]
            print(orders)
        elif main_menu == 2:
            #i want to create a new dictonary with every input 
            customer_name = input("what is the customers name")
            updates["Name"] = customer_name
            customer_address = input('what is the customers address')
            updates["Address"] = customer_address
            customer_number = input('what is the customers number')
            updates["Phone Number"] = customer_number
        elif main_menu == 3:
            for (i, item) in enumerate(courier_list, start=0):
                print(i, item)
                new_index = int(input("What index\n"))
                new_replacement_item =input("What would you like it to be\n") 
                courier_list[new_index] = new_replacement_item
                print(courier_list)
                continue
        elif main_menu == 4:
            for (i, item) in enumerate(courier_list, start=0):
                print(i, item)
        else:
            print('done')

from week6import import first_menu, second_menu, third_menu, save_menu

print('Welcome to homescreen')
while True:
    fmm = int(input("What menu would you like to access?\n Press 0 to exit\n Press 1 to access product menu\n Press 2 to access courier menu\n Press 3 to create, check orders and change status\n Press 4 to save a back-up\n"))
    print(fmm)
    if fmm == 4:
        save_menu() 
    elif fmm == 1:
        first_menu()
    elif fmm == 2:
        second_menu()
    elif fmm == 3:
        third_menu()
    elif fmm == 0:
        print("Goodbye!")
        break
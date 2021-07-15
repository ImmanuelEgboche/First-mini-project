from smp_import import save_menu, first_menu, second_menu, third_menu

print('Welcome to homescreen')
while True:
    fmm = int(input("What menu would you like to access?\n Press 0 to save and exit\n Press 1 to access product menu\n Press 2 to access courier menu\n Press 3 to create, check orders and change status\n"))
    print(fmm)
    if fmm == 0:
        save_menu()
        break 
    elif fmm == 1:
        first_menu()
    elif fmm == 2:
        second_menu()
    elif fmm == 3:
        third_menu()
from ConsoleUI import Menu


if(__name__=="__main__"):  
    menu_obj=Menu()

    while True:
        menu_obj.menue_messages()
        menu_obj.menu_apear(int(input("enter the number you want")))


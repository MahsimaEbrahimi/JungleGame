from ConsoleUI import Menu


if(__name__=="__main__"):  
    menu_obj=Menu()

    while True:
        menu_obj.menue_messages()
        try:
             menu_obj.menu_apear(int(input("enter the number you want")))
        
        except:
            print("You are entering a wrong number!!!!!!!!!!!")



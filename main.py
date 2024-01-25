from ConsoleUI import Menu


if(__name__=="__main__"):  
    menu_obj=Menu()

    while True:
        menu_obj.menue_messages()
        try:
             menu_input=int(input("enter the number you want"))             
             if (menu_input==7):
                break
             menu_obj.menu_apear(menu_input)        


        
        except:
              print("You are entering a wrong number!!!!!!!!!!!")



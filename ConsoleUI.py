from Animals import ANimal_class
from Lists import AnimaLListClass
import chk_validity
from chk_validity import chk_validity
class Menu:
    list_obj=AnimaLListClass()

    def menue_messages(self):
                print("press the number you want \
              1 for seeing all animals\
              2 for seeing the list of sleep animals \
               3 for appending an animal\
              4 for removing an animal\
              5 for searching in the list of animals\
               6 for mating of two animals")

    def menu_apear(self,number):
        Animal_we_made=None
        match number:
            case 1:
                Menu.list_obj.PAnimalList()
            case 2:
                Menu.list_obj.pSleep_Animals()
            case 3:
                print("input your animal information: ")
                Animal_name_inp=input("enter your animal name: ")
                gender_inp=input("print the gender of the animal: ")
                category_inp=input("print the category of animal: ")
                sleepType_inp=input("print the sleep type of the animal:")
                animal_sleep_chk=chk_validity.animal_sleepType_chk(sleepType_inp)

                if (chk_validity.animal_gender_ckh(gender_inp))==True:
                     if(animal_sleep_chk!=None):
                         Animal_we_made=ANimal_class(animal_sleep_chk ,gender_inp,category_inp,Animal_name_inp)
                         Animal_we_made.Sleep_method()
                         if Menu.list_obj.append(Animal_we_made)==True:
                               print("You could succefully add your animal to the list")
                else:
                     print(ValueError("wrong gender"))


            case 4:
                if (Menu.list_obj.IsEmpty()==True):
                    print("there is no animal in the list to be removed")
                    return
                else:
                    input_Ids =input("input your animal ids: ")
                    sep_id = input_Ids.split()
                    result = tuple([int(k) for k in sep_id])
                    chk_validity.animal_remove_chk(Menu.list_obj,*result)

            case 5:
                if (Menu.list_obj.IsEmpty()==True):
                    print("there is no animal in the list to be removed")
                    return                  
                else:
                    Id = int(input("Please enter the id of the animal:")) 
                    animal_search_result=Menu.list_obj.search(Id)
                    if (animal_search_result!=None):
                        print("Your animal is:",animal_search_result)

            case 6:
                    if(Menu.list_obj.Prent_Exist()==False):
                        print("there is no enough parent for mating.") 
                        return
                    
                    else:
                        parent1_Id=int(input("print the Id of the parent1"))
                        parent2_Id=int(input("print the Id of the parent2"))
                        found_animal=chk_validity.parents_chk_Id_Val(Menu.list_obj,parent1_Id,parent2_Id)
                        if(found_animal):
                            if(found_animal[0].Sleep_Parents(found_animal[1])==True):
                                   print("parents are sleep, cant mate")
                          
                            else:
 
                                mate_res= found_animal[0].Mate_method(found_animal[1])
                                if(isinstance(mate_res,ANimal_class)):
                                    Menu.list_obj.append(mate_res)
                                    print("ok, now you have an a new animal with the name of{materes.name}")
            
            case default:
             print("You are entering a wrong number!!!!!!!!!!!")
             


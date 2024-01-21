from Sleep import Sleep_class
class chk_validity:
    @classmethod
    def animal_gender_ckh(cls,gender_inp):            
            if(gender_inp in ("man","woman")):
                    return True
            else:
                    return False
    @classmethod
    def animal_sleepType_chk(cls,sleepType_inp):
        if (sleepType_inp.upper()=="DAY"):
                sleep_type=Sleep_class.Sleepday
                return sleep_type
        if (sleepType_inp.upper()=="NIGHT"):
                sleep_type=Sleep_class.SleepNight
                return sleep_type
        else:
               print(ValueError("wrong sleep type"))
               return None
    @classmethod
    def animal_remove_chk(cls,animal_List_class_obj,*args):
        # if(animal_List_class_obj.IsEmpty()==True):
        #    print("there is no animal in the list to be removed")
        #    return
        # else:
           for i in args:
                 search_result=animal_List_class_obj.search(i)
                 if(search_result)!=None:
                        animal_List_class_obj.remove(search_result)

    @classmethod
    def parents_chk_Id_Val(cls,animal_List_class_obj,*args):
                found_animal=[]
                for i in args:
                       search_result=animal_List_class_obj.search(i)
                       if(search_result)!=None:
                              found_animal.append(search_result)
                return found_animal
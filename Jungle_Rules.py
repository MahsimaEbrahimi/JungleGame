from Animals import Animals_Class
class Rules_class:
    def mating_rules(animal1,animal2):
        if animal1.category==animal2.category:
            Animals_Class.Mating()


    def eating_rules(self,type_animal_obj):
        if(type_animal_obj.SleepCond==False):
            type_animal_obj.Eat()
        else:
            type_animal_obj.Sleep()

        

    def sleeping_rules(self,type_animal_obj,time):
        if(type_animal_obj.SleepTime=="DAY" and time>=6 and time<=18):
                type_animal_obj.Sleep()
        elif (type_animal_obj.SleepTime=="NIGHT" and time>18 and time<=24):
                type_animal_obj.Sleep()
        else:
         print(f"hi,{type_animal_obj.name} is awake, what next?")


    
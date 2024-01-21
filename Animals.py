from datetime import datetime
import random as rn
class ANimal_class:
    id=0
    def __init__(self,Sleep,Gender,Category,name) :
        self.Sleep=Sleep   
        self.isSleep=None     

        self.Category=Category        
        self.id= ANimal_class.id
        ANimal_class.id+=1
        self.name=name

        self.Gender=Gender


    def Sleep_method(self):
       self.isSleep=self.Sleep(datetime.now().hour)
    
    def Sleep_Parents(self,Animal2):
        if self.isSleep==True or Animal2.isSleep==True:
            return True
        else:
            return False

    def Mate_method(self,Animal2):
        if(self.Gender==Animal2.Gender):
            print(TypeError ("Gay Error")) 
        elif self.Category==Animal2.Category:
            name_of_kid=input("input the name of child")
            return ANimal_class(rn.choice([self.Sleep,Animal2.Sleep]),
                                rn.choice([self.Gender,Animal2.Gender]),
                                rn.choice([self.Category,Animal2.Category]),name_of_kid)
        else:
            print(TypeError("category Error")) 
    

    def Eat_method(self):
        if self.Sleep_method==True:
            print("You can not eat while sleeping ")
        
        else:
            print("im eating")

    def __repr__(self) -> str:
        return f"({self.name},{self.Category},{self.Gender},{self.id},"\
        f"{self.Sleep.__name__})"
    

        
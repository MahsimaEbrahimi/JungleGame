from Animals import ANimal_class
from functools import wraps

class AnimaLListClass(list["ANimal_class"]):
    def PAnimalList(self):
        for i in self:
            print(i)
        if(len(self)==0):
            print("there is no animal added in the list")
    
    def pSleep_Animals(self):
        Awake=[]
        count_sleep_animals=0
        if(self.IsEmpty()==False):
            for i in self:
                if i.isSleep==True:
                    print(i.name,end=",")
                    count_sleep_animals+=1
                    Awake.append(1)
            print()
            
        else:
          print("there is no animal added in the list. you have to add one") 
    
    
    def IsEmpty(self):
        if(len(self)==0):
            return True
        else:
            return False
        
    def Prent_Exist(self):
        if(len(self)<2):
           return False
        else:
            return True

    def decoratorIf(func):
       @wraps(func)         
       def wrap_dec(self,*args):
          global flag
          try: 
            for k in args:
             if(isinstance(k,ANimal_class)):
               flag=True
             else:
                print(k.__class__)
                flag=False

             global value
             value=func(self ,k)              
            return value
          except:
              print(ValueError("wrong value"))
       return wrap_dec

    @decoratorIf
    def append(self, *args) -> None:            
       if flag==False:
            print("You are adding wrong value ")
            return flag
       for i in args:
            super().append(i)   
       return True

    
    @decoratorIf
    def remove(self, *args) -> None:             
              if flag==False:
                  print ("You are removing wrong value")
                  return flag
              
              for i in args:
                super().remove(i)
                print("You successfully deleted animals")
              return True

    def search(self,id):
        for i in self:
            if i.id==id:
                return i
#OOP (Object Oriented Programing) - part 1

class MyClass():
    '''
        First class for  calculate sum and multiplication 2 number.
    '''
    def __init__(self,number_1:int,number_2:int):
        self.number_1 = number_1
        self.number_2 = number_2
    
    def sum(self):
        '''
         This method for sum number_1 and number_2
        '''
        return self.number_1 + self.number_2
    
    def multiplication(self) -> int:
        '''
         This method for multiplication number_1 and number_2
        '''
        return self.number_1 * self.number_2
 
obj_0=MyClass(2, 3)
print(obj_0) #<__main__.MyClass object at 0x7f70c264ace0>
print(obj_0.sum()) #5
print(obj_0.multiplication()) #6

class Student():
    '''
        This class get name and score each student and append to the list.
    '''
    def __init__(self,name:str,score:int):
        self.information={}
        self.information['name'] = name
        self.information['score'] = score
        
    def get_student_information(self) -> dict:
        '''
        This method return student information.
        '''
        return self.information
obj_1 = Student('Sajjad', 20)    
print(obj_1.get_student_information()) #{'name': 'Sajjad', 'score': 20}

#Public variable in class
class Car:
    '''
        This class consist of public variable.
    '''
    model = 'peugeot' # public variable
    def __init__(self,tip:str):
        self.tip = tip
    
obj_2 = Car('206')
obj_3 = Car('208')
print(obj_2.model) #peugeot
print(obj_3.model) #peugeot
print(obj_2.tip) #206 - we can access variable.
print(obj_3.tip) #208 - we can access variable. 
  
class MyClass1:
    '''
        This class consist of public variable.
    '''
    global_list=[] #class variable - public variable.
    def __init__(self):
        pass
    def my_func(self,arg_0):
        '''
        This method return student information.
        '''
        return self.global_list.append(arg_0)  
obj_0 = MyClass1()
obj_1 = MyClass1()
obj_0.my_func(1)
obj_0.my_func(2)
obj_0.my_func(3)

print(obj_0.global_list) #[1, 2, 3] - we call global variable.
print(obj_1.global_list) #[1, 2, 3] - we call global variable. because global_list is a global or general variable so when we add value with obj_0 then obj_1 also has access to it.

#Private variable in class
class PrivateVariable:
    '''
        This class consist of private variable.
    '''
    def __init__(self,a,b):
        self.a = a
        self.__b = b #private  - not accessible out of class normally.
    def my_func(self) -> int:
        '''
        This method return private variable.
        '''
        self.__b +=1
        return(self.__b)
        
obj_0 = PrivateVariable(1, 2)
print(obj_0.a) # 1
#print(obj_0.__b) ## AttributeError - because 'b' is a private variable we can not access that out of class with normal calls. but we can access private variables by other methods in class.
print(obj_0.my_func()) #3 - for access to __b variable we should call  my_func method.

#Access private variables with name mangling.
class MyPrivateClass:
    '''
        This class consist of private variable.
    '''
    def __init__(self,var_a,b):
        self.var_a = var_a    #public variable
        self.__b = b  #private variable.
    
    def my_func(self):
        '''
        This method return private variable.
        '''
        self.__b+=1
        return (self.__b)
obj_0=MyPrivateClass(1, 2)
print(obj_0.var_a) #1 
print(obj_0.__dict__) # {'var_a': 1, '_MyPrivateClass__b': 2} 
print(obj_0._MyPrivateClass__b) #2 name mangling.
print(obj_0.my_func())  #3
             
             
             
#Private method in class -  we can define and access private methods like private variables.     
class PrivateMethodClass:
    '''
        This class consist of private method.
    '''
    def __my_private_method(self):
        '''
        This is a private method and return a string.
        '''
        self.result= 'This is a private method'
        return self.result
    def  my_public_class(self):
        '''
        This is a public method and return a string.
        '''
        self.result= 'This is a public method'
        return self.result

obj_0=PrivateMethodClass()

print(obj_0.my_public_class()) #This is a public method
print(obj_0._PrivateMethodClass__my_private_method()) #This is a private method

#OOP (Object Oriented Programing) - part 2
# Dunder method and overloading:
# __init__
# __str__
# __repr__
# __len__
# __getitem__ 
# __setitem__
# __call__
# __add__
# Data descriptor:
# __set__
# __get__

class MyClass2:
    '''
        This class consist of dunder method.
    '''
    def __init__(self):
        self.lst=[45,46,21]

obj_0=MyClass2()
print(obj_0)     #<__main__.MyClass2 object at 0x7f6186567b80>
print(obj_0.lst) #[45, 46, 21] 

class MyClass3:
    '''
        This class consist of dunder method.
    '''
    def __init__(self):
        self.lst=[45,46,21]
    def __str__(self):
        return str(self.lst)    

obj_0=MyClass3()
print(obj_0)     #[45, 46, 21]   
print(obj_0.lst) #[45, 46, 21]  

class MyClass4:
    '''
        This class consist of dunder method.
    '''
    def __init__(self):
        self.new_list=[60,32,95]
    def __len__(self):
        return len(self.new_list)
    def __getitem__(self,new_list_index):
        return self.new_list[new_list_index]
    def __setitem__(self,new_list_item,value):
        self.new_list[new_list_item] = value
    

obj_4=MyClass4()
print(obj_4.new_list)
print(len(obj_4)) #3
#print(len(obj_4)) #without __len__ method: TypeError: object of type 'MyClass4' has no len().
print(obj_4[1]) # get index from   __getitem__ method.
obj_4[1]=60 #change list item with __setitem__ method.
print(len(obj_4)) 
print(obj_4.new_list)







  
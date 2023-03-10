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
    def __str__ (self):
        return str(self.new_list)   
    

obj_4=MyClass4()
print(obj_4.new_list) #[60,32,95]
print(len(obj_4)) #3
#print(len(obj_4)) #without __len__ method: TypeError: object of type 'MyClass4' has no len().
print(obj_4[1]) # get index from   __getitem__ method.
obj_4[1]=39 #change list item with __setitem__ method.
print(len(obj_4)) 
print(obj_4.new_list) #[39,32,95]
print(obj_4) #[39,32,95] - get data from __str__
class Address:
    '''
        This class consist of dunder method.
    '''
    def __init__(self,c,s,z):
        self.city=c
        self.street=s
        self.zipcode=z
    def __str__(self):
        lst=[]
        lst.append(f'{self.city} - {self.street} - {self.zipcode}') 
        return ' '.join(lst)
obj_0=Address('Tehran','pirozi','123')
print(obj_0) # Tehran - piroozi - 123     

#OOP (Object Oriented Programing) - part 3 - Inheritance
class Person():
    '''
        This is a parent class.
    '''
    def __init__(self,name):
        self.name=name
        
    def show(self):
        '''
            print student name.
        '''
        print('name: ',self.name)

class StudentClass(Person):
    '''
        This is a child class.
    '''
    def __init__(self,name,score):
        self.score=score
        Person.__init__(self, name) #For variable calls  from the parent method we should have use the class name and__init__ dunder method.
    
    def welcome(self):
        '''
            print welcome student message.
        '''
        print('Welcome:',self.name)
          
obj_5=StudentClass('Sajjad',20)
obj_5.welcome() #Welcome: Sajjad
obj_5.show() #name:  Sajjad       
print(StudentClass.__mro__) #(<class '__main__.StudentClass'>, <class '__main__.Person'>, <class 'object'>)
#Using the Sajjad method, you can see the parents of each class. The parent class also inherits from the object class.        

#In the example below D class has 2 parents.Derived from two classes B1 and B2.
class B1:
    '''
        This is a parent class.
    '''
    def __init__(self,x):
        self.x=x
        print(x)
class B2:
    '''
        This is a parent class.
    '''
    def __init__(self,y):
        self.y=y
        print(y)
class D1(B1,B2):
    '''
        This is a child class.
    '''
    def __init__(self,z):
        print(z)
        B1.__init__(self,2)
        B2.__init__(self,3)
                
obj_6 =D1(1) # 1 2 3    
print(D1.__mro__) #(<class '__main__.D1'>, <class '__main__.B1'>, <class '__main__.B2'>, <class 'object'>)            
  
class Employee:
      def __init__(self, id, name):
          self.id = id
          self.name = name
    

 #This example is used to calculate salary.
class HE(Employee):
      def __init__(self, id, name, hw, hr):
          super().__init__(id, name)
          self.hw = hw
          self.hr = hr
 
      def h(self):
          return self.hw * self.hr      
      
class SE(Employee):
      def __init__(self, id, name, s):
          super().__init__(id, name)
          self.s = s
      
      def h(self):
          return self.s   
    
class CE(SE):
      def __init__(self, id, name, s, c):
          super().__init__(id, name , s)
          self.c = c
      
      def h(self):
          return self.s + self.c   

class P:
    def payroll(self,lst):
        for i in lst:
            print(f'{i.id}:{i.name} = {i.h()}')  
ob1 = HE(1,'sara', 4, 100000)            
ob2 = SE(2,'ali',5000000)
ob3 = CE(3,'taha',3000000,500000)

ob = P()
ob.payroll([ob1, ob2, ob3])  
'''  
1:sara = 400000
2:ali = 5000000
3:taha = 3500000
'''   

#Diamond problem
#If a class has 2 parents and we call the same name and common function in both classes, which class returns the response? The class that is written first will be called.      
class A:
   def f(self):
       print('A')
       
class B(A):
   def f(self):
       print('B')
       
class C(A):
   def f(self):
       print('C')
       
class D(B, C):
    pass

d = D()    
d.f()   # B

#Private and Protected variable  in class
class B: 
    def __init__(self, x, y):
        self._a = x      # protected
        self.__b = y     # private
    
    def f(self):       
        print(self._a)
        print(self.__b) 
    
class D(B):    
    def h(self):
        print(self._a)
        #print(self.__b) # error 'D' object has no  attribute '_D__b'
        
d = D(1, 2)        
d.h()   # 1
d.f()   # 1 2

#Private and Protected method in class
class B:
    def __f(self):
        return 'A'
    
    def g(self):
        print(self.__f())
        
class D(B):    
    def __f(self):
        return 'B'

d = D()
d.g()    # A    
#OOP (Object Oriented Programing)

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
    
        
    
    
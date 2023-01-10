#OOP (Object Oriented Programing)

class MyClass():
    '''
        First class for  calculate sum and multiplication 2 number.
    '''
    def __init__(self,number_1:int,number_2:int) -> int:
        self.number_1 = number_1
        self.number_2 = number_2
    
    def sum(self):
        '''
         This method for sum number_1 and number_2
        '''
        return self.number_1 + self.number_2
    
    def multiplication(self):
        '''
         This method for multiplication number_1 and number_2
        '''
        return self.number_1 * self.number_2
 
obj_0=MyClass(2, 3)
print(obj_0) #<__main__.MyClass object at 0x7f70c264ace0>
print(obj_0.sum()) #5
print(obj_0.multiplication()) #6
 
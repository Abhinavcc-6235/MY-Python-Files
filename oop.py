#****************************************************
#*************object oriented programming************
#****************************************************
# # name1='abhinav'
# # name1_age=25
# # name2='arjun'
# # name2_age=22
# # name3='dhanesh'
# # name3_age=26
# # name4='ajith'
# # name4_age=22
# # name5='jerin'
# # name5_age=24
# # print(name1,name1_age,'\n',name2,name2_age,'\n',name3,name3_age,'\n',name4,name4_age,'\n',name5,name5_age)
# ##class class name
# #
# from typing import Any


# class student:
#    def __init__(self,name,age):
#       self.name=name
#       self.age=age
# stud1=student('jhon',23)
# stud2=student('abhi',25)
# stud3=student('arjun',22)
# stud4=student('dhanesh',22)
# stud5=student('ajith',22)

# # print(stud1.name,stud1.age,'\n',stud2.name,stud2.age,'\n',stud3.name,stud3.age,'\n',stud4.name,stud4.age,'\n',stud5.name,stud5.age)   

# class Book:
#    def __init__(self,name,author,year,distribute):
#       self.name=name
#       self.author=author
#       self.year=year
#       self.distribute=distribute
# Book1=Book('empire','jhon',2001,'itc')
# Book2=Book('timeline','edwin',2003,'j&j') 
# Book3=Book('aadu jeevatham','',1997,'dc') 
# Book4=Book('my life','merin',2000,'mybook') 
# Book5=Book('life','joy',2005,'good book') 

# # print(Book.name,'\n',Book.author',\n',Book.year,'\n',Book1.distribute)
# #displaying data using functions
# class Employee:
#    age=10
#    #class attributes
#    def __init__(self,name,salary,id_no,jobe_role,joining_date):
#       self.name=name
#       self.salary=salary
#       self.id_no=id_no
#       self.jobe_role=jobe_role
#       self.joining_date=joining_date

#    def display_details(self):
#      print(self.name,self.salary,self.id_no,self.jobe_role,self.joining_date)    #methode(self is the first parameter)

      
# Employee1=Employee('abhinav',50000,45,'engineer','20/01/2025')   
# Employee1.display_details()

# Employee2=Employee('arjun',60000,48,'analyst','26/09/2024')
# Employee2.display_details()
# Employee3=Employee('aju',70000,58,'data scienist','07/11/2021') 
# Employee3.display_details() 
# Employee4=Employee('arun',40000,48,'analyst','12/06/2026')
# Employee4.display_details()    
# # print('name_','_salary','_id','_job role','_year')
# # print(Employee1.name,Employee1.salary,Employee1.id_no,Employee1.jobe_role,Employee1.joining_date)
# # print(Employee2.name,Employee2.salary,Employee2.id_no,Employee2.jobe_role,Employee2.joining_date)
# # print(Employee3.name,Employee3.salary,Employee3.id_no,Employee3.jobe_role,Employee3.joining_date)
# # print(Employee4.name,Employee4.salary,Employee4.id_no,Employee4.jobe_role,Employee4.joining_date)
# #*************************
# #asscing class atribute
# print(Employee.age)

# class student():
#    count=0
#    def __init__(self,name,age,height):
#       self.name=name
#       self.age=age
#       self.height=height
# # std1=student('abhinav',25,178) 
#       student.count=student.count+1
# #construcor counted by1
    
#    def display_count(self):
#      print(student.count)
    
# std1=student('abhinav',25,178)
# std1=student('arjun',22,180)
# std1=student('dhanesh',25,177)
# std1.display_count()    

#inheritance
# class Animals:
#    def __init__(self,has_leg):
#       self.has_leg=has_leg
# class dog(Animals):
#    pass
# dog=dog(has_leg='yes')
# print('the dog has 4 legs',dog.has_leg)      

# class Animal:
#    def __init__(self,sleep,eat,):
#       self.sleep=sleep
#       self.eat=eat

# class Dog(Animal):
#    def __init__(self,sleep,eat,):
#       super().__init__(sleep,eat)
#       self.speak="bow"
      
# class Cat(Animal):
#    def __init__(self,sleep,eat):
#       super().__init__(sleep,eat)
#       self.speak='meow'
# dog=Dog(sleep='yes',eat='yes')
# cat=Cat(sleep='yes',eat='yes')
 

# print(dog.sleep,dog.eat,dog.speak)
# print(cat.sleep,cat.eat,dog.speak)

print('***************************')
# class Animal:
#    def __init__(self,name,age):
#       self.name=name
#       self.age=age

#    def eat(self):
#       print('the animal is eating')
# class Dog(Animal):
#    def bark(self):
#        print('bow  bow')
      
# class Cat(Animal):
#     def meow(self):
#        print('meow meow')

# dog=Dog('dobu',56)
# cat=Cat('rocky',34)
# print(dog.name,dog.age)
# dog.eat()
# dog.bark()
# print(cat.name,cat.age)
# cat.eat()
# cat.meow()
#***************************
# print('****************************')
# class person:
#     def __init__(self,name,age):
#        self.name=name
#        self.age=age 
#     def display(self):
# class Student(person):
#    def __init__(self, name, age,course):
#       super().__init__(name, age)
#       self.course = course     

#    def show_course(self):
#       print('students corse:',self.course) 

# print(Student( 'abhinav',25,'data science'))

# #************************************
# #***********abstract***************
# from abc import ABC,abstractmethod
# class Bank(ABC):
#    @abstractmethod
#    def deposit(self):
#       pass
#    @abstractmethod
#    def loan(self):
#       pass
# class SBI(Bank):
#     def deposit(self):
#        print('deposited is exicuted')
    
#     def loan(self):
#        print('loan is applied')
#     def profit(self):
#        print('profit')
       

# sbi=SBI()
# sbi.deposit()
# sbi.loan()
# sbi.profit()
from abc import ABC,abstractmethod
class Shape(ABC):
   @abstractmethod
   def area(self):
      pass
class Rectangle(Shape):
   def __init__(self,length,width):
        self.length=length
        self.width=width
   def area(self):
      rect_area= self.length*self.width
      print(rect_area)

class Circle(Shape):
    def __init__(self,radius):
      self.radius=radius
    def area(self):
      circ_value=3.14*self.radius*self.radius
      print(circ_value)
      
rectangle=Rectangle(4,10) 
print(rectangle.area())
circle=Circle(8)
print(circle.area())





   
   
   
      
      
      
   

      


 

      

   
      
   

      
        

    
               


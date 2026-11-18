# class Animal:
#  def move(self):
#   print('animal walks')

# class Frog(Animal):
#    def move(self):
#      print('frog jump')

# frog=Frog()
# frog.move()   

class Animal:
 def move(self):
  print('animal ')

class Dog(Animal):
   def sound(self):
     print('dog sound bow')

class Cat(Animal):
   def sound(self):
     print('cat sound meow')     

dog=Dog()  
dog.sound()
cat=Cat()
cat.sound()

class Vehicle():
  def start(self):
    print('vehicle starting')

class Car(Vehicle):
  def start(self):
    print('car strat using key')

class electric_bike(Vehicle):
  def start(self):
    print('bike start using key')

car=Car()
car.start()    



   
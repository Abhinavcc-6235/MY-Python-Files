class Animal:
    def eat(self):
        print('animal is dog')

class Walaks():
    def walk(self):
        print('walkes')

class Dog(Animal, Walaks):
      def bark(self):
          print('bow')



dog = Dog()
dog.eat()
dog.walk()
dog.bark()

print('***********************')

class Camera():
    def take_photo(self):
        print('capture photo')

class Call():
    def make_call(self):
        print('call friend')

class Smartphone(Camera,Call):
    def internet(self):
        print('browsing internet')    

smartphone=Smartphone()
smartphone.make_call()
smartphone.take_photo()
smartphone.internet() 

print('*************************')

class Mediaplayer():
    def play_video(self):
        print('playing video')

class Internetdevice():
    def conect_wifi(self):
        print('connected to wifi')

class SmartTV(Mediaplayer,Internetdevice):
    def change_channel(self):
        print('changing tv channel')

smarttv=SmartTV()
smarttv.play_video()
smarttv.conect_wifi()
smarttv.change_channel()
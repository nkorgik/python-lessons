from abc import ABC, abstractclassmethod

class Person(ABC):
    @abstractclassmethod
    def speak(self):
        pass
        

class Pupil(Person):
    def speak(self):
        print('Woof!')

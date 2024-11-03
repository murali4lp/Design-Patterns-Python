class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Dog'

    def speak(self):
        return 'Woof!'
    
class DogFood:
    def __str__(self):
        return 'Dog Food'
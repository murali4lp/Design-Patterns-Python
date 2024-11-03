class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Cat'

    def speak(self):
        return 'Meow!'
    
class CatFood:
    def __str__(self):
        return 'Cat Food'
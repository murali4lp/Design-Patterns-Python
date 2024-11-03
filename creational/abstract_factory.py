from shared.dog import Dog, DogFood
from shared.cat import Cat, CatFood

class DogFactory:
    """ Concrete factory which produces dog and dog food objects"""

    def get_pet(self, pet_name='Scooby'):
        return Dog(pet_name)
    
    def get_pet_food(self):
        return DogFood()
    
class CatFactory:
    """ Concrete factory which produces cat and cat food objects"""

    def get_pet(self, pet_name = 'Tom'):
        return Cat(pet_name)
    
    def get_pet_food(self):
        return CatFood()
    
class PetStore:
    """ Abstract factory """
    pet_factories = dict(dog=DogFactory(), cat=CatFactory())

    def __init__(self, pet_factory_name=None):
        self._pet_factory = self.pet_factories[pet_factory_name]

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_pet_food()

        print("Our pet is '{}'!".format(pet))
        print("Pet says '{}'!".format(pet.speak()))
        print("its food is '{}'".format(pet_food))
  
if __name__ == '__main__':

    def get_pet_store(factory_name='dog'):
        return PetStore(factory_name)
    
    shop = get_pet_store('dog')
    shop.show_pet()

    shop = get_pet_store('cat')
    shop.show_pet()
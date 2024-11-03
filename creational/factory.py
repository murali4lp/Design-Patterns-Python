from shared.dog import Dog
from shared.cat import Cat
    
"""
The factory method
"""
def get_pet(pet_name, pet='dog'):
    pets = dict(dog=Dog(pet_name), cat= Cat(pet_name))
    return pets.get(pet)



if __name__ == '__main__':
    d = get_pet('Scooby', 'dog')
    print(d.name)
    print(d.speak())

    c = get_pet('Tom', 'cat')
    print(c.name)
    print(c.speak())

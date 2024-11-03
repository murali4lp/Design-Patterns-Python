import copy

class Prototype:

    def __init__(self):
        self._objects = {}
    
    def register_object(self, name, obj):
        self._objects[name] = obj

    def deregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(kwargs)
        return obj
    
class Car:
    def __init__(self):
        self.name = 'Skylark'
        self.color = 'Red'
        self.options = 'Ex'
        self.engine = None

    def __str__(self):
        return f"{self.name} | {self.color} | {self.options} | {self.engine}"
    

if __name__ == '__main__':
    c = Car()
    prototype = Prototype()
    prototype.register_object('skylark', c)
    print(c)

    clone = prototype.clone('skylark', engine='Turbo')
    print(clone)
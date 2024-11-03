class Subject:

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):
    
    def __init__(self, name=""):
        super().__init__()
        self._name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp
    
    @temp.setter
    def temp(self, temp):
        self._temp = temp
        self.notify()


class TempViewer:
    """Observer class"""

    def update(self, subject):
        print(f"Temperature viewer: {subject._name} has temperature {subject.temp}")


if __name__ == '__main__':
    c1 = Core('Core 1')
    c2 = Core('Core 2')
    
    v1 = TempViewer()
    v2 = TempViewer()

    c1.attach(v1)
    c1.attach(v2)

    c1.temp = 80
    c1.temp = 90
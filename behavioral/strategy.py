import types

class Strategy:
    """ Strategy pattern class"""

    def __init__(self, func=None):
        self.name = 'Default Strategy'

        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(f"{self.name} is used")


def strategy_one(self):
    print(f"{self.name} is used to execute method 1")

def strategy_two(self):
    print(f"{self.name} is used to execute method 2")


if __name__ == '__main__':
    s0 = Strategy()
    s0.execute()

    s1 = Strategy(strategy_one)
    s1.name = 'strategy 1'
    s1.execute()

    s2 = Strategy(strategy_two)
    s2.name = 'strategy 2'
    s2.execute()
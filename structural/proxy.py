import time

class Producer:
    """ Define the resource intensive object to instantiate"""
    
    def produce(self):
        print("Producer is busy!")

    def meet(self):
        print("Producer is available now!")

class Proxy:
    """ Define the relatively less resource intensive proxy to instantiate"""
    
    def __init__(self):
        self.occupied = False
        self.producer = None

    def produce(self):
        """Check if the producer is available"""

        print("Checking if producer is available")
        if not self.occupied:
            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()
        else:
            time.sleep(2)
            print("Producer is busy")


if __name__ == '__main__':
    p = Proxy()
    p.produce()

    p.occupied = True
    p.produce()
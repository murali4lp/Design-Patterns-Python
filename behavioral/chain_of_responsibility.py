class Handler:
    """Abstract Handler"""

    def __init__(self, successor):
        self._successor = successor

    def next(self, request):
        handled = self._handle(request)

        if not handled:
            self._successor.next(request)

    def _handle(self, request):
        raise NotImplementedError
    

class ConcreteHandler1(Handler):

    def _handle(self, request):
        if 0 < request <= 10:
            print(f"Request {request} handled by request handler 1")
            return True
        
class ConcreteHandler2(Handler):

    def _handle(self, request):
        if 11 < request <= 100:
            print(f"Request {request} handled by request handler 2")
            return True
        
class DefaultHandler(Handler):

    def _handle(self, request):
        print(f"End of chain. No handler for request {request}")
        return True
            

class Client:

    def __init__(self):
        self.handler = ConcreteHandler1(ConcreteHandler2(DefaultHandler(None)))

    def delegate(self, requests):
        for request in requests:
            self.handler.next(request)


if __name__ == '__main__':
    c = Client()

    requests = [2, 50, 300]

    c.delegate(requests)
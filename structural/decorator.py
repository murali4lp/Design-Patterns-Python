from functools import wraps

def highlight(func):
    """Decorated function"""
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        return f"<h1>{return_value}</h1>"
    
    return wrapper

@highlight
def hello_world():
    """Original function"""
    return 'Hello, World'

if __name__ == '__main__':
    print(hello_world())
    print(hello_world.__name__)
    print(hello_world.__doc__)
from functools import wraps


def repeat (n):
    if ( n > 0 and isinstance(n, int)):
        def decorator(func):
            @wraps(func)
            def wrapper(*args,**kwargs):
                num = n
                while (num > 0):
                    result = func(*args,**kwargs)
                    num -=1
                return result    
            return wrapper
        return decorator
    else:
        raise ValueError("Error")

@repeat(3.5)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alex")
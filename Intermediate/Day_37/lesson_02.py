import time
from functools import wraps


def time_decorator (func):
    @wraps(func)
    def wrapper(*args ,**kwargs):
        start = time.perf_counter()
        try:
            result = func(*args,**kwargs)
            return result
        except Exception as error:
            print(f"Error : {error}")
            raise
        finally:
            end = time.perf_counter()
            print(f"Время выполнения {end - start}")
    return wrapper


@time_decorator
def sum_n (n):
    result = 0
    while (n != 0):
        result += n
        n -= 1
    return result
        
print(sum_n(1000000000))


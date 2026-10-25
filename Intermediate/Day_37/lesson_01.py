
def greet_decorator(func):
    def wrapper(*args , **kwargs):
        print("Добро пожаловать!")
        return func(*args ,**kwargs)
        
    return wrapper


@greet_decorator
def show_name(name):
    print(f"Меня зовут, {name} ")


show_name("alex")
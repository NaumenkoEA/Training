numbers = [10, 20, 30]
user = {
    "name": "Evgen",
    "age": 23
}

def show_all(*args, **kwargs):
    for value in args:
        print(value)
    
    for key , value in kwargs.items():
        print(key , value)
    


show_all(*numbers, **user)
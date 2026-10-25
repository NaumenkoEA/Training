numbers = [5, 10, 15, 20]

def sum_all(*args):
    return sum(args)

# print(sum_all(*numbers))

user = {
    "name": "Evgen",
    "age": 23,
    "city": "solik"
}

def show_user(**kwargs):
    print(kwargs)

show_user(**user)
def print_user(**kwargs):
    for key , value in kwargs.items():
        print( key , value)

# print_user(name="Evgen", age=23, city="solik")


def get_kwargs_count(**kwargs):
    return len(kwargs)

# res = get_kwargs_count(name="Evgen", age=23, city="solik")


def get_string_kwargs(**kwargs):
    return {key : value for key, value in kwargs.items() if type(value) == str}


# res = get_string_kwargs(
#     name="Evgen",
#     age=23,
#     city="solik",
#     is_admin=True
# )

def show_data(*args, **kwargs):
    for value in args:
        print(value)

    for key , value in kwargs.items():
        print(key , value)


show_data(10, 20, 30, name="Evgen", age=23)
# print(res)
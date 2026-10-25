user = {
    "name": "Evgen",
    "age": 23,
    "city": "solik",
    "is_admin": True,
    "score": 95
}


def normalize_user(user):
    result = {key : str(value) if type(value) == int or type(value) == bool else value for key ,value in user.items()}
    return result

res = normalize_user(user)

print(res)
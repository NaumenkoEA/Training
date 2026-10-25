user = {
    "name": "Evgen",
    "age": 23,
    "city": "solik",
    "is_admin": True,
    "score": 95
}

# for key ,value in user.items():
#     if(type(value) == bool):
#         print(key)

def get_keys_by_type(user, value_type):
    result = [key for key ,value in user.items() if type(value) == value_type]
    return result

# res = get_keys_by_type(user, str)

def get_values_by_type(user, value_type):
    result = [value for key ,value in user.items() if type(value) == value_type]
    return result

# res = get_values_by_type(user,int)

def get_dict_by_type(user, value_type):
    result = {key: value for key ,value in user.items() if type(value) == value_type}
    return result

# res = get_dict_by_type(user,int)

def get_count_by_type(user, value_type):
    result = {key: value for key ,value in user.items() if type(value) == value_type}
    return len(result)

# res = get_count_by_type(user,int)

def remove_fields_by_type(user, value_type):
    result = {key: value for key ,value in user.items() if type(value) != value_type}
    return result

# res = remove_fields_by_type(user,int)

def convert_int_values_to_string(user):
    result = {key: str(value) if type(value) == int else value for key ,value in user.items()}
    return result

res = convert_int_values_to_string(user)

print(res)
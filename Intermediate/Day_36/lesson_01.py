def multiply(a : int , b : int)-> int:
    return a*b


def get_name(name : str)->str:
    return name.upper()

def get_adults(players :list[dict])->list:
    return [player for player in players if player["age"] >=18]
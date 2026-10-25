def print_all(*args):
    for value in args:
        print(value)


# print_all("Evgen", 23, "solik", True)


def get_args_count(*args):
    return len(args)


def sum_all(*args):
    total = 0
    for value in args:
        total = total + value
    return total


def average_all(*args):
    return sum(args) / len(args)


def get_even_numbers(*args):
    return [value for value in args if value % 2 ==0]


def get_max_number(*args):
    return max(args)


res = get_max_number(4, 17, 2, 35, 9)


def get_number_stats(*args):
    res = {
    "count": len(args),
    "sum": sum(args),
    "min": min(args),
    "max": max(args),
    "average": sum(args) / len(args)
    }
    return res

res = get_number_stats(10, 20, 30, 40)

print(res)
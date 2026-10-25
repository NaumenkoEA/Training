class MathUtils:
    @staticmethod
    def is_even(number):
        return number % 2 == 0


print(MathUtils.is_even(10))
print(MathUtils.is_even(7))


class Player:
    game = "Football"

    @classmethod
    def get_game(cls):
        return cls.game


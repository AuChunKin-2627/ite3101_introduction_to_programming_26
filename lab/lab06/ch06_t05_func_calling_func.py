def one_good_turn(n: int):
    return n + 1


def deserves_another(n: int):
    return one_good_turn(n) + 2
d= deserves_another(3)
print(d)
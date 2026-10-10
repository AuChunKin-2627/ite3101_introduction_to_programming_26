def distance_from_zero(number):
    if type(number) == int or type(number) == float:
        return abs(number)
    return "Nope"


print(distance_from_zero("abc"))

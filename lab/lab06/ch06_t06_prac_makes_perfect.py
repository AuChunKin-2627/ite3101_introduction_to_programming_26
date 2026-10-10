def cube(number: int)->int:
    return number**3

def by_three(number: int):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


cube(10)

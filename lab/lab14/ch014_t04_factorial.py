def factorial(x: int) -> int:
    value = 1
    for i in range(x+1):
        value *= i
    return value

# Write your function below!
def fizz_count(numbers):

    count = 0
    for n in numbers:
        if n < 10:
            total = total+1
    return total

lotto = [4, 8, 15, 16, 23, 42]
small = count_small(lotto)
print(small)

# Write your function below!
def fizz_count(x):

    count = 0
    for n in x:
        if x == 'fizz':
        count = count + 1
    return count


lotto = ['fizz', 'cat', 'fizz']
small = fizz_count(lotto)
print(small)

# Write your function below!
def fizz_count(x):

    count = 0
    for n in x:
        if n < 10:
            count = count+1
    return count


lotto = ['fizz', 'cat', 'fizz']
small = fizz_count(lotto)
print(small)

phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char in 'Aa':
        print('X', end='')
    else:
        print(char, end='')

# Don't delete this print statement!
print()

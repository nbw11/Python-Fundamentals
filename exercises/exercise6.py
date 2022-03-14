# 1.  5-3 Try it yourself

alien_color = 'green'

if alien_color == 'green':
    print('You earned 5 points!')
if alien_color == 'red':
    print('You earned 5 points!')

# 2. 5-4 Try it yourself

if alien_color == 'green':
    print("Player earned 5 points for shooting!")
else:
    print('Player earned 10 points!')

if alien_color == 'red':
    print("Player earned 5 points for shooting")
else:
    print("Player earned 10 points!")


# 3.  5-5 Try it yourself

if alien_color == 'green':
    print('Player earned 5 points')
elif alien_color == 'yellow':
    print('Player earned 10 points')
else:
    print('Player earned 15 points')

if alien_color == 'yellow':
    print('Player earned 5 points')
elif alien_color == 'green':
    print('Player earned 10 points')
else:
    print('Player earned 15 points')


if alien_color == 'yellow':
    print('Player earned 5 points')
elif alien_color == 'red':
    print('Player earned 10 points')
else:
    print('Player earned 15 points')

# 4 5-6 Try it yourself

age = 67
if age < 2:
    print('This person is a baby')
elif age >= 2 and age < 4:
    print('This person is a toddler')
elif age >= 4 and age < 13:
    print('This person is a kid')
elif age >= 13 and age < 20:
    print('This person is a teenager')
elif age >= 20 and age < 65:
    print('This person is an adult')
elif age >= 65:
    print('This person is an elder')


# 5.

def boolean_funk(arg1):
    print(bool(arg1 == 12))


boolean_funk(12)
boolean_funk(1.2)
boolean_funk(0)
boolean_funk(.4)
boolean_funk(0.0)

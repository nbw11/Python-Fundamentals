# 1.
# 2-8 Number Eight

print(5 + 3)
print(10 - 2)
print(2 * 4)
print(16 / 2)

# 2-9 Favorite Number

fav_number = "1"
message = "Hi my favorite number is {}"

print(message.format(fav_number))

# 2

vari_1 = 456234
vari_2 = 68423791
vari_3 = 13794628
vari_4 = 96374


def number_sets():
    print(vari_1)
    print(vari_2)
    print(vari_3)
    print(vari_4)


print(number_sets())


def number_set1(arg1, arg2):
    print(float(arg1))
    print(int(arg2))

print(number_set1(250, 257.2))

# 4

def fave_movie():
    movie = input('What is your favorite movie?')
    times_seen = int(input('How many times have you seen it?'))

    message = 'I have seen {0} {1} times.'
    print(message.format(movie, times_seen))

fave_movie()





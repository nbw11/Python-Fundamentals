# 1. 4-3 Counting to twenty

def counter():
    for stretch1 in range(1, 21):
        print(stretch1)

# counter()

# 2. 4-6 Odd Numbers

def counter2():
    for stretch2 in range(1, 21, 2):
        print(stretch2)

# counter2()

# 4. 4-7 Threes

def counter3():
    for stretch3 in range(3, 30, 3):
        print(stretch3)

# counter3()

# 5 4-8 Cubes

def counter_cube():
    cubes = []
    for stretch in range(1, 11):
        cubes.append(stretch**3)
    print(cubes)

counter_cube()


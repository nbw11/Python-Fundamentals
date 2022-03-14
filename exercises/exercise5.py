# 1. 5-1

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 2. 5-2
print("Hello" == "hello")
print("Howdy" != "howdy!")

greeting = "HOWDY"
greeting2 = "hello"
print(greeting.lower() == "howdy")
print(greeting2.lower() == "HELLO")

print(8 > 6)
print(9 < 21)
print(10 >= 10)
print(19 <= 10)
print(10 > 2 and 3 > 2)
print(9 > 3 and 3 > 3)

print("Howdy" is "Howdy!")
print("yo" is "yo")
print("yo" is not "yoyo")
print("yes" is not "yes")

# 3.

def exercise_funk(arg1, arg2):
    alpha = arg1 + arg2
    print(alpha)
    beta = arg1 - arg2
    print(beta)
    delta = arg1 * arg2
    print(delta)
    gamma = arg1 / arg2
    print(gamma)
    phi = arg1 % arg2
    print(phi)
    theta = arg1 ** arg2
    print(theta)
    omega = arg1 // arg2
    print(omega)

 exercise_funk(2, 3)

# 4.

def exercise_funk2(argo1):
    argo1 %= 10
    print(argo1)
    argo1 -= 20
    print(argo1)
    argo1 **= 2
    print(argo1)
    argo1 += 5
    print(argo1)


exercise_funk2(10)


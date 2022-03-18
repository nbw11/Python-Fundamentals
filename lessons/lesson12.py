# Lesson 12 Exception Handling

def sample_divide():
    print('Let\'s divide two numbers.')
    try:
        first = input('The first number is?')
        second = input('The second number is?')
        answer = int(first) / int(second)
        print(answer)
    except(ZeroDivisionError, ValueError):
        print('You can\'t divide by zero, or use a string')


# sample_divide()


def multi_except_sample():
    names = ('Dave', 'Matt', 'Jody')
    these = (25.4, 30, 34)

    try:
        delta = int(these[3])
        echo = complex(these[0], 5)
        print('Delta is ' + str(delta))
    except IndexError:
        print('Please provide at least 1 argument')
    except ValueError:
        print('That is not a number')
    except TypeError:
        print('You have provided something weird')
    except NameError:
        print('I don\'t know how to calculate that')

# multi_except_sample()

# The else block can be used to execute code that does not need to be tested.
# This else will only exectue if the try succeeds
alpha, fox = 5, 10


def sample_except_else(arg):
    try:
        if fox > arg:
            golf = fox / arg
            print('Value is {0}'.format(golf))
    except ZeroDivisionError:
        print('An error has occurred')
    else:
        print('Division was successful')

# sample_except_else(14)

# The finally block is excecuted regardless of whether try block succeeds
def sample_finally():
    try:
        if fox > alpha:
            bravo = fox / (fox - alpha) - 5
            print('Value is {0}'.format(bravo))
    except ZeroDivisionError:
        print('Error occurred')
    else:
        print('else prints')
    finally:
        print('finally prints')

sample_finally()
# 1 10-6 Addition, 10-7 Addition Calculator
def simple_add():
    print('Let\'s add two numbers')
    print('Enter q to quit.')

    while True:
        try:
            first = input('The first number is?')
            if first == 'q':
                break
            second = input('The second number is?')
            if second == 'q':
                break
            answer = int(first) + int(second)
            print(answer)
        except ValueError:
            print('That is not a number =/')
            simple_add()

# simple_add()

# 2. 10-8 Cats and Dogs 10-9


def cat_names():
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        print(f'Sorry, the file {filename} does not exist.')
    else:
        print(cats.txt)


filename = 'cats.txt'
cat_names()

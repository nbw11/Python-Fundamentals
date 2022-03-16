# 5-8 + 5-9 Hello admin, no users

usernames = ['admin', 'buddy', 'guy', 'friend', 'pal']


def username_demo():
    # usernames.clear()
    if len(usernames) > 0:
        for username in usernames:
            if username == 'admin':
                print('Hello admin would you like to see a status report?')
            else:
                print('Hello {}, thank you for logging in again.'.format(username))
    else:
        print('We need to find some users!')


# username_demo()

# 5-10 Checking usernames

current_users = ['john', 'jacob', 'jingle', 'heimer', 'schmidt']
new_users = ['jacob', 'chris', 'josh', 'Schmidt', 'joe']


def username_demo_two():
    for new_user in new_users:
        if new_user in current_users:
            print(f'Please enter another username.')
        else:
            print(f'username is available')


# username_demo_two()

# 5-11 Ordinal Numbers

numberz = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def numbers():
    for number in numberz:
        # print(number)
        if number == 1:
            print('1st')
        elif number == 2:
            print('2nd')
        elif number == 3:
            print('3rd')
        else:
            print('{}th'.format(number))


# numbers()

# 4. 6-1 Person

# person = {'first_name': 'nick', 'last_name': 'willis', 'age': '30', 'city': 'wichita'}

# print(person)

# 6-7 People
tony = {'first_name': 'tony', 'last_name': 'stark', 'age': '32', 'city': 'new york'}
bruce = {'first_name': 'bruce', 'last_name': 'banner', 'age': '35', 'city': 'dayton'}
people = [tony, bruce]


def peeples():
    for person in people:
        print(people)


peeples()
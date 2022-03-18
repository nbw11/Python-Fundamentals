# 1. 8-3 T-shirt

# def make_shirt(arg, arg2):
#    print('This shirt is', arg + ' and reads', arg2)

# make_shirt('large', 'rockon')
# make_shirt(arg='large', arg2='rockon')


# 8-4


def make_shirtl(arg='L', arg2='I love python'):
    print('This shirt is', arg + ' and reads', arg2)


def make_shirtm(arg='M', arg2='I love python'):
    print('This shirt is', arg + ' and reads', arg2)


def make_shirts(arg='S', arg2='WOOOOO!'):
    print('This shirt is', arg + ' and reads', arg2)


# 8-5
def describe_city(city, country='Brazil'):
    print(city, 'is a city in', country)


# describe_city('recife')
# describe_city('salvador')
# describe_city('houston')

# 2 8-9 Messages

messages = ['hi', 'bye', 'how', 'wow']
sent_messages = []


def show_messages():
    print(messages)


# show_messages()

# 8-10

def send_messages():
    while messages:
        current_message = messages.pop()
        print(f'{current_message}')
        sent_messages.append(current_message)


# send_messages()
# print(messages)
# print(sent_messages)

# 8-11 didn't understand this I think I achieved this in the above comments

# 3. 9-1 Restaurant
# couldnt get any of this to work despite help from classmates

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name:" + self.restaurant_name)
        print("Cuisine Type:" + self.cuisine_type)

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!')


luke = Restaurant('Luke', 'whacksauce')


luke.describe_restaurant()


# 9-2

# 9-3 Users

# 1. 9-6 Ice cream stand

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name:" + self.restaurant_name)
        print("Cuisine Type:" + self.cuisine_type)

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def display_flavors(self):
        print(f'{self.flavors}')


baskinrobs = IceCreamStand('Baskin robins', 'ice cream')

print(baskinrobs.display_flavors())
print(baskinrobs.restaurant_name)

# 2. didnt have prev exercise carpal tunnel setting in
# 3. didnt have prev exercise carpal tunnel setting in (3/17/22 8:12p)


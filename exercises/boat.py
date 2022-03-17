class Boat:
    def __init__(self, size, color, type):
        self._size = size
        self._color = color
        self._type = type

    def boat_float_sink(self):
        print(str.format('The {0} is floating.', self._type))

    def get_size(self):
        return self._size

    def set_size(self, size_val):
        self._size = size_val

    def get_color(self):
        return self._color

    def set_color(self, color_val):
        self._color = color_val

    def get_type(self):
        return self._type

    def set_type(self, type_val):
        self._type = type_val

    size = property(get_size, set_size)
    color = property(get_color, set_color)
    type = property(get_type, set_type)


my_boat = Boat('large', 'white', 'yacht')

print(my_boat.color)
print(my_boat.size)
print(my_boat.type)

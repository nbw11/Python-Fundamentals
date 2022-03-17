class Guitar:
    def __init__(self, guitar_strings, guitar_type, guitar_color):
        self._guitar_strings = guitar_strings
        self._guitar_type = guitar_type
        self._guitar_color = guitar_color

    def guitar_plays(self):
        print(str.format('The {} plays a tune!', self._guitar_type))

    @property
    def guitar_strings(self):
        return self._guitar_strings

    @guitar_strings.setter
    def horse_breed(self, strings_val):
        self.guitar_strings = strings_val

    @property
    def guitar_type(self):
        return self._guitar_type

    @guitar_type.setter
    def guitar_type(self, type_val):
        self.guitar_type = type_val

    @property
    def guitar_color(self):
        return self._guitar_color

    @guitar_color.setter
    def guitar_color(self, color_val):
        self.guitar_color = color_val


my_guitar = Guitar('7', 'electric', 'black')

print(my_guitar.guitar_color)
print(my_guitar.guitar_strings)
print(my_guitar.guitar_plays())



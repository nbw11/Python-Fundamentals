class Horse:
    def __init__(self, horse_breed, horse_nature, horse_color):
        self._horse_breed = horse_breed
        self._horse_nature = horse_nature
        self._horse_color = horse_color

    def horse_gallops(self):
        print(str.format('The {} gallops!', self._horse_breed))

    @property
    def horse_breed(self):
        return self._horse_breed

    @horse_breed.setter
    def horse_breed(self, breed_val):
        self.horse_breed = breed_val

    @property
    def horse_nature(self):
        return self._horse_nature

    @horse_nature.setter
    def horse_nature(self, nature_val):
        self.horse_nature = nature_val

    @property
    def horse_color(self):
        return self._horse_color

    @horse_color.setter
    def horse_color(self, color_val):
        self.horse_color = color_val


my_horse = Horse('mustang', 'wild', 'black')

print(my_horse.horse_color)
print(my_horse.horse_nature)
print(my_horse.horse_gallops())



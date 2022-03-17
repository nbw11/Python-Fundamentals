class Watch:
    def __init__(self, brand, material, type):
        self._brand = brand
        self._material = material
        self._type = type

    def watch_tracks_time(self):
        print(str.format('The {0} tells time.', self._brand))

    def get_brand(self):
        return self._brand

    def set_brand(self, brand_val):
        self._brand = brand_val

    def get_material(self):
        return self._material

    def set_material(self, material_val):
        self._material = material_val

    def get_type(self):
        return self._type

    def set_type(self, type_val):
        self._type = type_val

    brand = property(get_brand, set_brand)
    material = property(get_material, set_material)
    type = property(get_type, set_type)


my_watch = Watch('rolex', 'gold', 'analog')

print(my_watch.material)
print(my_watch.brand)
print(my_watch.type)
print(my_watch.watch_tracks_time())
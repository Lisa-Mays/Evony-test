import time


class SingletonPreset(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PresetSettings(metaclass=SingletonPreset):
    def __init__(self):
        # Initialize the dictionary as an empty dictionary
        self.my_dict = {}

    def add_item(self, key, item):
        self.my_dict[key] = item

    def remove_item(self, key):
        # Remove an item from the dictionary by its key
        if key in self.my_dict:
            del self.my_dict[key]

    def get_item(self, key):
        # Get an item from the dictionary by its key
        return self.my_dict.get(key)

    def get_all_items(self):
        return self.my_dict

import time


class SingletonBoss(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ListBoss(metaclass=SingletonBoss):
    def __init__(self):
        # Initialize the dictionary as an empty dictionary
        self.my_dict = {}

    def add_item(self, item):
        # Generate a unique key based on item.x and item.y
        key = f"{item['x']}_{item['y']}"

        # Add the item to the dictionary with the generated key
        self.my_dict[key] = item

    def remove_item(self, key):
        # Remove an item from the dictionary by its key
        if key in self.my_dict:
            del self.my_dict[key]

    def update_item(self, key):
        # Remove an item from the dictionary by its key
        if key in self.my_dict:
            self.my_dict[key]['isNew'] = False

    def get_item(self, key):
        # Get an item from the dictionary by its key
        return self.my_dict.get(key)

    def get_all_items(self):
        self.remove_expired_bosses()
        # Get all items in the dictionary
        filtered_items = [item for item in self.my_dict.values() if item['isNew']]
        return sorted(filtered_items, key=self.distance_from_target)

    def distance_from_target(self, boss):
        boss_x, boss_y = boss['x'], boss['y']
        distance = ((boss_x - 623) ** 2 + (boss_y - 642) ** 2) ** 0.5  # TODO Change later
        return distance

    def remove_expired_bosses(self):
        current_time = time.time()
        threshold_time = current_time - (20 * 60)  # 20 minutes threshold

        # Create a list of keys to remove (expired bosses)
        keys_to_remove = [key for key, item in self.my_dict.items() if not item['isNew'] and item.get('timestamp', 0) < threshold_time]

        # Remove the expired bosses
        for key in keys_to_remove:
            del self.my_dict[key]
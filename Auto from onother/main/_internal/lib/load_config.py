import json
import os

class NestedDict:
    def __init__(self, d):
        self._d = d

    def __getattr__(self, attr):
        if attr in self._d:
            if isinstance(self._d[attr], dict):
                return NestedDict(self._d[attr])
            else:
                return self._d[attr]
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attr}'")


class CoordsConfig:
    def __init__(self, config_file):
        # Construct the absolute path to the config file using __file__
        current_dir = os.path.dirname(__file__)
        self.config_file = os.path.join(current_dir, config_file)
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print(f"Config file '{self.config_file}' not found.")
            self.config = None
        except json.JSONDecodeError:
            print(f"Error decoding JSON in '{self.config_file}'.")
            self.config = None

    def get_config(self):
        return self.config

    def __getattr__(self, attr):
        if self.config is not None and attr in self.config:
            return NestedDict(self.config[attr])
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attr}'")
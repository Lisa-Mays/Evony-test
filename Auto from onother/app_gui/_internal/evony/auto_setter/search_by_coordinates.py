import time
import logging

from evony import constants
from lib.load_config import CoordsConfig
from evony.image_checker import ImageChecker
from evony.app_navigator import AppNavigator

class SearchBox:
    def __init__(self, device):
        self.device = device
        self.logger = logging.getLogger(device.serial)
        self.searchConfig = CoordsConfig(constants.COORDINATES_CONFIG_FILE).search_box
        self.image_checker = ImageChecker(device)
        self.app_navigator = AppNavigator(device)

    def enter_coordinates(self, x, y, attempt=1):
        self.logger.info(f"Enter Coordinates {x} {y}")
        self.device.input_tap(self.searchConfig.search_icon.x, self.searchConfig.search_icon.y)  # Tap the search box
        time.sleep(2)
        if self.image_checker.is_search_popup():
            self.input_coordinates(self.searchConfig.x_input.x, self.searchConfig.x_input.y, x)  # Enter X
            self.device.input_tap(self.searchConfig.exit_input.x, self.searchConfig.exit_input.y)  # Tap the search box
            self.input_coordinates(self.searchConfig.y_input.x, self.searchConfig.y_input.y, y)  # Enter Y
            self.device.input_tap(self.searchConfig.exit_input.x, self.searchConfig.exit_input.y)
            self.device.input_tap(self.searchConfig.go_button.x, self.searchConfig.go_button.y)  # Tap search button
            time.sleep(4)
            self.device.input_tap(self.searchConfig.select.x, self.searchConfig.select.y)  # Tap boss in map
            self.logger.info(f"Selected boss: {x} {y}")
            time.sleep(1)
            return True

        # Reset to World map
        self.logger.info("Resetting the screen to World map.")
        self.app_navigator.go_back_main_screen()
        self.app_navigator.go_to_world_map()
        self.logger.info(f"We cannot Enter Coordinates correctly {x} {y}")
        return False

    def input_coordinates(self, x, y, text):
        self.device.input_tap(x, y)
        self.device.shell('input keyevent 67 67 67 67')
        time.sleep(2)
        self.device.input_text(text)
        time.sleep(1)
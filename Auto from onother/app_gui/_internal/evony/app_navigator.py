import time
from evony import constants
from lib.load_config import CoordsConfig
from lib.manage_screen import ManageScreen


class AppNavigator:
    def __init__(self, device):
        self.device = device
        self.manage_screen = ManageScreen(device)
        self.config = CoordsConfig(constants.COORDINATES_CONFIG_FILE).chatting

    def go_back_main_screen(self):
        i = 1
        while True:
            self.device.input_keyevent(4)
            time.sleep(2)
            if self.manage_screen.find_and_tap_button('cancel_quit.png') or i > 5:
                if self.manage_screen.find_and_tap_button('world_map.png', False):
                    self.manage_screen.set_screen(constants.IN_CITY_SCREEN)
                else:
                    self.manage_screen.set_screen(constants.WORLD_MAP_SCREEN)
                break
            i += 1

    def go_to_world_map(self):
        if (self.manage_screen.find_and_tap_button('go_to_city.png', False)
                or self.manage_screen.find_and_tap_button('world_map.png')):
            self.manage_screen.set_screen(constants.WORLD_MAP_SCREEN)
            self.manage_screen.set_step_back(0)
            time.sleep(8)

    def go_to_read_whisper(self):
        self.device.input_tap(self.config.whisper.x, self.config.whisper.y)
        time.sleep(2)
        self.device.input_tap(self.config.tab.x, self.config.tab.y)
        time.sleep(1)
        self.device.input_tap(self.config.first_chat.x, self.config.first_chat.y)
        time.sleep(1)
        self.manage_screen.set_screen(constants.WHISPER_SCREEN)
        self.manage_screen.set_step_back(2)

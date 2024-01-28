import logging
import threading
import time

from evony.auto_setter.boss_setter import BossSetter
from evony.auto_setter.boss_reader import BossReader
from evony.app_navigator import AppNavigator
from evony.image_checker import ImageChecker
from evony.login_manager import LoginManager


class GameService(threading.Thread):
    def __init__(self, device, is_logged_in):
        super(GameService, self).__init__()
        self.is_logged_in = is_logged_in
        self.stop_event = threading.Event()
        self.app_navigator = AppNavigator(device)
        self.boss_reader = BossReader(device)
        self.boss_setter = BossSetter(device)
        self.image_checker = ImageChecker(device)
        self.login_manager = LoginManager(device,  self.is_logged_in)
        self.logger = logging.getLogger(device.serial)

    def stop(self):
        self.is_logged_in.set(False)
        self.stop_event.set()

    def run(self):
        time_restart = time.time() + 3600
        while not self.stop_event.is_set():
            if time.time() > time_restart:
                time_restart = time.time() + 3600
                self.login_manager.reset_game()
            self.login_manager.start_auto()

            if self.is_logged_in.get():
                self.navigate_to_world_map()

            if self.is_logged_in.get():
                self.reading_boss()

            if self.is_logged_in.get():
                self.attack_boss()

            if not self.is_logged_in.get():
                time.sleep(300)

    def navigate_to_world_map(self):
        self.log("Navigating back to the main screen...")
        self.app_navigator.go_back_main_screen()
        self.log("Navigating to the world map...")
        self.app_navigator.go_to_world_map()
        self.log("Navigation to world map completed.")

    def reading_boss(self):
        self.log("Navigating to read whisper...")
        self.app_navigator.go_to_read_whisper()
        self.log("Reading boss in whisper...")
        self.boss_reader.reading_boss()
        self.log("Boss reading process completed.")

    def attack_boss(self):
        self.log("Initiating boss attack...")
        self.boss_setter.start_setter()
        self.log("Boss attack process completed.")

    def log(self, message):
        return self.logger.info(message)

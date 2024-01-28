import logging
import threading
import time
import random

from lib.manage_screen import ManageScreen
from evony.login_manager import LoginManager


class LoginThread(threading.Thread):
    def __init__(self, device, is_logged_in):
        super(LoginThread, self).__init__()
        self.is_logged_in = is_logged_in
        self.stop_event = threading.Event()
        self.manage_screen = ManageScreen(device)
        self.logger = logging.getLogger(device.serial)
        self.login_manager = LoginManager(device)

    def run(self):
        while not self.stop_event.is_set():
            restart_game = self.manage_screen.find_and_tap_button('restart_btn.png', False)
            self.is_logged_in.set(not restart_game)
            self.logger.info(f"Check Login {not restart_game}")
            if restart_game:
                time.sleep(20)
                self.login_manager.reset_game()
                time.sleep(20)
                self.is_logged_in.set(True)

            time.sleep(4)

    def stop(self):
        self.stop_event.set()

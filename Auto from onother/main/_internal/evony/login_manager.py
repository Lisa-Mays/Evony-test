import subprocess
import time
import logging
import xml.etree.ElementTree as ET

from evony.image_checker import ImageChecker


class LoginManager:
    def __init__(self, device,  is_logged_in):
        self.device = device
        self.img_checker = ImageChecker(device)
        self.logger = logging.getLogger(device.serial)
        self.is_logged_in = is_logged_in

    def start_game(self):
        if not self.is_game_running():
            self.logger.info("Starting game...")
            self.launch_game()
            time.sleep(10)

    def start_auto(self):
        self.start_game()
        self.is_logged_in.set(False)
        self.logger.info("Checking Login...")
        while self.img_checker.is_loading_game():
            self.logger.info("Loading game...")
            time.sleep(20)
            self.is_logged_in.set(True)
        for attempt in range(1, 10):
            self.device.input_keyevent(4)
            time.sleep(2)
            if self.img_checker.is_cancel_button():
                time.sleep(1)
                self.device.input_tap(490, 730)
                time.sleep(2)
                if self.img_checker.is_no_alliance():
                    self.reset_game()
                    time.sleep(60)
                self.device.input_keyevent(4)
                self.is_logged_in.set(True)
                break
            if attempt >= 9:
                self.logger.info("We will try to reset the game")
                self.reset_game()
                time.sleep(300)
                self.start_auto()
                break
        self.logger.info("Done...")
        return True

    def is_loading_screen(self):
        return self.img_checker.is_loading_game()

    def restart_screen(self):
        return self.img_checker.is_restart_screen()

    def is_game_running(self):
        return self.get_current_package_name() == 'com.topgamesinc.evony'

    def reset_game(self):
        self.quit_game()
        time.sleep(5)
        self.launch_game()
        time.sleep(60)

    def launch_game(self):
        try:
            self.device.shell(
                'am start -n "com.topgamesinc.evony/com.topgamesinc.androidplugin.UnityActivity" -a android.intent.action.MAIN -c android.intent.category.LAUNCHER')
            self.logger.info("Starting Evony...")
        except Exception as e:
            self.logger.info("Error launching the game:", e)

    def quit_game(self, package_name="com.topgamesinc.evony"):
        try:
            self.device.shell(f'am force-stop {package_name}')
            self.logger.info("Quitting Evony...")
        except Exception as e:
            self.logger.info(f"Failed to kill process with packages: {e}")

    def get_current_package_name(self):
        try:
            result = self.device.shell('uiautomator dump')
            if "UI hierchary dumped to:" in result:
                # Extract the temporary file path from the output
                dump_path = result.split("UI hierchary dumped to:")[1].strip()
                xml_content = self.device.shell(f'cat {dump_path}')
                root = ET.fromstring(xml_content)

                for node in root.iter('node'):
                    package_name = node.get('package')
                    if package_name:
                        return package_name

        except Exception as e:
            self.logger.info("Error getting the current package name:", e)

        return None

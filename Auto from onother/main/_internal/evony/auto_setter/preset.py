import cv2
import pytesseract
import time
import logging

from lib.manage_screen import ManageScreen
from lib.load_config import CoordsConfig
from evony import constants

class Preset:
    def __init__(self, device):
        self.device = device
        self.preset_config = CoordsConfig(constants.PRESET_CONFIG_FILE)
        self.crop_config = CoordsConfig(constants.CROP_IMAGE_CONFIG_FILE).march_time
        self.manage_screen = ManageScreen(device)
        self.logger = logging.getLogger(device.serial)
        self.presets = {}
        self.init_preset()

    def init_preset(self):
        preset_config = self.preset_config.get_config()
        self.presets = {
            preset_number: {
                "timestamp": time.time(),
                "priority": settings['priority'],
                "mode": settings['mode']
            }
            for preset_number, settings in preset_config.items()
            if settings['active']
        }
        self.presets = dict(sorted(self.presets.items(), key=lambda x: x[1]["priority"]))

    def get_preset_for_boss(self, boss_name):
        available_preset = self.get_available_preset()
        preset_config = self.preset_config.get_config()

        for preset_number, value in available_preset.items():
            if boss_name in preset_config[preset_number]['bosses']:
                self.logger.info(f"Preset {preset_number} is available for boss {boss_name}")
                return preset_number

        return False

    def get_preset_setting(self, preset_number):
        return self.presets[preset_number]

    def set_preset_time(self, preset, is_rally=False):
        timestamp = time.time() + self.get_finish_time()
        if is_rally:
            timestamp += 300
        self.presets[preset]['timestamp'] = timestamp

    def get_available_preset(self):
        current = time.time()
        presets = {}
        for key, preset in self.presets.items():
            if preset['timestamp'] < current:
                presets[key] = True
        return presets

    def get_finish_time(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        x, y, width, height = self.crop_config.x, self.crop_config.y, self.crop_config.width, self.crop_config.height
        march_time_image = self.manage_screen.crop_screenshot(x, y, width, height)
        gray_image = cv2.cvtColor(march_time_image, cv2.COLOR_BGR2GRAY)

        # Perform text extraction
        time_str = pytesseract.image_to_string(gray_image, lang='eng',
                                                      config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')

        # Split the string into hours, minutes, and seconds
        hours = int(time_str[:2])
        minutes = int(time_str[2:4])
        seconds = int(time_str[4:])

        # Calculate the total seconds
        total_seconds = (hours * 3600 + minutes * 60 + seconds) * 2 + 5  # Adding 5 secs to avoid lagging time
        self.logger.info(f"Time march to boss: {total_seconds}")

        return min(total_seconds, 1000)

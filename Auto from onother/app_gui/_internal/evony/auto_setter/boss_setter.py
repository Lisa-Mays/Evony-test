import time
import logging

from evony import constants
from lib.load_config import CoordsConfig
from evony.auto_setter.list_boss import ListBoss
from evony.auto_setter.search_by_coordinates import SearchBox
from evony.auto_setter.preset import Preset
from evony.image_checker import ImageChecker

class BossSetter:
    def __init__(self, device):
        self.device = device
        self.config = CoordsConfig(constants.COORDINATES_CONFIG_FILE).get_config()['boss_setter']
        self.list_boss = ListBoss()
        self.search_box = SearchBox(device)
        self.preset = Preset(device)
        self.logger = logging.getLogger(device.serial)
        self.current_boss = '000_000'
        self.image_checker = ImageChecker(device)
        self.boss_name = ''
        self.is_rally_mode = False

    def start_setter(self):
        list_boss = self.list_boss.get_all_items()
        for boss in list_boss:
            if not self.preset.get_available_preset():
                self.logger.info(f"All presets are busy...")
                break
            self.current_boss = f"{boss['x']}_{boss['y']}"
            self.boss_name = f"{boss['name']}-{boss['level']}".lower()
            preset = self.preset.get_preset_for_boss(self.boss_name)
            if preset is not False:
                self.logger.info(f"We are going to enter coordinates for {self.boss_name}")
                if self.search_box.enter_coordinates(boss['x'], boss['y']):
                    can_attack = self.process_preset(preset)
                    self.handle_after_preset_actions(preset, can_attack)
            else:
                self.logger.info(f"We have no preset available for boss {self.boss_name}")

        if len(self.list_boss.get_all_items()) > 10:
            time.sleep(10)
            self.start_setter()

    def process_preset(self, preset):
        preset_setting = self.preset.get_preset_setting(preset)
        self.is_rally_mode = preset_setting['mode'] == 'rally'
        if self.is_rally_mode:
            self.logger.info(f"We are going to rally boss: {self.boss_name}")
            return self.rally_mode()
        else:
            self.logger.info(f"We are going to solo boss: {self.boss_name}")
            return self.solo_mode()

    def handle_after_preset_actions(self, preset, can_attack):
        if not can_attack:
            self.logger.info(f"We can't attack boss {self.boss_name} at the moment. We will try it later")
            return
        self.device.input_tap(self.config[preset]['x'], self.config[preset]['y'])  # Tap preset
        time.sleep(2)
        if self.image_checker.general_available():
            self.preset.set_preset_time(preset, self.is_rally_mode)
            self.device.input_tap(self.config['march_btn']['x'], self.config['march_btn']['y'])
            self.logger.info('We are killing boss: ' + self.boss_name)
            self.list_boss.update_item(self.current_boss)
            if self.is_rally_mode is False:
                time.sleep(2)
                self.device.input_tap(self.config['after_solo']['x'], self.config['after_solo']['y'])
        else:
            self.logger.info(f"We have no general for preset {preset}, boss {self.boss_name}. We will try it later.")
            self.device.input_keyevent(4)
            if self.is_rally_mode:
                self.device.input_keyevent(4)
        time.sleep(2)

    def solo_mode(self):
        return self.is_boss_exist() and self.image_checker.solo_button() and self.image_checker.march_interface()

    def rally_mode(self):
        if self.is_boss_exist() and self.image_checker.rally_button():
            self.device.input_tap(self.config['5min_btn']['x'], self.config['5min_btn']['y'])  # Tap rally 5 min Button
            time.sleep(2)

            if self.image_checker.rally_interface():
                return True

        return False

    def is_boss_exist(self):
        if not self.image_checker.boss_available():
            self.logger.info(f'Boss {self.boss_name} has vanished.')
            self.list_boss.update_item(self.current_boss)
            return False

        return True

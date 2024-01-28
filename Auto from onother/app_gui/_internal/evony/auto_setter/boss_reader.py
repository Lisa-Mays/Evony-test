import time
import cv2
import pytesseract
import re
import logging

from evony.auto_setter.list_boss import ListBoss
from lib.manage_screen import ManageScreen
from evony.image_checker import ImageChecker, LoginFailedException
from evony import constants


class BossReader:
    def __init__(self, device):
        self.device = device
        self.image_checker = ImageChecker(device)
        self.screenshot = ManageScreen(device)
        self.logger = logging.getLogger(device.serial)
        self.boss_pattern = r'(Lv(\d+)(.*?)(?=Lv\d+|$))'

    def reading_boss(self):
        self.extract_bosses()

        for seq in range(15):
            self.swipe_whisper(500, 200)
            boss_list = self.extract_bosses()
            if len(boss_list) < 1:
                break
        self.step_back()

    def swipe_whisper(self, x, y):
        self.device.input_swipe(x, y, x, y + 600, 1000)

    def extract_time_in_minutes(self, time_string):
        if "min" in time_string:
            return int(re.search(r'(\d+)min', time_string).group(1))
        elif "secs" in time_string:
            return 10
        else:
            return 1000

    def process_boss_match(self, match):
        name_match = re.search(r'(\w+\(\w+\)|\w+)(\(K:(\d+)X:(\d+),Y:(\d+)\))', match[2])
        shared_minutes = self.extract_time_in_minutes(match[2])

        if name_match and shared_minutes <= 15:
            return {
                'level': int(match[1]),
                'name': name_match.group(1).replace("(", "").replace(")", "").replace("Troop", ""),
                'x': int(name_match.group(4)),
                'y': int(name_match.group(5)),
                'timestamp': int(time.time()),
                'isNew': True
            }
        return None

    def step_back(self):
        step_back = self.screenshot.get_step_back()
        for step in range(step_back):
            self.device.input_keyevent(4)
            time.sleep(2)

    def extract_bosses(self):
        pytesseract.pytesseract.tesseract_cmd = constants.TESSERACT_CMD_PATH
        image = self.image_checker.get_screenshot(True)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        equalized_image = cv2.equalizeHist(gray_image)
        blurred_image = cv2.GaussianBlur(equalized_image, (5, 5), 0)
        extracted_text = pytesseract.image_to_string(blurred_image)
        extracted_text = extracted_text.replace("just now", "10 secs ago")

        # Define a regex pattern to match lines starting with "shared Coordinates"
        pattern = r"shared Coordinates:(.*?)ago"
        matches = re.findall(pattern, extracted_text, re.DOTALL)
        output = ''.join(matches)
        output_text = ''.join(output.split())
        matches = re.findall(self.boss_pattern, output_text)
        boss_info = [self.process_boss_match(match) for match in matches if self.process_boss_match(match)]

        list_boss = ListBoss()
        for boss in boss_info:
            if list_boss.get_item(f"{boss['x']}_{boss['y']}") is None:
                list_boss.add_item(boss)
                self.logger.info(f"We have added boss {boss} to queue")

        return boss_info

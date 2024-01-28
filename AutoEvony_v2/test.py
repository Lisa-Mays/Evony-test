from asyncio import constants
from ppadb.client import Client as AdbClient
import cv2
import numpy as np
from PIL import Image
import io
import os
import time


class SingletonScreen(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class ManageScreen(metaclass=SingletonScreen):
    def __init__(self, device):
        self.device = device
        self.value = None
        self.step_back = 0

    def find_and_tap_button(self, image, is_tap=True, screenshot=None):
        template_path = os.path.join(constants.IMAGE_DIR, image)
        x, y = self.get_image_coordinates(template_path, screenshot)
        if x is not False:
            if is_tap is True:
                self.device.input_tap(x, y)
            time.sleep(2)
            return True
        return False

    def crop_screenshot(self, x, y, width, height):
        return self.get_screenshot()[y:y+height, x:x+width]

    def get_screenshot(self):
        screenshot_stream = io.BytesIO(self.device.screencap())
        screenshot_pil = Image.open(screenshot_stream)
        return cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2BGR)

    def get_image_coordinates(self, template_path, screenshot):
        if screenshot is None:
            screenshot = self.get_screenshot()
        template_image = cv2.imread(template_path)
        height, width = template_image.shape[:2]

        # Perform template matching
        result = cv2.matchTemplate(screenshot, template_image, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to determine matches
        threshold = 0.90
        locations = np.where(result >= threshold)
        # Get the coordinates of matched regions
        matched_coordinates = list(zip(*locations[::-1]))

        if matched_coordinates:
            # Calculate the center coordinates of the matched region
            x = matched_coordinates[0][0] + width // 2
            y = matched_coordinates[0][1] + height // 2
            return x, y
        else:
            return False, False



# # Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("127.0.0.1:5555")



a = ManageScreen(device)
start_time = time.time()
screen_capturer = a.get_screenshot()
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time} seconds")
cv2.imshow('Screenshot', screen_capturer)
cv2.waitKey(0)
cv2.destroyAllWindows()



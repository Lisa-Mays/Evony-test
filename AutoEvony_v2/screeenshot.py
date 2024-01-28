import subprocess
import cv2
import numpy as np
import os
import time as tm
import io
from PIL import Image
from ppadb.client import Client as AdbClient

class Auto:
    def __init__(self, ip='127.0.0.1', portt=''):
        client = AdbClient(host=ip, port=5037)
        self.device = client.device(ip + ":" + str(portt))
        self.ip = ip
        self.port = portt
        self.pwd = 'cd android'
        # Connect to the device
        subprocess.run(f'{self.pwd} && adb connect {self.ip}:{self.port}', shell=True)     

    def screen_capture(self):
        # Capture the screen
        start_time = tm.time()
        screenshot_stream = io.BytesIO(self.device.screencap())
        screenshot_pil = Image.open(screenshot_stream)
        end_time = tm.time()
        execution_time = end_time - start_time
        print(f"{self.port} Thời gian thực thi chụp ảnh là {execution_time} giây.")
        return cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2BGR)

    def find_img(self, img,screenshot, threshold=0.9, num_positions=1):
        if os.path.exists(img):
            template = cv2.imread(img)
            result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
            height, width = result.shape[:2]
            loc = np.where(result >= threshold)
            positions = list(zip(*loc[::-1]))[:num_positions]

            if positions:
                return positions
            else:
                return [(0,0)]    
    
    def click(self, x, y):
        self.device.input_tap(x, y)
        
    def swipe(self, x1, y1, x2, y2, duration=1000):
        self.device.input_swipe(x1, y1, x2, y2,duration)
    
    def esc(self):
        self.device.input_keyevent("111")

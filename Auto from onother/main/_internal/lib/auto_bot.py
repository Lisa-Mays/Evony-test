import logging
import threading
import time

from ppadb.client import Client as AdbClient
from evony.game_service import GameService
from evony.login import LoginThread


class DataStore:
    def __init__(self, data=False):
        self.data = data

    def set(self, data):
        self.data = data

    def get(self):
        return self.data


class AutoBot(threading.Thread):
    def __init__(self, device_port):
        super(AutoBot, self).__init__()
        self.stop_event = threading.Event()
        self.port = device_port
        self.device = self.init_device(device_port)
        self.logger = logging.getLogger(self.device.serial)
        self.is_logged_in = DataStore()
        self.game_service = GameService(self.device, self.is_logged_in)
        self.game_service.daemon = True

    def init_device(self, device_port):
        client = AdbClient(host="127.0.0.1", port=5037)
        return client.device(device_port)

    def run(self):
        if time.time() < 1698598800:
            self.game_service.start()
            self.game_service.join()

    def start_again(self):
        self.game_service = GameService(self.device, self.is_logged_in)
        self.game_service.start()

    def stop(self):
        self.stop_event.set()
        self.game_service.stop()

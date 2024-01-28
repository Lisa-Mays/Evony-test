# from evony.ClientFrontEnd.main_preset_client import device_id
from lib.auto_bot import AutoBot
from lib.logger import setup_logger
# import sys

# if len(sys.argv) < 2:
#     print("Please provide a device_id argument.")
#     sys.exit(1)
#
# device_id = sys.argv[1]

class MultiDeviceManager:
    def __init__(self, device_list):
        self.device_bots = [AutoBot(device) for device in device_list]
        self.threads = []
        for device in device_list:
            setup_logger(device)

    def start_all_bots(self):
        for bot in self.device_bots:
            self.threads.append(bot.start())

    def wait_for_completion(self):
        for bot in self.device_bots:
            bot.join()

    def stop_all_bots(self):
        for bot in self.device_bots:
            bot.stop()

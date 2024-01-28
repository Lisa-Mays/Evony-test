import os

IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
COORDINATES_CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config/coordinates.json")
PRESET_CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config/preset.json")
BOSSES_CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config/bosses.json")
CROP_IMAGE_CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config/crop_image.json")
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "var/debug.log")
TESSERACT_CMD_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Tesseract/tesseract.exe")

IN_CITY_SCREEN = 'in_city'
WORLD_MAP_SCREEN = 'world_map'
ATK_BOSS_SCREEN = 'atk_boss'
WHISPER_SCREEN = 'whisper'

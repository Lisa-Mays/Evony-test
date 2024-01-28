import logging
from evony.auto_setter.preset import Preset
from lib.logger import setup_logger

setup_logger()

logging.getLogger("evony").info("Test")

# device = True
#
# preset = Preset(device)
#
# preset_name = preset.get_preset_for_boss('5-warlord')
# preset.get_preset_setting(preset_name)
# # preset.get_finish_time()
#
#
# presets = {
#     1: {"timestamp": 1634472000.0, "priority": 2},
#     2: {"timestamp": 1634471000.0, "priority": 1},
#     3: {"timestamp": 1634473000.0, "priority": 3},
# }
#
# sorted_presets = dict(sorted(presets.items(), key=lambda x: x[1]["priority"]))

# for preset_number, preset_data in sorted_presets.items():
#     print(f"Preset {preset_number}: {preset_data}")

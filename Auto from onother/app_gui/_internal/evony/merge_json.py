import json

merged_data = {}
file_list = ['config/Preset_1.json', 'config/Preset_2.json',
             'config/Preset_3.json', 'config/Preset_4.json',
             'config/Preset_5.json', 'config/Preset_6.json',
             'config/Preset_7.json', 'config/Preset_8.json']

for file_path in file_list:
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)
        merged_data.update(json_data)

# Use the merged_data list as needed
print(merged_data)
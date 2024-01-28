from evony.auto_setter import BossReader
from evony.auto_setter import ListBoss
from ppadb.client import Client as AdbClient

# # Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("127.0.0.1:21583")

boss_reader = BossReader(device)
# Print the extracted text
boss_reader.reading_boss()
print(ListBoss().get_all_items())
# result = device.screencap()
# with open("main.png", "wb") as fp:
#     fp.write(result)
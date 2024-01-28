import pytesseract

from evony import Preset
from ppadb.client import Client as AdbClient

# # Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("127.0.0.1:21583")

# Set the path to your Tesseract executable (adjust this to your Tesseract installation)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


# x, y, width, height =  360, 922, 90, 25
# cropped_image = screen.crop_screenshot(x, y, width, height)
# gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)


# Use pytesseract to perform OCR on the thresholded image
# text = pytesseract.image_to_string(gray_image, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')

preset = Preset(device)
time = preset.get_finish_time()
# Print the extracted text
print(time)

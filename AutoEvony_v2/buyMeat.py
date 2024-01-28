from time import sleep
import subprocess
from screeenshot import Auto
from numpy import ndarray
from PyQt5.QtWidgets import QApplication,QMessageBox

class RunAuto2():
    def __init__(self,exitFlag,port,ip) -> None:
        self.port = port
        self.ip = ip
        self.sc = Auto(self.ip,self.port)
        self.exitFlag = exitFlag
        
        self.buyMeat = ".\\img\\buyMeat.png"
        self.xacnhan = ".\\img\\xacnhanmuaMEat.png"
        self.choden = ".\\img\\choden.png"
        while not self.exitFlag.is_set():
            while not self.exitFlag.is_set():
                screenshot = self.sc.screen_capture()
                if not isinstance(screenshot, ndarray):
                    self.errorOut(1)
                
                position = self.sc.find_img(self.choden,screenshot, 0.9, 1)
                if position[0][0]== 0 and position[0][1] == 0:
                    sleep(3)
                    break
                
                position = self.sc.find_img(self.xacnhan,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(1)
                    break
                
                position = self.sc.find_img(self.buyMeat,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1]+102)
                    sleep(1)
                    break
                else:
                    self.sc.click(272,791)
                    sleep(3)
        self.errorOut()
    
    def errorOut(self,type=0):
        # Tạo một hộp thoại thông báo lỗi
        if type == 1:
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Critical)
            error_message.setWindowTitle(f"Acc Count Error {self.port}")
            error_message.setText("Mất kết nối!!")
            error_message.setInformativeText(f"Cổng {self.port} mất kết nối!!!")
            error_message.setStandardButtons(QMessageBox.Ok)
            error_message.exec()
        
        subprocess.Popen(f'cd android && adb disconnect {self.ip}:{self.port}', shell=True)
        exit()
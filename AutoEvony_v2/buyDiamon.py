from time import sleep
import subprocess
from screeenshot import Auto
from numpy import ndarray
from PyQt5.QtWidgets import QApplication,QMessageBox

class RunAuto3():
    def __init__(self,exitFlag,port,ip) -> None:
        self.port = port
        self.ip = ip
        self.sc = Auto(self.ip,self.port)
        self.exitFlag = exitFlag
        
        self.da500 = ".\\img\\Datim\\500Kc.png"
        self.da1000 = ".\\img\\Datim\\1000Kc.png"
        self.da2000 = ".\\img\\Datim\\2000Kc.png"
        self.da5000 = ".\\img\\Datim\\5000Kc.png"
        
        self.xu500 = ".\\img\\XuVang\\500Kc.png"
        self.xu1000 = ".\\img\\XuVang\\1000Kc.png"
        self.xu2000 = ".\\img\\XuVang\\2000Kc.png"
        self.xu5000 = ".\\img\\XuVang\\5000Kc.png"
        
        self.xacnhan = ".\\img\\xacnhanmuaMEat.png"
        self.chokimcuong = ".\\img\\chokimcuong.png"
        while not self.exitFlag.is_set():
            while not self.exitFlag.is_set():
                screenshot = self.sc.screen_capture()
                if not isinstance(screenshot, ndarray):
                    self.errorOut(1)
                
                position = self.sc.find_img(self.chokimcuong,screenshot, 0.9, 1)
                if position[0][0]== 0 and position[0][1] == 0:
                    sleep(3)
                    break
                
                position = self.sc.find_img(self.xacnhan,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(3)
                    break
                
                position = self.sc.find_img(self.da500,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    print("500kc da")
                    self.sc.click(position[0][0],position[0][1]+100)
                    sleep(1)
                    break
                
                position = self.sc.find_img(self.da1000,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    print("1000kc da")
                    self.sc.click(position[0][0],position[0][1]+100)
                    sleep(1)
                    break
                
                position = self.sc.find_img(self.da2000,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    print("2000kc da")
                    self.sc.click(position[0][0],position[0][1]+100)
                    sleep(1)
                    break
                
                position = self.sc.find_img(self.da5000,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    print("5000kc da")
                    self.sc.click(position[0][0],position[0][1]+100)
                    sleep(1)
                    break
                
                position = self.sc.find_img(self.xu500,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    print("500kc xu")
                    self.sc.click(position[0][0],position[0][1]+100)
                    sleep(1)
                    break
                
                position = self.sc.find_img(self.xu1000,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    print("1000kc xu")
                    self.sc.click(position[0][0],position[0][1]+100)
                    sleep(1)
                    break
                
                position = self.sc.find_img(self.xu2000,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    print("2000kc xu")
                    self.sc.click(position[0][0],position[0][1]+100)
                    sleep(1)
                    break
                
                position = self.sc.find_img(self.xu5000,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    print("5000kc xu")
                    self.sc.click(position[0][0],position[0][1]+100)
                    sleep(1)
                    break
                
                self.sc.click(272,827)
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
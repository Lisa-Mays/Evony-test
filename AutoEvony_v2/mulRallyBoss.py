# $ADB_LOCAL_TRANSPORT_MAX_PORT
import sys
from time import sleep
import subprocess
from screeenshot import Auto
from numpy import ndarray
from PyQt5.QtWidgets import QApplication,QMessageBox

class RunAuto():
    def __init__(self,exitFlag,port,ip,setting) -> None:
        self.port = port
        self.ip = ip
        self.sc = Auto(self.ip,self.port)
        self.exitFlag = exitFlag
        
        self.boss = {}
        self.setting={}
        for key, value in setting.items():
            if value is not None:
                if key != "champ" and key != "meat":
                    if value == "Chạy Hết":
                        self.boss[key] = 0
                    else:
                        self.boss[key] = value
                        
                else:
                    self.setting[key] = value

        # ====================image==========================
        self.game = ".\\img\\login\\game.png"
        self.notUpdate = ".\\img\\login\\notUpdate.png"
        self.inRungame = ".\\img\\login\\inRungame.png"
        self.gif = ".\\img\\login\\gif.png"
        self.notUpdate = ".\\img\\login\\notUpdate.png"
        self.LienMinh = ".\\img\\login\\alliance.png"
        self.relogin = ".\\img\\login\\relogin.png"
        self.toMuchESC = ".\\img\\outAlliance\\toMuchESC.png"
        self.HienGoiNap = ".\\img\\outAlliance\\HienGoiNap.png"
        self.close1 = ".\\img\\outAlliance\\close1.png"
        self.close2 = ".\\img\\outAlliance\\close2.png"
        
        self.inAlliance = ".\\img\\inAlliance\\alliance.png"
        self.goWar = ".\\img\\inAlliance\\goWar.png"
        
        self.InWarAlliance = ".\\img\\inAlliance\\waralliance.png"
        self.warChamp = ".\\img\\inAlliance\\warChamp.png"
        self.thamgia = ".\\img\\inWar\\thamgia.png"
        self.thamgia2 = ".\\img\\inWar\\thamgia2.png"
        self.select1 = ".\\img\\inWar\\select1.png"
        self.checkselect1 = ".\\img\\inWar\\checkselect1.png"
        self.champ1 = ".\\img\\inWar\\champ1.png"
        self.champ2 = ".\\img\\inWar\\champ2.png"
        self.choseChamp = ".\\img\\inWar\\choseChamp.png"
        self.chontuong = ".\\img\\inWar\\chontuong.png"
        self.flag2 = ".\\img\\inWar\\flag2.png"
        self.flag3 = ".\\img\\inWar\\flag3.png"
        self.reback = ".\\img\\inWar\\reback.png"
        self.up = ".\\img\\inWar\\up.png"
        self.up2 = ".\\img\\inWar\\up2.png"
        self.PVP = ".\\img\\inAlliance\\PVP.png"
        self.eatMeat = ".\\img\\inWar\\eatMeat.png"
        self.callBack2 = ".\\img\\callBack2.png"
        self.callBack3 = ".\\img\\callBack3.png"
        
        self.inKhodo = ".\\img\\inKhodo\\khodo.png"
        self.getMeat = ".\\img\\inKhodo\\200KC.png"
        self.tickmeat = ".\\img\\inKhodo\\tickmeat.png"
        
        self.error1 = "./img/error/error1.png"
        self.error2 = "./img/error/error2.png"
        
        self.updown = 1
        self.clickselect1 = 0
        # ====================position==========================
        self.positionAlliance = 0
        # ==============================================
         
        while not self.exitFlag.is_set():
            if not self.positionAlliance:
                self.OutAlliance()
            elif self.positionAlliance == 1:
                self.InAlliance()
            elif self.positionAlliance == 2:
                self.InWar()
            elif self.positionAlliance == 3:
                self.InKhoDO()
            
            sleep(1)
        self.errorOut()
        
    def CheckPosition(self,screenshot):
        position = self.sc.find_img(self.relogin,screenshot, 0.9, 1)
        if position[0][0]!= 0 and position[0][1] != 0:
            print(f"Acc:{self.port} đăng nhập lại, đợi 30s !!!!!!")
            self.sc.click(position[0][0],position[0][1])
            self.positionAlliance = 0
            sleep(30)
            return
        
        position = self.sc.find_img(self.inAlliance,screenshot, 0.9, 1)
        if position[0][0] != 0 and position[0][1] != 0:
            self.positionAlliance = 1
            return 
        
        position = self.sc.find_img(self.InWarAlliance,screenshot, 0.9, 1)
        position2 = self.sc.find_img(self.warChamp,screenshot, 0.9, 1)
        if (position[0][0] != 0 and position[0][1]) != 0 or (position2[0][0] != 0 and position2[0][1]):
            self.positionAlliance = 2
            return
        
        position = self.sc.find_img(self.inKhodo,screenshot, 0.9, 1)
        if (position[0][0] != 0 and position[0][1] != 0):
            self.positionAlliance = 3
            return
     
        self.positionAlliance = 0
        
    def OutAlliance(self):
        while not self.exitFlag.is_set():
            while not self.exitFlag.is_set():
                screenshot = self.sc.screen_capture()
                if not isinstance(screenshot, ndarray):
                    self.errorOut(1)        

                self.CheckPosition(screenshot)
                if self.positionAlliance:
                    sleep(2)
                    return
                
                position = self.sc.find_img(self.game,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    print(f"Acc:{self.port} đăng nhập, đợi 30s !!!!!!")
                    sleep(30)
                    break
                
                position = self.sc.find_img(self.notUpdate,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(2)
                    break
                
                position = self.sc.find_img(self.inRungame,screenshot, 0.8, 1) 
                if position[0][0]!= 0 and position[0][1] != 0:
                    print(f"Acc:{self.port} đang vào game, đợi 10s !!!!!!")
                    sleep(10)
                    break
                
                position = self.sc.find_img(self.gif,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(2)
                    break
                
                position = self.sc.find_img(self.toMuchESC,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(2)
                    break
                
                position = self.sc.find_img(self.HienGoiNap,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.esc()
                    sleep(2)
                    break
                
                position = self.sc.find_img(self.error1,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.esc()
                    sleep(2)
                    break
                
                position = self.sc.find_img(self.close1,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(2)
                    break
                
                position = self.sc.find_img(self.close2,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(2)
                    break
                
                position = self.sc.find_img(self.LienMinh,screenshot, 0.8, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(2)
                    break
                self.sc.esc()
                sleep(2)
    def InAlliance(self):
        while not self.exitFlag.is_set():
            while not self.exitFlag.is_set():
                screenshot = self.sc.screen_capture()
                if not isinstance(screenshot, ndarray):
                    self.errorOut(1)

                self.CheckPosition(screenshot)
                if self.positionAlliance != 1:
                    sleep(2)
                    return
                
                position = self.sc.find_img(self.HienGoiNap,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.esc()
                    sleep(2)
                    break
                
                position = self.sc.find_img(self.error1,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.esc()
                    sleep(2)
                    break
                
                position = self.sc.find_img(self.goWar,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(1)
                    break
                sleep(3)
        self.errorOut()
    def InWar(self):
        while not self.exitFlag.is_set():
            while not self.exitFlag.is_set():
                screenshot = self.sc.screen_capture()
                if not isinstance(screenshot, ndarray):
                    self.errorOut(1)
                
                self.CheckPosition(screenshot)
                if self.positionAlliance != 2:
                    sleep(2)
                    return
                
                position = self.sc.find_img(self.error2,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.esc()
                    sleep(2)
                    break
                
                position = self.sc.find_img(self.HienGoiNap,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.esc()
                    sleep(2)
                    break
                
                position = self.sc.find_img(self.error1,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.esc()
                    sleep(2)
                    break
                
                position = self.sc.find_img(self.thamgia2,screenshot, 0.9, 1)
                if position[0][0] != 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(2)
                    break
                position = self.sc.find_img(self.thamgia,screenshot, 0.9, 1)
                if position[0][0] != 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(2)
                    break
                else:
                    position = self.sc.find_img(self.reback,screenshot, 0.99, 1)
                    if position[0][0]!= 0 and position[0][1] != 0:
                        self.updown = 0
                        sleep(1)
                    position = self.sc.find_img(self.up,screenshot, 0.99, 1)
                    if position[0][0]!= 0 and position[0][1] != 0:
                        self.updown = 1
                        sleep(1)      
                    position = self.sc.find_img(self.up2,screenshot, 0.99, 1)
                    if position[0][0]!= 0 and position[0][1] != 0:
                        self.updown = 1
                        sleep(1)  
                         
                    position = self.sc.find_img(self.PVP,screenshot, 0.9, 1)
                    if position[0][0]!= 0 and position[0][1] != 0:
                        self.sc.click(position[0][0],position[0][1])
                        # if self.updown == 1:
                        #     self.sc.swipe(300, 500, 300, 180,3000)
                        # else:
                        #     self.sc.swipe(300, 553, 300,873 ,3000)
                        sleep(1)
                        break
                         
                
                position = self.sc.find_img(self.callBack2,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.esc()
                    sleep(2)
                    break
                    
                position = self.sc.find_img(self.callBack3,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.esc()
                    sleep(2)
                    break
                    
                position = self.sc.find_img(self.select1,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.clickselect1 += 1
                    if self.clickselect1 >= 4:
                        self.sc.esc()
                        self.clickselect1 = 0
                        sleep(2)
                        break
                    else:
                        self.sc.click(position[0][0]+50,position[0][1])
                        sleep(2)
                        break
                
                position = self.sc.find_img(self.eatMeat,screenshot, 0.8, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(2)
                    break
                
                position = self.sc.find_img(self.checkselect1,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    if  self.setting["champ"] > 0:
                        position = self.sc.find_img(self.champ1,screenshot, 0.99, 1)
                        if position[0][0]!= 0 and position[0][1] != 0:
                            self.sc.click(position[0][0],position[0][1])
                            sleep(2)
                            break
                        if self.setting["champ"] >= 2:
                            position = self.sc.find_img(self.champ2,screenshot, 0.99, 1)
                            if position[0][0]!= 0 and position[0][1] != 0:
                                self.sc.click(position[0][0],position[0][1])
                                sleep(2)
                                break
                        
                    position = self.sc.find_img(self.flag2,screenshot, 0.9, 1)
                    if position[0][0]!= 0 and position[0][1] != 0:
                        self.sc.click(461,923)
                        self.clickselect1 = 0
                        sleep(2)
                        break
                    
                    position = self.sc.find_img(self.flag3,screenshot, 0.9, 1)
                    if position[0][0]!= 0 and position[0][1] != 0:
                        self.sc.esc()
                        self.clickselect1 = 0
                        sleep(2)
                        break
                
                position = self.sc.find_img(self.choseChamp,screenshot, 0.95, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(2)
                    break
                else:
                    position = self.sc.find_img(self.chontuong,screenshot, 0.9, 1)
                    if position[0][0]!= 0 and position[0][1] != 0:
                        print("esc")
                        self.sc.esc()
                        sleep(2)
                        print("click")
                        self.sc.click(461,923)
                        sleep(3)
                        break
                    
                sleep(3)
    def InKhoDO(self):
        while not self.exitFlag.is_set():
            while not self.exitFlag.is_set():
                screenshot = self.sc.screen_capture()
                if not isinstance(screenshot, ndarray):
                    self.errorOut(1)
                
                self.CheckPosition(screenshot)
                if self.positionAlliance != 3:
                    return
                
                position = self.sc.find_img(self.tickmeat,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    for i in range(1,self.setting["meat"]):
                        self.sc.click(position[0][0],position[0][1])
                        sleep(1)
                    self.sc.click(330,687)
                    sleep(5)
                    self.sc.esc()
                    break
                
                position = self.sc.find_img(self.getMeat,screenshot, 0.9, 1)
                if 320<position[0][1]<470:
                    self.sc.click(449,555)
                    sleep(2)
                    break
                elif position[0][1]==0 or position[0][1]>470:
                    self.sc.click(449,390)
                    sleep(2)
                    break
                
                sleep(3)
                
    
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
        sys.exit()

        
# adb disconnect 127.0.0.1:5553
# error: no such device '127.0.0.1:5553'




#320 - 470
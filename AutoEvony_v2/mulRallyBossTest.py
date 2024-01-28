# $ADB_LOCAL_TRANSPORT_MAX_PORT
from time import sleep
import subprocess
from screeenshot import Auto
from numpy import ndarray
from PyQt5.QtWidgets import QApplication,QMessageBox

app = QApplication([])

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
                if key != "champ" and key != "meat" and key != "port" and key != "ip":
                    if value == "Chạy Hết":
                        self.boss[key] = 0
                    else:
                        self.boss[key] = value
                        
                else:
                    self.setting[key] = value
        self.BossFilterSuccess = None
        self.LevelFilterSuccess = None
        
        self.Alliance = False
        self.WarAlliance = False
        self.FillterBoss = False
        self.localBoss = None
        self.flagChoseChamp = False
        self.flagSwipe = False
        self.bosslocalError = [(None,None)]
        # ====================image==========================
        self.game = ".\\img\\login\\game.png"
        self.inRungame = ".\\img\\login\\inRungame.png"
        self.relogin = ".\\img\\login\\relogin.png"
        self.gif = ".\\img\\login\\gif.png"
        self.notUpdate = ".\\img\\login\\notUpdate.png"
        self.alliance = ".\\img\\login\\alliance.png"
        self.toMuchESC = ".\\img\\outAlliance\\toMuchESC.png"
        self.HienGoiNap = ".\\img\\outAlliance\\HienGoiNap.png"
        self.close1 = ".\\img\\outAlliance\\close1.png"
        self.inAlliance = ".\\img\\inAlliance\\alliance.png"
        self.goWar = ".\\img\\inAlliance\\goWar.png"
        self.InWarAlliance = ".\\img\\inAlliance\\waralliance.png"
        self.warChamp = ".\\img\\inAlliance\\warChamp.png"
        self.PVP = ".\\img\\inAlliance\\PVP.png"
        self.thamgia = ".\\img\\inWar\\thamgia.png"
        self.tronglocBoss = ".\\img\\inAlliance\\tronglocBoss.png"
        
        self.champ1 = ".\\img\\inWar\\champ1.png"
        self.champ2 = ".\\img\\inWar\\champ2.png"
        self.resetcreep = ".\\img\\inWar\\resetcreep.png"
        self.creep = ".\\img\\inWar\\1creep.png"
        self.clearChamp = ".\\img\\inWar\\clearChamp.png"
        self.lookChamp = ".\\img\\inWar\\look.png"
        self.choseChamp = ".\\img\\inWar\\choseChamp.png"
        self.flag2 = ".\\img\\inWar\\flag2.png"
        self.select1 = ".\\img\\inWar\\select1.png"

        
        # ====================image==========================
        while not self.exitFlag.is_set():
            if not self.Alliance and not self.WarAlliance and not self.FillterBoss:
                self.OutAlliance()
            if self.Alliance:
                self.InAlliance()
            if self.WarAlliance:
                self.InWar()
            if self.FillterBoss:
                self.bossFilter()
            sleep(1)
        self.errorOut()
        
    def checkPosition(self,screenshot):
        position = self.sc.find_img(self.tronglocBoss,screenshot, 0.9, 1)
        if position[0][0] != 0 and position[0][1] != 0:
            self.WarAlliance = False
            self.Alliance = False
            self.FillterBoss = True
            return
        
        position = self.sc.find_img(self.InWarAlliance,screenshot, 0.9, 1)
        position2 = self.sc.find_img(self.warChamp,screenshot, 0.9, 1)
        if (position[0][0] != 0 and position[0][1]) != 0 or (position2[0][0] != 0 and position2[0][1]):
            self.WarAlliance = True
            self.Alliance = False
            self.FillterBoss = False
            return
        
        position = self.sc.find_img(self.inAlliance,screenshot, 0.9, 1)
        if position[0][0] != 0 and position[0][1] != 0:
            self.WarAlliance = False
            self.Alliance = True
            self.FillterBoss = False
            return
        
        self.FillterBoss = False
        self.WarAlliance = False
        self.Alliance = False
    
    def OutAlliance(self):
        while not self.exitFlag.is_set():
            print("vao OutAlliance")
            while not self.exitFlag.is_set():
                screenshot = self.sc.screen_capture()
                if not isinstance(screenshot, ndarray):
                    self.errorOut(1)
                
                self.checkPosition(screenshot)
                if self.Alliance or self.WarAlliance:
                    return
                
                position = self.sc.find_img(self.game,screenshot, 0.9, 1)
                print(position)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    print("Login game, sleep 50s")
                    self.waitLoggame = True
                    sleep(50)
                    break
                
                position = self.sc.find_img(self.notUpdate,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(3)
                    break
                
                position = self.sc.find_img(self.inRungame,screenshot, 0.8, 1) 
                if position[0][0]!= 0 and position[0][1] != 0:
                    print("In load game, sleep 20s")
                    sleep(20)
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
                    sleep(1)
                    break
                
                position = self.sc.find_img(self.close1,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    return
                
                position = self.sc.find_img(self.alliance,screenshot, 0.8, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(3)
                    break
            
                self.sc.esc()
        self.errorOut()
        
    def InAlliance(self):
        while not self.exitFlag.is_set():
            print("vao InAlliance")
            while not self.exitFlag.is_set():
                screenshot = self.sc.screen_capture()
                if not isinstance(screenshot, ndarray):
                    self.errorOut(1)

                self.checkPosition(screenshot)
                if not self.Alliance:
                    return
                
                position = self.sc.find_img(self.goWar,screenshot, 0.9, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0],position[0][1])
                    sleep(2)
                    break
        self.errorOut()
    def InWar(self):
        count = 0
        while not self.exitFlag.is_set():
            print("vao InWar")
            while not self.exitFlag.is_set():
                screenshot = self.sc.screen_capture()
                if not isinstance(screenshot, ndarray):
                    self.errorOut(1)
                
                self.checkPosition(screenshot)
                if not self.WarAlliance:
                    self.flagChoseChamp = False
                    return
                
                position = self.sc.find_img(self.PVP,screenshot, 0.99, 1)
                if position[0][0]!= 0 and position[0][1] != 0:
                    self.sc.click(position[0][0]+80,position[0][1]+20)
                    sleep(3)
                    break
                
                position = self.sc.find_img(self.thamgia,screenshot, 0.9, 2)
                locals = position
                if position[0][0]!= 0 and position[0][1] != 0:
                    if self.bosslocalError[0] == position[0]:
                        if len(position)>=2:
                            print("len 2")
                            if self.bosslocalError[0] == position[1]:
                                pass
                            else:
                                self.bosslocalError = [position[1]]
                                self.sc.click(position[0][0]-50,position[0][1]+5)
                                sleep(3)
                                break
                        self.flagSwipe = True
                        count+=1
                    else:
                        self.bosslocalError = [position[0]]
                        self.sc.click(position[0][0]-50,position[0][1]+5)
                        sleep(3)
                        break
                
                if self.flagSwipe or (locals[0][0] == 0 and locals[0][1] == 0):
                    position = self.sc.find_img(self.PVP,screenshot, 0.8, 1)
                    if position[0][0]!= 0 and position[0][1] != 0:
                        self.sc.swipe(300, 500, 300, 180,3000)
                        self.flagSwipe = False
                        sleep(3)
                        if count == 4:
                            count = 0
                            self.bosslocalError=[(None,None)]
                        break
                
                if self.flagChoseChamp == False:
                    position = self.sc.find_img(self.resetcreep,screenshot, 0.8, 1)
                    if position[0][0]!= 0 and position[0][1] != 0:
                        self.sc.click(position[0][0],position[0][1])
                        sleep(2)
                        position = self.sc.find_img(self.lookChamp,screenshot, 0.9, 1)
                        if position[0][0]!= 0 and position[0][1] != 0:
                            self.sc.click(position[0][0]-350,position[0][1])
                            sleep(5)
                            break
                        else:
                            self.flagChoseChamp = True
                            break
                    position = self.sc.find_img(self.clearChamp,screenshot, 0.8, 1)
                    if position[0][0]!= 0 and position[0][1] != 0:
                        self.sc.click(position[0][0],position[0][1])
                        self.flagChoseChamp = True
                        sleep(5)
                        break
                        
                else:
                    position = self.sc.find_img(self.creep,screenshot, 0.9, 1)
                    print("creeo:",position)
                    if position[0][0]!= 0 and position[0][1] != 0:
                        self.sc.click(position[0][0],position[0][1])
                        sleep(1)
                        
                    if self.setting["champ"] > 0:
                        if self.setting["champ"] == 1:
                            position = self.sc.find_img(self.champ1,screenshot, 0.9, 1)
                            if position[0][0]!= 0 and position[0][1] != 0:
                                self.sc.click(position[0][0],position[0][1])
                                sleep(3)
                                break
                        if self.setting["champ"] >= 2:
                            position = self.sc.find_img(self.champ2,screenshot, 0.9, 1)
                            if position[0][0]!= 0 and position[0][1] != 0:
                                self.sc.click(position[0][0],position[0][1])
                                sleep(3)
                                break
                        
                        position = self.sc.find_img(self.choseChamp,screenshot, 0.95, 1)
                        print(position)
                        if position[0][0]!= 0 and position[0][1] != 0:
                            self.sc.click(position[0][0],position[0][1])
                            sleep(5)
                            break
                        
                    position = self.sc.find_img(self.flag2,screenshot, 0.9, 1)
                    if position[0][0]!= 0 and position[0][1] != 0:
                        self.sc.click(position[0][0]+10,position[0][1]+5)
                        self.flagChoseChamp == False
                        sleep(3)
                        break
                        
                        
                self.sc.esc()
                # 300 500 300 190
        self.errorOut()
    def bossFilter(self):
        while not self.exitFlag.is_set():
            print("vao bossFilter")
            while not self.exitFlag.is_set():
                screenshot = self.sc.screen_capture()
                if not isinstance(screenshot, ndarray):
                    self.errorOut(1)
                
                self.checkPosition(screenshot)
                if not self.FillterBoss:
                    self.BossFilterSuccess = None 
                    self.LevelFilterSuccess = None
                    return
                
                if self.BossFilterSuccess == None and self.LevelFilterSuccess == None:
                    for key, value in self.boss.items():
                        imgBoss = f".\\img\\boss\\{key}.png"
                        position = self.sc.find_img(imgBoss,screenshot, 0.9, 1)
                        if position[0][0]!= 0 and position[0][1] != 0:
                            self.BossFilterSuccess = key
                            self.LevelFilterSuccess = value
                            break
                    if self.BossFilterSuccess == None or self.LevelFilterSuccess == None:
                        self.sc.esc()
                        self.flagSwipe = True
                        return
                
                if self.BossFilterSuccess != None and self.LevelFilterSuccess != None: 
                    if self.BossFilterSuccess == "turtle":
                        for i in range(value+1,6+1):
                            imgBoss = f".\\img\\boss\\{value+1}.png"
                            position = self.sc.find_img(imgBoss,screenshot, 0.9, 1)
                            if position[0][0]!= 0 and position[0][1] != 0:
                                print("tim thay level:", position)
                                self.localBoss = position
                                self.BossFilterSuccess = None 
                                self.LevelFilterSuccess = None
                                self.bosslocalError = [(None,None)]
                                self.sc.click(270,920)
                                sleep(3)
                                return
                        self.flagSwipe = True
                        self.sc.esc()
        self.errorOut()     
# 'ymir': None, 'pumkin': None, 'sphinx': None, 'witch': None, 'hydra': None, 'golem': None, 'turtle': None, 'warlord': None, 'nor': None, 'cerberus': None}
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

        
# adb disconnect 127.0.0.1:5553
# error: no such device '127.0.0.1:5553'





from PyQt5 import QtWidgets,QtCore,QtGui
from shared_variable import Account,buttonTabChange
import multiprocessing as mul
from mulRallyBoss import RunAuto
from buyMeat import RunAuto2
from buyDiamon import RunAuto3
from time import sleep
from resfreshPort import Resfresh_Port
import subprocess

class GuiStart(QtWidgets.QWidget):
    def __init__(self, parent=None,position = None):
        super().__init__(parent)
        self.initUI()
        self.Do = 1
        self.position = position
        self.exitsMul = mul.Event()

    def initUI(self):
        layout = QtWidgets.QGridLayout()
        
        label1 = QtWidgets.QLabel('Nhập IP:')
        label2 = QtWidgets.QLabel('Nhập Port:')
        
        self.inputIP = QtWidgets.QLineEdit()
        self.inputIP.setText("127.0.0.1")
        self.inputIP.setObjectName("inputIP")
        self.inputPort = QtWidgets.QLineEdit()
        self.inputPort.textChanged.connect(self.handleLineEditPort)
        self.inputIP.textChanged.connect(self.handleLineEditIp)
        
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.inputIP, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.inputPort, 1, 1)
        
        self.buttonJoinRally = QtWidgets.QPushButton("JoinRally")
        self.buttonJoinRally.setStyleSheet("background-color: #68bdf8;")
        self.buttonBuyDiamon = QtWidgets.QPushButton("Diamon")
        self.buttonBuyMeat = QtWidgets.QPushButton("Meat")
        self.buttonOpenRelic = QtWidgets.QPushButton("OpenRelic")
        
        self.buttonStart = QtWidgets.QPushButton("Start")

        # Thêm các nút vào layout
        layout.addWidget(self.buttonJoinRally, 0,2)
        layout.addWidget(self.buttonBuyDiamon, 0,3)
        layout.addWidget(self.buttonBuyMeat, 0,4)
        layout.addWidget(self.buttonOpenRelic, 1,3)
        
        # Đặt buttonStart ở dưới cùng và giữa
        layout.addWidget(self.buttonStart, 2, 1, 55, 3, QtCore.Qt.AlignBottom)
                
        self.setLayout(layout)
        
        # Tạo danh sách ánh xạ giữa nút và giá trị self.Do tương ứng
        self.button_values = {
            self.buttonJoinRally: 1,
            self.buttonBuyDiamon: 2,
            self.buttonBuyMeat: 3,
            self.buttonOpenRelic: 4,
            self.buttonStart: False
        }
        
        # Bắt sự kiện khi nút được nhấn và cập nhật giá trị self.Do
        for button in self.button_values.keys():
            
            if button == self.buttonStart:
                button.clicked.connect(self.start)
            else:
                button.clicked.connect(self.buttonClicked)
    
    def buttonClicked(self):
        # Lấy nút đã được nhấn
        sender = self.sender()

        # Cập nhật giá trị self.Do dựa trên nút được nhấn
        self.Do = self.button_values[sender]
        Account[self.position]["do"] = self.Do
        # Đặt màu mặc định cho tất cả các nút
        for button in self.button_values.keys():
            button.setStyleSheet("")

        # Đặt màu cho nút đã được nhấn
        sender.setStyleSheet("background-color: #68bdf8;")

    def start(self):
        sender = self.sender()
        if self.button_values[sender] == False:
            # Lấy danh sách port có kết nối 
            portTrue = Resfresh_Port()
            getPortTrue = portTrue.ResfreshPort()
            # Lấy port đã nhập
            port = self.inputPort.text()
            if port == "":
                return
            else:
                port = int(port)
            ip = self.inputIP.text()
            runStatus = False
            for i in getPortTrue:
                if port == i:
                    runStatus = True
            if runStatus == True:
                connectPort = self.connectPort(port,ip)
                if connectPort == True:
                    # Đặt văn bản mới cho tab
                    buttonTabChange[self.position].setTabText(self.position, f"{port}")
                    
                    # Làm mới lại khóa
                    self.exitsMul.clear()
                    
                    # Set lại button start thành đã chạy
                    self.button_values[sender] = True
                    self.buttonStart.setText("Stop")
                    sender.setStyleSheet("background-color: #68bdf8;")
                    if self.Do == 1:
                        self.mulRun = mul.Process(target=RunAuto,args=(self.exitsMul,port,ip,Account[self.position]))
                        self.mulRun.start()
                    elif self.Do == 2:
                        self.mulRun = mul.Process(target=RunAuto3,args=(self.exitsMul,port,ip))
                        self.mulRun.start()
                    elif self.Do == 3:
                        self.mulRun = mul.Process(target=RunAuto2,args=(self.exitsMul,port,ip))
                        self.mulRun.start()

        else:
            self.exitsMul.set()
            self.mulRun.join()
            self.button_values[sender] = False
            buttonTabChange[self.position].setTabText(self.position, f"{self.position}")
            self.buttonStart.setText("Start")
            sender.setStyleSheet("")

    def connectPort(self,port,ip):
        pwd = 'cd android'
        disconect = subprocess.Popen(f'{pwd} && adb disconnect {ip}:{port}',stdout=subprocess.PIPE, shell=True)
        status = disconect.stdout.read()  
        # Chạy lệnh adb connect và đợi cho đến khi hoàn thành
        connect_command = f'{pwd} && adb connect {ip}:{port}'
        try:
            pipe = subprocess.Popen(connect_command, stdout=subprocess.PIPE, shell=True)
            status = pipe.stdout.read()
            # Lệnh adb connect hoàn thành, kiểm tra kết quả
            if b"connected" in status:
                print(f"Connect to {ip}:{port} success")
                return True
            else:
                return False
        except subprocess.CalledProcessError as e:
        # Lệnh adb connect không thành công, có thể in ra thông báo lỗi
            print(f"Error connecting to {ip}:{port}: {e.stderr}")
            return False
        
    def handleLineEditPort(self, new_text):
        # new_text chứa giá trị mới trong QLineEdit
        # Thực hiện xử lý dựa trên giá trị mới tại đây
        try:
           Account[self.position]['port'] = int(new_text)  # Chuyển giá trị mới thành kiểu số nguyên
        except ValueError:
            # Nếu người dùng nhập không phải là số, bạn có thể xử lý lỗi hoặc thực hiện hành động khác tùy theo yêu cầu
            pass
    
    def handleLineEditIp(self, new_text):
        # new_text chứa giá trị mới trong QLineEdit
        # Thực hiện xử lý dựa trên giá trị mới tại đây
        try:
            Account[self.position]['ip'] = new_text # Chuyển giá trị mới thành kiểu số nguyên
        except ValueError:
            # Nếu người dùng nhập không phải là số, bạn có thể xử lý lỗi hoặc thực hiện hành động khác tùy theo yêu cầu
            pass
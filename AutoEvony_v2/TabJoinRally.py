from PyQt5 import QtWidgets,QtCore
from shared_variable import Account,boss_JoinRally
from functools import partial
class GuiJoinRally(QtWidgets.QWidget):
    def __init__(self, parent=None, position = None):
        super().__init__(parent)
        self.initUI()
        self.position = position
        self.meat_value = 5
        self.champ_value = 2
        
        
    def initUI(self):
        layout = QtWidgets.QGridLayout()  # Sử dụng QHBoxLayout để các phần tử nằm ngang
        
        # tạo frame chọn tướng, thịt
        self.frameSetup(layout)
        
        # tạo frame chọn boss Ymir
        self.frameBoss(layout,"ymir",6,0,1)
        self.frameBoss(layout,"pumkin",6,0,2)
        self.frameBoss(layout,"nor",19,1,0)
        self.frameBoss(layout,"cerberus",4,1,1)
        self.frameBoss(layout,"sphinx",6,1,2)
        self.frameBoss(layout,"turtle",6,2,0)
        self.frameBoss(layout,"golem",6,2,1)
        self.frameBoss(layout,"witch",6,2,2)
        self.frameBoss(layout,"warlord",6,3,0)
        self.frameBoss(layout,"hydra",6,3,1)
        
        # Đặt layout cho QWidget
        self.setLayout(layout)
        
        
    
    def frameSetup(self,layout):
        # Tạo QFrame để làm khung
        frameSetup = QtWidgets.QFrame()
        frameSetup.setFrameShape(QtWidgets.QFrame.Box)  # Đặt kiểu khung
        frameSetup.setLineWidth(1)  # Đặt độ rộng của khung
        frameSetup.setStyleSheet("background-color: LightBlue;")
        
        # ===========================Tạo checkbox==========================================================
        self.champ = QtWidgets.QLabel(self)
        self.champ.setText(f"Chọn tướng:")

        # Tạo khung nhập số liệu (QLineEdit)
        self.lineEditchamp = QtWidgets.QLineEdit()
        self.lineEditchamp.setFixedWidth(15)
        self.lineEditchamp.setText("2")
        self.lineEditchamp.setEnabled(True)  # Ban đầu vô hiệu hóa QLineEdit
        self.lineEditchamp.textChanged.connect(self.handleLineEditChange)
        
        self.meat = QtWidgets.QLabel(self)
        self.meat.setText(f"Chọn tướng:")
        # Tạo khung nhập số liệu (QLineEdit)
        self.lineEditmeat = QtWidgets.QLineEdit()
        self.lineEditmeat.setFixedWidth(15)
        self.lineEditmeat.setText("5")
        self.lineEditmeat.setEnabled(True)  # Ban đầu vô hiệu hóa QLineEdit
        self.lineEditmeat.textChanged.connect(self.handleLineEditmeat)
        #===================================================================================================
        
        
        # =================Thêm các phần tử vào layout với hàng và cột tương ứng============================
        frame_layout = QtWidgets.QGridLayout()
        frame_layout.addWidget(self.champ, 0, 0)
        frame_layout.addWidget(self.lineEditchamp, 0, 1)
        frame_layout.addWidget(self.meat, 2, 0)
        frame_layout.addWidget(self.lineEditmeat, 2, 1)
        frameSetup.setLayout(frame_layout)
        #===================================================================================================
        # Đặt QFrame vào layout chính
        layout.addWidget(frameSetup)
        
    def frameBoss(self,layout,boss,level,row,col):
        frame = QtWidgets.QFrame()
        frame.setFrameShape(QtWidgets.QFrame.Box)  # Đặt kiểu khung
        frame.setMinimumSize(150,1)
        frame.setLineWidth(1)  # Đặt độ rộng của khung
        frame.setStyleSheet("background-color: LightBlue;")
        
        # Tạo một label để hiển thị mục được chọn
        labelBoss = QtWidgets.QLabel(self)
        labelBoss.setAlignment(QtCore.Qt.AlignCenter)
        labelBoss.setText(f"Bỏ hết {boss}")
        
        # Tạo một QComboBox
        dropdownBoss = QtWidgets.QComboBox(self)

        # Thêm các mục vào drop-down menu
        dropdownBoss.addItem(f"Bỏ Hết")
        for i in range(1,level):
            dropdownBoss.addItem(f"{i}")
        dropdownBoss.addItem(f"Chạy Hết")
        
        # Thêm các phần tử vào layout với hàng và cột tương ứng
        frame_layout = QtWidgets.QGridLayout()
        frame_layout.addWidget(labelBoss)
        frame_layout.addWidget(dropdownBoss,1,0)
        frame.setLayout(frame_layout)
        
        # Đặt QFrame vào layout chính
        layout.addWidget(frame,row,col)
        
        # Khi trạng thái của dropdown_Ymir thay đổi, kiểm tra nó
        dropdownBoss.activated.connect(partial(self.on_dropdown, boss=boss,labelBoss = labelBoss))
                
        
    def on_dropdown(self, index, boss,labelBoss):
        # Lấy nút đã được nhấn
        sender = self.sender()
        # Xử lý sự kiện khi một mục được chọn từ drop-down menu
        selected_item = sender.itemText(index)
        if selected_item == "Bỏ Hết":
            del Account[self.position][f'{boss}']
            labelBoss.setText(f"Bỏ Hết {boss}")
        elif selected_item == "Chạy Hết":
            Account[self.position][f'{boss}'] = None
            labelBoss.setText(f"Chạy Hết {boss}")
        else:
            Account[self.position][f'{boss}'] = int(selected_item)
            labelBoss.setText(f"Bỏ {boss}: {selected_item} trở xuống")

    def handleLineEditChange(self, new_text):
        # new_text chứa giá trị mới trong QLineEdit
        # Thực hiện xử lý dựa trên giá trị mới tại đây
        try:
           Account[self.position]['champ'] = int(new_text)  # Chuyển giá trị mới thành kiểu số nguyên
        except ValueError:
            # Nếu người dùng nhập không phải là số, bạn có thể xử lý lỗi hoặc thực hiện hành động khác tùy theo yêu cầu
            pass
    
    def handleLineEditmeat(self, new_text):
        # new_text chứa giá trị mới trong QLineEdit
        # Thực hiện xử lý dựa trên giá trị mới tại đây
        try:
            Account[self.position]['meat'] = int(new_text)  # Chuyển giá trị mới thành kiểu số nguyên
        except ValueError:
            # Nếu người dùng nhập không phải là số, bạn có thể xử lý lỗi hoặc thực hiện hành động khác tùy theo yêu cầu
            pass
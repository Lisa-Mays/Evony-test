from PyQt5 import QtCore, QtGui, QtWidgets
from resfreshPort import Resfresh_Port
from TabStart import GuiStart
from TabJoinRally import GuiJoinRally
from shared_variable import Account,addNew,addButtonTab
class Ui_MainWindow():
    def setupUi(self, MainWindow):
        self.AccAdd = 0
        self.text_file_path = "Account.txt"
        self.Start = []
        self.JoinRally = []
        # Đặt tên cho cửa sổ chính
        MainWindow.setObjectName("AutoEvony")
        MainWindow.setWindowTitle("Auto Evony")
        # Đặt kích thước của cửa sổ chính
        MainWindow.resize(835, 600)
        MainWindow.setWindowIcon(QtGui.QIcon('.\\img\\icon\\icon.png'))
        
        # Tạo biểu tượng (icon) cho cửa sổ chính và đặt nó
        icon = QtGui.QIcon(".//img//icon//icon.png")
        MainWindow.setWindowIcon(icon)

        # Tạo một tiện ích trung tâm (central widget) cho cửa sổ chính
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Tạo một sắp xếp lưới (grid layout) cho tiện ích trung tâm
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        # Tạo một tiện ích tab (tab widget) cho tiện ích trung tâm
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        
        self.gridLayout.addWidget(self.tabWidget)
        
        
        self.model = QtGui.QStandardItemModel(None)
        self.model.setColumnCount(2)  # Số cột
        # Đặt tên cho các cột
        self.model.setHeaderData(0, 1, "EMULATOR")
        self.model.setHeaderData(1, 1, "PORT")
        
        self.table_view = QtWidgets.QTableView()
        self.table_view.setModel(self.model)
        self.table_view.setObjectName("listView")
        
        self.table_view.setColumnWidth(0, 120)
        self.table_view.setColumnWidth(1, 120)
        
        self.gridLayout.addWidget(self.table_view, 0, 1, 1, 2)
        
                        
        self.RefreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshButton.setObjectName("RefreshButton")
        self.RefreshButton.setText("Refresh Port")
        self.RefreshButton.clicked.connect(self.ResetPort)
        self.gridLayout.addWidget(self.RefreshButton, 1, 1,1,1)

        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setObjectName("AddButton")
        self.AddButton.setText("Add Tab")
        self.gridLayout.addWidget(self.AddButton, 1, 2,1,1)
        self.AddButton.clicked.connect(self.addNewTab)

        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setObjectName("StartButton")
        self.StartButton.setText("Start All")
        self.gridLayout.addWidget(self.StartButton, 1, 0, 1, 1)
        self.StartButton.clicked.connect(self.RunAll)

        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setObjectName("StopButton")
        self.StopButton.setText("Stop All")
        self.gridLayout.addWidget(self.StopButton, 2, 0, 1, 1)
        self.StopButton.clicked.connect(self.StopAll)
        
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setObjectName("SaveButton")
        self.SaveButton.setText("Save")
        self.gridLayout.addWidget(self.SaveButton, 2, 1,1,1)
        self.SaveButton.clicked.connect(self.saveData)
        
        self.LoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadButton.setObjectName("LoadButton")
        self.LoadButton.setText("Load")
        self.gridLayout.addWidget(self.LoadButton, 2, 2,1,1)
        self.LoadButton.clicked.connect(self.loadData)
        
        # Đặt tiện ích trung tâm cho cửa sổ chính
        MainWindow.setCentralWidget(self.centralwidget)
        # Kết nối sự kiện và phương thức trong PyQt5
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.ResetPort()
        
    
    def addNewTab(self):
        addNew()
        tab_style = "QTabBar::tab { min-width: 60px;min-height:20px; font-size: 8pt; }"
        # Tạo tab mới   
        New_Acc = QtWidgets.QWidget()
        New_Acc.setObjectName(f"Acc{self.AccAdd}")
        
        # Tạo sắp xếp lưới cho tab mới
        New_Acc_layout = QtWidgets.QGridLayout(New_Acc)
        New_Acc_layout.setObjectName("New_Acc_layout")
        
        # Tạo một TabControl
        chirldTab = QtWidgets.QTabWidget()
        chirldTab.setObjectName("chirldTab")
        
        # Tạo các tab con
        tabStart = QtWidgets.QWidget()
        tabJoinRally = QtWidgets.QWidget()
        tabOpenRelic = QtWidgets.QWidget()
        
        
        # ===============Tạo nội dung cho tab trong TabControl con==========================
        # Tạo tab Start và sử dụng GuiStart để tạo nội dung
        self.Start.append(GuiStart(tabStart,self.AccAdd))
        self.JoinRally.append(GuiJoinRally(tabJoinRally,self.AccAdd)) 
        addButtonTab(self.tabWidget)
        #=======================Thêm các phần tử và điều chỉnh giao diện của tab con)==========================

        chirldTab.setStyleSheet(tab_style)
        
        # Thêm các tab vào TabControl
        chirldTab.addTab(tabStart, "Start")
        chirldTab.addTab(tabJoinRally, "JoinRally")
        chirldTab.addTab(tabOpenRelic, "OpenRelic")
        
        # Thêm TabControl vào cửa sổ chính
        New_Acc_layout.addWidget(chirldTab)
        
        # Thêm tab mới vào tiện ích tab
        self.tabWidget.addTab(New_Acc, f"{self.AccAdd}")
        self.AccAdd += 1
        
        
    def ResetPort(self):
        get_port = Resfresh_Port()
        port = get_port.ResfreshPort()
        self.model.removeRows(0, self.model.rowCount())
        
        if port != 0:
            port = list(port)
            port.sort()
            for i in port:
                item_port = QtGui.QStandardItem(str(i))
                if i==0:
                    item_emulator = QtGui.QStandardItem("NotFound")
                else:
                    item_emulator = QtGui.QStandardItem("Ldplayer")
                self.model.appendRow([item_emulator, item_port])
        
        
    def saveData(self):
        data_str = '\n'.join([str(item) for item in Account])
        with open(self.text_file_path, 'w') as text_file:
            text_file.write("")
            text_file.write(data_str)
    def loadData(self):
        data = []
        with open('Account.txt', 'r') as file:
            lines = file.readlines()
        
        for line in lines:
            dictionary = eval(line.strip())
            data.append(dictionary)
        for i in range(len(data)):
            self.addNewTab()
            self.Start[i].inputPort.setText(str(data[i]["port"]))
            self.Start[i].inputIP.setText(str(data[i]["ip"]))
            self.JoinRally[i].lineEditmeat.setText(str(data[i]["meat"]))
            self.JoinRally[i].lineEditchamp.setText(str(data[i]["champ"]))
            if data[i]["do"] == 1:
                self.Start[i].buttonJoinRally.click()
            elif data[i]["do"] == 2:
                self.Start[i].buttonBuyDiamon.click()
            elif data[i]["do"] == 3:
                self.Start[i].buttonBuyMeat.click()
        file.close()

    def RunAll(self):
        for i in range(self.AccAdd):
            if self.Start[i].button_values[self.Start[i].buttonStart] == False:
                self.Start[i].buttonStart.click()
            
    def StopAll(self):
        for i in range(self.AccAdd):
            if self.Start[i].button_values[self.Start[i].buttonStart] == True:
                self.Start[i].buttonStart.click()
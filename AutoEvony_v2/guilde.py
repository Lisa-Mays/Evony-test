import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui, QtWidgets, QtCore
import tabwidget
import subprocess
from multiprocessing import freeze_support


# new additions
class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt)
            painter.restore()


# class TabWidget(QtWidgets.QTabWidget):
#     def __init__(self, *args, **kwargs):
#         QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
#         self.setTabBar(TabBar(self))
#         self.setTabPosition(QtWidgets.QTabWidget.West)

# new additions


class app_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = tabwidget.Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.tabWidget = TabWidget()
        self.ui.tabWidget.setTabBar(TabBar(self.ui.tabWidget))
        self.ui.tabWidget.setTabPosition(self.ui.tabWidget.West)
        # # Kết nối nút thêm tab mới với một phương thức xử lý sự kiện
        # self.addButton.clicked.connect(self.addNewTab)


if __name__ == '__main__':
    subprocess.Popen("cmd /c setx ADB_LOCAL_TRANSPORT_MAX_PORT 4000")
    freeze_support()
    app = QApplication(sys.argv)
    w = app_window()
    w.show()
    sys.exit(app.exec_())
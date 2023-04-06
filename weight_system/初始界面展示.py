from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
# PySide6-uic test.ui -o ui_test.py    如何把ui文件编译为py文件
# from ui_test import Ui_test
from weight_system.Ui_初始界面 import Ui_MainWindow
from weight_system.ui_源文件导入 import Ui_Form1
from weight_system.ui_数据入库 import Ui_Form2

class MainWindow(QMainWindow, Ui_MainWindow, Ui_Form1, Ui_Form2):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        # 创建页面 Widget
        self.page1 = QWidget()
        self.page1_ui = Ui_Form1()
        self.page1_ui.setupUi(self.page1)

        self.page2 = QWidget()
        self.page2_ui = Ui_Form2()
        self.page2_ui.setupUi(self.page2)

        # 将页面 Widget 添加到 stackedWidget 中
        self.stackedWidget.addWidget(self.page1)
        self.stackedWidget.addWidget(self.page2)

        # 为菜单栏中的菜单项绑定信号和槽函数
        self.actionsourcefileimport.triggered.connect(self.show_page1)
        self.actionfileimport.triggered.connect(self.show_page2)

    def show_page1(self):
        print("show_page1 called")
        self.stackedWidget.setCurrentWidget(self.page1)
        print('Current widget:', self.stackedWidget.currentWidget())

    def show_page2(self):
        self.stackedWidget.setCurrentWidget(self.page2)

if __name__=='__main__':
    app = QApplication([])  #启动一个应用
    window = MainWindow() #实例化主窗口
    window.show() #展示主窗口
    app .exec()#避免程序执行到这一行后直接退出
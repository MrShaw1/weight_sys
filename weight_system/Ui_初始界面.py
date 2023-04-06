# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '初始界面.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStackedWidget, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action123 = QAction(MainWindow)
        self.action123.setObjectName(u"action123")
        self.actionsourcefileimport = QAction(MainWindow)
        self.actionsourcefileimport.setObjectName(u"actionsourcefileimport")
        self.actionfileimport = QAction(MainWindow)
        self.actionfileimport.setObjectName(u"actionfileimport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(380, 180, 120, 80))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_3.setCursor(QCursor(Qt.IBeamCursor))
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.actionsourcefileimport)
        self.menu_2.addAction(self.actionfileimport)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action123.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.actionsourcefileimport.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u6587\u4ef6\u5bfc\u5165", None))
        self.actionfileimport.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5bfc\u5165", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u9884\u5904\u7406", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5165\u5e93", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u4fe1\u606f", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5206\u6790\u4e0e\u5bf9\u6bd4", None))
    # retranslateUi


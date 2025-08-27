# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bc_generator_qt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(737, 325)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButtonStartLoop = QPushButton(self.centralwidget)
        self.pushButtonStartLoop.setObjectName(u"pushButtonStartLoop")
        self.pushButtonStartLoop.setGeometry(QRect(40, 240, 181, 23))
        self.pushButtonExit = QPushButton(self.centralwidget)
        self.pushButtonExit.setObjectName(u"pushButtonExit")
        self.pushButtonExit.setGeometry(QRect(540, 240, 131, 23))
        self.lineEditData = QLineEdit(self.centralwidget)
        self.lineEditData.setObjectName(u"lineEditData")
        self.lineEditData.setGeometry(QRect(190, 150, 301, 20))
        self.labelIterationDelay = QLabel(self.centralwidget)
        self.labelIterationDelay.setObjectName(u"labelIterationDelay")
        self.labelIterationDelay.setGeometry(QRect(40, 210, 71, 16))
        self.lineEdit_IterationDelay = QLineEdit(self.centralwidget)
        self.lineEdit_IterationDelay.setObjectName(u"lineEdit_IterationDelay")
        self.lineEdit_IterationDelay.setGeometry(QRect(110, 210, 111, 20))
        self.label_imageviewer = QLabel(self.centralwidget)
        self.label_imageviewer.setObjectName(u"label_imageviewer")
        self.label_imageviewer.setGeometry(QRect(30, 30, 640, 120))
        self.label_imageviewer.setMaximumSize(QSize(640, 120))
        self.label_imageviewer.setPixmap(QPixmap(u"generated_barcode.jpg"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 737, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonStartLoop.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButtonExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.lineEditData.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Code128 barcode contents", None))
        self.labelIterationDelay.setText(QCoreApplication.translate("MainWindow", u"Delay (ms)", None))
        self.lineEdit_IterationDelay.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Delay in milliseconds", None))
        self.label_imageviewer.setText("")
    # retranslateUi


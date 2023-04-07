# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QHeaderView, QLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(792, 631)
        MainWindow.setMinimumSize(QSize(350, 450))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.profileComboBox = QComboBox(self.groupBox_2)
        self.profileComboBox.setObjectName(u"profileComboBox")

        self.horizontalLayout_2.addWidget(self.profileComboBox)

        self.addProfileButton = QPushButton(self.groupBox_2)
        self.addProfileButton.setObjectName(u"addProfileButton")
        self.addProfileButton.setMaximumSize(QSize(134, 16777215))

        self.horizontalLayout_2.addWidget(self.addProfileButton)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 50))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.startAllRotationButton = QPushButton(self.groupBox)
        self.startAllRotationButton.setObjectName(u"startAllRotationButton")

        self.verticalLayout_2.addWidget(self.startAllRotationButton)

        self.rotationTable = QTableWidget(self.groupBox)
        if (self.rotationTable.columnCount() < 2):
            self.rotationTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.rotationTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.rotationTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.rotationTable.setObjectName(u"rotationTable")
        self.rotationTable.setContextMenuPolicy(Qt.CustomContextMenu)

        self.verticalLayout_2.addWidget(self.rotationTable)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 50))
        self.groupBox_3.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.logTextField = QTextEdit(self.groupBox_3)
        self.logTextField.setObjectName(u"logTextField")
        self.logTextField.setEnabled(True)
        self.logTextField.setStyleSheet(u"QPlainTextEdit {\n"
"	color: rgb(255, 255, 255);  \n"
"}\n"
"QPlainTextEdit:readonly {\n"
"	color: rgb(255, 255, 255);  \n"
"}")
        self.logTextField.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.logTextField)


        self.verticalLayout.addWidget(self.groupBox_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 792, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RClicker", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u0438", None))
        self.addProfileButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0442\u0430\u0446\u0438\u0438", None))
        self.startAllRotationButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0432\u0441\u0435", None))
        ___qtablewidgetitem = self.rotationTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.rotationTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0441\u043a", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433", None))
    # retranslateUi


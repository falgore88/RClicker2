# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RotationHealDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(603, 362)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gid = QGridLayout()
        self.gid.setObjectName(u"gid")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gid.addWidget(self.label_2, 1, 0, 1, 1)

        self.globalTimeoutField = QSpinBox(Dialog)
        self.globalTimeoutField.setObjectName(u"globalTimeoutField")
        self.globalTimeoutField.setMinimum(1)
        self.globalTimeoutField.setMaximum(1000)
        self.globalTimeoutField.setValue(30)

        self.gid.addWidget(self.globalTimeoutField, 1, 7, 1, 2)

        self.rotationNameTextField = QLineEdit(Dialog)
        self.rotationNameTextField.setObjectName(u"rotationNameTextField")

        self.gid.addWidget(self.rotationNameTextField, 0, 1, 1, 8)

        self.bindButton = QPushButton(Dialog)
        self.bindButton.setObjectName(u"bindButton")

        self.gid.addWidget(self.bindButton, 1, 1, 1, 1)

        self.abilityTimeoutField = QSpinBox(Dialog)
        self.abilityTimeoutField.setObjectName(u"abilityTimeoutField")
        self.abilityTimeoutField.setMinimum(1)
        self.abilityTimeoutField.setMaximum(1000)
        self.abilityTimeoutField.setValue(50)

        self.gid.addWidget(self.abilityTimeoutField, 1, 5, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gid.addWidget(self.label_3, 1, 4, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gid.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gid.addWidget(self.label_4, 1, 6, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gid.addWidget(self.label_5, 1, 2, 1, 1)

        self.addonCoordsButton = QPushButton(Dialog)
        self.addonCoordsButton.setObjectName(u"addonCoordsButton")

        self.gid.addWidget(self.addonCoordsButton, 1, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gid)

        self.abilityTable = QTableWidget(Dialog)
        if (self.abilityTable.columnCount() < 4):
            self.abilityTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.abilityTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.abilityTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.abilityTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.abilityTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.abilityTable.setObjectName(u"abilityTable")
        self.abilityTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.abilityTable.verticalHeader().setVisible(True)

        self.verticalLayout_2.addWidget(self.abilityTable)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.saveButton = QPushButton(Dialog)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.rotationNameTextField, self.abilityTimeoutField)
        QWidget.setTabOrder(self.abilityTimeoutField, self.globalTimeoutField)
        QWidget.setTabOrder(self.globalTimeoutField, self.saveButton)
        QWidget.setTabOrder(self.saveButton, self.cancelButton)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u043e\u0442\u0430\u0446\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0411\u0438\u043d\u0434", None))
        self.rotationNameTextField.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u0440\u043e\u0442\u0430\u0446\u0438\u044f", None))
        self.rotationNameTextField.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0439 \u0440\u043e\u0442\u0430\u0446\u0438\u0438", None))
        self.bindButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0436\u043c\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0422\u0430\u0439\u043c\u0430\u0443\u0442 \u043c\u0435\u0436\u0434\u0443 \u0430\u0431\u0438\u043b\u043a\u0430\u043c\u0438, \u043c\u0441", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0422\u0430\u0439\u043c\u0430\u0443\u0442 \u0434\u043b\u044f \u043f\u043e\u0432\u0442\u043e\u0440\u043d\u043e\u0433\u043e \u0437\u0430\u043f\u0443\u0441\u043a\u0430, \u043c\u0441", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043e\u0440\u0434. \u0430\u0434\u0434\u043e\u043d\u0430", None))
        self.addonCoordsButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0436\u043c\u0438", None))
        ___qtablewidgetitem = self.abilityTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.abilityTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u0411\u0438\u043d\u0434", None));
        ___qtablewidgetitem2 = self.abilityTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043e\u0440\u0434", None));
        ___qtablewidgetitem3 = self.abilityTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442", None));
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_widgets.ui'
#
# Created: Fri Oct 29 11:13:04 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(630, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.IconButton = QtWidgets.QPushButton(Dialog)
        self.IconButton.setMinimumSize(QtCore.QSize(40, 40))
        self.IconButton.setMaximumSize(QtCore.QSize(40, 40))
        self.IconButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}")
        self.IconButton.setText("")
        self.IconButton.setIconSize(QtCore.QSize(30, 30))
        self.IconButton.setObjectName("IconButton")
        self.horizontalLayout.addWidget(self.IconButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.messageLable = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.messageLable.setFont(font)
        self.messageLable.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLable.setObjectName("messageLable")
        self.verticalLayout.addWidget(self.messageLable)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_2.addWidget(self.btn_ok)
        self.btn_cancle = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_cancle.setFont(font)
        self.btn_cancle.setObjectName("btn_cancle")
        self.horizontalLayout_2.addWidget(self.btn_cancle)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btn_ok, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QObject.connect(self.btn_cancle, QtCore.SIGNAL("clicked()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.messageLable.setText(QtWidgets.QApplication.translate("Dialog", "Message", None, -1))
        self.btn_ok.setText(QtWidgets.QApplication.translate("Dialog", "OK", None, -1))
        self.btn_cancle.setText(QtWidgets.QApplication.translate("Dialog", "Cancle", None, -1))


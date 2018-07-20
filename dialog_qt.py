# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
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
        self.btn_ok.clicked.connect(Dialog.accept)
        self.btn_cancle.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.messageLable.setText(_translate("Dialog", "Message"))
        self.btn_ok.setText(_translate("Dialog", "OK"))
        self.btn_cancle.setText(_translate("Dialog", "Cancle"))


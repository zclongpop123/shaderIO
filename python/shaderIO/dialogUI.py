#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Wed Aug 01 15:35:08 2018
#========================================
import os
from PySide2 import QtGui, QtWidgets
from . import dialogQt, shaderUtil
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Dialog(QtWidgets.QDialog, dialogQt.Ui_Dialog):
    '''
    '''
    def __init__(self, parent=shaderUtil.get_maya_window(), message='Message'):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

        self.IconButton.setIcon(QtGui.QIcon(os.path.join(shaderUtil.get_script_path(), 'icons/question.png')))
        self.messageLable.setText(message)

        self.exec_()

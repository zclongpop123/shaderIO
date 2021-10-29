#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Wed Aug 01 15:35:08 2018
#========================================
import os
from PySide2 import QtGui, QtWidgets
from . import dialog_widgets, util
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Dialog(QtWidgets.QDialog, dialog_widgets.Ui_Dialog):
    '''
    '''
    def __init__(self, parent=util.get_maya_window(), message='Message'):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

        self.IconButton.setIcon(QtGui.QIcon(os.path.join(util.get_script_path(), 'icons/question.png')))
        self.messageLable.setText(message)

        self.exec_()

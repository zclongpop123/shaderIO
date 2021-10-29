#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Tue Jul 17 14:51:24 2018
#========================================
import os.path, inspect
import maya.cmds as mc
import maya.mel as mel
import maya.OpenMayaUI as OpenMayaUI
from PySide2 import QtWidgets
import shiboken2
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def get_script_path():
    '''
    '''
    script = inspect.getfile(inspect.currentframe().f_back)
    return os.path.dirname(script)




def get_maya_window():
    '''
    '''
    window = OpenMayaUI.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(window), QtWidgets.QWidget)




PROGRESSBAR = mel.eval('string $temp = $gMainProgressBar;')

def startProgress(count):
    mc.progressBar(PROGRESSBAR, e=True, bp=True, maxValue=max(count, 1))



def moveProgress(message):
    mc.progressBar(PROGRESSBAR, e=True, step=1, st=message)



def endProgress():
    mc.progressBar(PROGRESSBAR, e=True, ep=True)



def get_start_dir(start_dir):
    '''
    '''
    if os.path.isfile(start_dir):
        start_dir = os.path.dirname(start_dir)

    elif os.path.isdir(start_dir):
        pass

    else:
        start_dir = mc.workspace(q=True, lfw=True)[0]

    return start_dir




def get_output_path(filter_format='Maya ASCII (*.ma)', start_dir=None):
    '''
    '''
    start_dir = get_start_dir(start_dir)
    filePath = mc.fileDialog2(ff=filter_format, startingDirectory=start_dir)
    return filePath




def get_input_path(filter_format='Maya ASCII (*.ma)', start_dir=None):
    '''
    '''
    start_dir = get_start_dir(start_dir)
    filePath = mc.fileDialog2(ff=filter_format, fm=4, okc='Select', startingDirectory=start_dir)
    return filePath

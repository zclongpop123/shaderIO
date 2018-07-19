#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Tue Jul 17 14:28:28 2018
#========================================
import os.path
import maya.OpenMayaUI as OpenMayaUI
try:
    from PySide2 import QtWidgets, QtCore
    import shiboken2
except:
    from PySide import QtGui, QtCore
    import shiboken
    QtWidgets = QtGui
    shiboken2 = shiboken

from . import shader_qt, shader_core, shader_util
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def get_maya_window():
    '''
    '''
    window = OpenMayaUI.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(window), QtWidgets.QWidget)



class ShaderIO(QtWidgets.QMainWindow, shader_qt.Ui_MainWindow):
    '''
    '''
    def __init__(self, parent=get_maya_window()):
        super(ShaderIO, self).__init__(parent)
        self.setupUi(self)

        self.__current_dir = ''

        self.show()




    @QtCore.Slot(bool)
    def on_btn_setExportShaderPath_clicked(self, args=None):
        '''
        '''
        filePath = shader_util.get_output_path('Maya ASCII (*.ma)', self.__current_dir)
        if filePath:
            self.line_outputShader.setText(filePath[0])
            self.line_outputData.setText('{0}.json'.format(os.path.splitext(filePath[0])[0]))
            self.__current_dir = os.path.dirname(filePath[0])




    @QtCore.Slot(bool)
    def on_btn_setExportDataPath_clicked(self, args=None):
        '''
        '''
        filePath = shader_util.get_output_path('JSON File (*.json)', self.__current_dir)
        if filePath:
            self.line_outputData.setText(filePath[0])
            self.__current_dir = os.path.dirname(filePath[0])




    @QtCore.Slot(bool)
    def on_btn_exportAll_clicked(self, args=None):
        '''
        '''
        data_path = str(self.line_outputData.text())
        if data_path:
            shader_core.export_all_sg_data(data_path)

        node_path = str(self.line_outputShader.text())
        if node_path:
            shader_core.export_all_sg_nodes(node_path)




    @QtCore.Slot(bool)
    def on_btn_exportSelection_clicked(self, args=None):
        '''
        '''
        data_path = str(self.line_outputData.text())
        if data_path:
            shader_core.export_sel_sg_data(data_path)

        node_path = str(self.line_outputShader.text())
        if node_path:
            shader_core.export_sel_sg_nodes(node_path)




    @QtCore.Slot(bool)
    def on_btn_setImportShaderPath_clicked(self, args=None):
        '''
        '''
        filePath = shader_util.get_input_path('Maya ASCII (*.ma)', self.__current_dir)
        if filePath:
            self.line_inputShader.setText(filePath[0])
            self.line_inputData.setText('{0}.json'.format(os.path.splitext(filePath[0])[0]))
            self.__current_dir = os.path.dirname(filePath[0])




    @QtCore.Slot(bool)
    def on_btn_setImportDataPath_clicked(self, args=None):
        '''
        '''
        filePath = shader_util.get_input_path('JSON File (*.json)', self.__current_dir)
        if filePath:
            self.line_inputData.setText(filePath[0])
            self.__current_dir = os.path.dirname(filePath[0])




    @QtCore.Slot(bool)
    def on_btn_import_clicked(self, args=None):
        '''
        '''
        sg_ns = shader_core.refrence_shader(str(self.line_inputShader.text()))
        geo_ns = str(self.line_lineGeoNamespace.text())
        shader_core.assign_shader(str(self.line_inputData.text()), sg_ns, geo_ns, by_sel=False)




    @QtCore.Slot(bool)
    def on_btn_importToSelection_clicked(self, args=None):
        '''
        '''
        sg_ns = shader_core.refrence_shader(str(self.line_inputShader.text()))
        geo_ns = str(self.line_lineGeoNamespace.text())
        shader_core.assign_shader(str(self.line_inputData.text()), sg_ns, geo_ns, by_sel=True)

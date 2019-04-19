#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Tue Jul 17 14:28:28 2018
#========================================
import os.path
import maya.OpenMayaUI as OpenMayaUI
from PySide2 import QtWidgets, QtCore, QtGui
import shiboken2
from . import shaderQt, dialogUI, shaderCore, shaderUtil
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class ShaderIO(QtWidgets.QMainWindow, shaderQt.Ui_MainWindow):
    '''
    '''
    def __init__(self, parent=shaderUtil.get_maya_window()):
        super(ShaderIO, self).__init__(parent)
        self.setupUi(self)

        self.__current_dir = ''

        self.show()




    @QtCore.Slot(bool)
    def on_btn_setExportShaderPath_clicked(self, args=None):
        '''
        '''
        filePath = shaderUtil.get_output_path('Maya ASCII (*.ma)', self.__current_dir)
        if filePath:
            self.line_outputShader.setText(filePath[0])
            self.line_outputData.setText('{0}.json'.format(os.path.splitext(filePath[0])[0]))
            self.__current_dir = os.path.dirname(filePath[0])




    @QtCore.Slot(bool)
    def on_btn_setExportDataPath_clicked(self, args=None):
        '''
        '''
        filePath = shaderUtil.get_output_path('JSON File (*.json)', self.__current_dir)
        if filePath:
            self.line_outputData.setText(filePath[0])
            self.__current_dir = os.path.dirname(filePath[0])




    @QtCore.Slot(bool)
    def on_btn_exportAll_clicked(self, args=None):
        '''
        '''
        if not dialogUI.Dialog(message='Export all shaders and data ? ? ?').result():
            return

        data_path = str(self.line_outputData.text())
        if data_path:
            shaderCore.export_all_shading_data(data_path)

        node_path = str(self.line_outputShader.text())
        if node_path:
            shaderCore.export_all_shading_nodes(node_path)




    @QtCore.Slot(bool)
    def on_btn_exportSelection_clicked(self, args=None):
        '''
        '''
        if not dialogUI.Dialog(message='Export selection shaders and data ? ? ?').result():
            return

        data_path = str(self.line_outputData.text())
        if data_path:
            shaderCore.export_sel_shading_data(data_path)

        node_path = str(self.line_outputShader.text())
        if node_path:
            shaderCore.export_sel_shading_nodes(node_path)




    @QtCore.Slot(bool)
    def on_btn_setImportShaderPath_clicked(self, args=None):
        '''
        '''
        filePath = shaderUtil.get_input_path('Maya ASCII (*.ma)', self.__current_dir)
        if filePath:
            self.line_inputShader.setText(filePath[0])
            self.line_inputData.setText('{0}.json'.format(os.path.splitext(filePath[0])[0]))
            self.__current_dir = os.path.dirname(filePath[0])




    @QtCore.Slot(bool)
    def on_btn_setImportDataPath_clicked(self, args=None):
        '''
        '''
        filePath = shaderUtil.get_input_path('JSON File (*.json)', self.__current_dir)
        if filePath:
            self.line_inputData.setText(filePath[0])
            self.__current_dir = os.path.dirname(filePath[0])




    @QtCore.Slot(bool)
    def on_btn_import_clicked(self, args=None):
        '''
        '''
        if not dialogUI.Dialog(message='Import shaders and data ? ? ?').result():
            return

        sg_ns = shaderCore.refrence_shader(str(self.line_inputShader.text()))
        geo_ns = str(self.line_lineGeoNamespace.text())
        shaderCore.set_shading_members(str(self.line_inputData.text()), sg_ns, geo_ns, by_sel=False)

        attr_file_path = os.path.join(os.path.dirname(str(self.line_inputShader.text())), 'arnoldAttr.json')
        shaderCore.set_arnold_attribute(attr_file_path, geo_ns)




    @QtCore.Slot(bool)
    def on_btn_importToSelection_clicked(self, args=None):
        '''
        '''
        if not dialogUI.Dialog(message='Import shaders and data to selection objects ? ? ?').result():
            return

        sg_ns = shaderCore.refrence_shader(str(self.line_inputShader.text()))
        geo_ns = str(self.line_lineGeoNamespace.text())
        shaderCore.set_shading_members(str(self.line_inputData.text()), sg_ns, geo_ns, by_sel=True)

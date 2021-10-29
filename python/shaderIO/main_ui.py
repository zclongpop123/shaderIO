#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Tue Jul 17 14:28:28 2018
#========================================
import os.path
from PySide2 import QtWidgets, QtCore
from . import main_widgets, dialog_ui, core, util
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class ShaderIO(QtWidgets.QMainWindow, main_widgets.Ui_MainWindow):
    '''
    '''
    def __init__(self, parent=util.get_maya_window()):
        super(ShaderIO, self).__init__(parent)
        self.setupUi(self)

        self.__current_dir = ''

        self.show()




    @QtCore.Slot(bool)
    def on_btn_setExportShaderPath_clicked(self, args=None):
        '''
        '''
        filePath = util.get_output_path('Maya ASCII (*.ma)', self.__current_dir)
        if filePath:
            self.line_outputShader.setText(filePath[0])
            self.line_outputData.setText(os.path.join(os.path.dirname(filePath[0]), 'mapping.json'))
            self.__current_dir = os.path.dirname(filePath[0])




    @QtCore.Slot(bool)
    def on_btn_setExportDataPath_clicked(self, args=None):
        '''
        '''
        filePath = util.get_output_path('JSON File (*.json)', self.__current_dir)
        if filePath:
            self.line_outputData.setText(filePath[0])
            self.__current_dir = os.path.dirname(filePath[0])




    @QtCore.Slot(bool)
    def on_btn_exportAll_clicked(self, args=None):
        '''
        '''
        if not dialog_ui.Dialog(message='Export all shaders and data ? ? ?').result():
            return

        data_path = str(self.line_outputData.text())
        if data_path:
            core.export_all_shading_data(data_path)

        node_path = str(self.line_outputShader.text())
        if node_path:
            core.export_all_shading_nodes(node_path)




    @QtCore.Slot(bool)
    def on_btn_exportSelection_clicked(self, args=None):
        '''
        '''
        if not dialog_ui.Dialog(message='Export selection shaders and data ? ? ?').result():
            return

        data_path = str(self.line_outputData.text())
        if data_path:
            core.export_sel_shading_data(data_path)

        node_path = str(self.line_outputShader.text())
        if node_path:
            core.export_sel_shading_nodes(node_path)




    @QtCore.Slot(bool)
    def on_btn_setImportShaderPath_clicked(self, args=None):
        '''
        '''
        filePath = util.get_input_path('Maya ASCII (*.ma)', self.__current_dir)
        if filePath:
            self.line_inputShader.setText(filePath[0])
            self.line_inputData.setText(os.path.join(os.path.dirname(filePath[0]), 'mapping.json'))
            self.__current_dir = os.path.dirname(filePath[0])




    @QtCore.Slot(bool)
    def on_btn_setImportDataPath_clicked(self, args=None):
        '''
        '''
        filePath = util.get_input_path('JSON File (*.json)', self.__current_dir)
        if filePath:
            self.line_inputData.setText(filePath[0])
            self.__current_dir = os.path.dirname(filePath[0])




    @QtCore.Slot(bool)
    def on_btn_import_clicked(self, args=None):
        '''
        '''
        if not dialog_ui.Dialog(message='Import shaders and data ? ? ?').result():
            return

        sg_ns = core.refrence_shader(str(self.line_inputShader.text()))
        geo_ns = str(self.line_lineGeoNamespace.text())
        core.set_shading_members(str(self.line_inputData.text()), sg_ns, geo_ns, by_sel=False)

        attr_file_path = os.path.join(os.path.dirname(str(self.line_inputShader.text())), 'arnoldAttr.json')
        core.set_arnold_attribute(attr_file_path, geo_ns)




    @QtCore.Slot(bool)
    def on_btn_importToSelection_clicked(self, args=None):
        '''
        '''
        if not dialog_ui.Dialog(message='Import shaders and data to selection objects ? ? ?').result():
            return

        sg_ns = core.refrence_shader(str(self.line_inputShader.text()))
        geo_ns = str(self.line_lineGeoNamespace.text())
        core.set_shading_members(str(self.line_inputData.text()), sg_ns, geo_ns, by_sel=True)

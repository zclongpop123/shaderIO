#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Tue Jul 17 16:06:36 2018
#========================================
import sys
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
path = 'D:/Repo'
path in sys.path or sys.path.append(path)

import shaderIO
reload(shaderIO)

shaderIO.shaderUI.ShaderIO()

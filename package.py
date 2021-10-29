#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Tue Jan 12 16:49:34 2021
#========================================
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
name = 'shaderIO'


version = '0.0.1'


authors = [
    'zangchanglong'
]


description = \
    '''
    '''


requires = [

]


build_command = False


def commands():
    '''
    '''
    env.PYTHONPATH.append('{root}/python')


uuid = '{name}-{version}'.format(name=name, version=str(version))

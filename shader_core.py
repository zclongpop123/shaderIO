#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Tue Jul 10 15:40:53 2018
#========================================
import os, re, json
import maya.cmds as mc
import maya.OpenMaya as OpenMaya
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def get_all_sg_nodes():
    '''
    get scene all shadingEngine nodes.
    '''
    iterator = OpenMaya.MItDependencyNodes(OpenMaya.MFn.kShadingEngine)
    while not iterator.isDone():
        if not OpenMaya.MFnDependencyNode(iterator.item()).isDefaultNode():
            yield iterator.item()
        iterator.next()




def get_sel_sg_nodes():
    '''
    get shadingEngine nodes by selected geometrys.
    '''
    #- get selected geometry
    mc.select(hi=True)
    geo_selection = OpenMaya.MSelectionList()
    OpenMaya.MGlobal.getActiveSelectionList(geo_selection)

    #-
    geo_iterator = OpenMaya.MItSelectionList(geo_selection)
    geo_mobject  = OpenMaya.MObject()
    while not geo_iterator.isDone():
        geo_iterator.getDependNode(geo_mobject)
        sg_iterator = OpenMaya.MItDependencyGraph(geo_mobject, OpenMaya.MFn.kShadingEngine, OpenMaya.MItDependencyGraph.kDownstream)
        while not sg_iterator.isDone():
            if OpenMaya.MFnDependencyNode(sg_iterator.currentItem()).isDefaultNode():
                sg_iterator.next()
                continue

            yield sg_iterator.currentItem()
            sg_iterator.next()

        geo_iterator.next()




def export_sg_nodes(sg_nodes, sg_file_path):
    '''
    '''
    selection = OpenMaya.MSelectionList()
    for sg in sg_nodes:
        selection.add(sg)

    if selection.isEmpty():
        return False

    OpenMaya.MGlobal.setActiveSelectionList(selection)
    OpenMaya.MFileIO.exportSelected(sg_file_path, None, True)

    return True




def export_all_sg_nodes(sg_file_path):
    '''
    '''
    return export_sg_nodes(get_all_sg_nodes(), sg_file_path)




def export_sel_sg_nodes(sg_file_path):
    '''
    '''
    return export_sg_nodes(get_sel_sg_nodes(), sg_file_path)




def get_sg_members(sg_node):
    '''
    '''
    sg_api_mfn = OpenMaya.MFnSet(sg_node)
    geo_selection = OpenMaya.MSelectionList()
    sg_api_mfn.getMembers(geo_selection, False)

    return geo_selection




def get_select_strings(selection, cut_shape=True):
    '''
    '''
    iterator = OpenMaya.MItSelectionList(selection)

    members = list()
    strings = list()
    dagpath = OpenMaya.MDagPath()
    while not iterator.isDone():
        iterator.getStrings(strings)
        iterator.getDagPath(dagpath)

        if cut_shape:
            geo = dagpath.fullPathName().rsplit('|', 1)[0]
        else:
            geo = dagpath.fullPathName().rsplit('.')[0]

        for x in strings:
            if x.count('.') == 0:
                members.append(geo)
            else:
                members.append('{0}.{1}'.format(geo, x.split('.')[-1]))

        iterator.next()

    return members




def export_sg_data(sg_nodes, data_file_path):
    '''
    '''
    data = dict()
    for sg in sg_nodes:
        sg_name    = OpenMaya.MFnDependencyNode(sg).name()
        sg_members = get_select_strings(get_sg_members(sg))
        if sg_members:
            data[sg_name] = sg_members

    with open(data_file_path, 'w') as f:
        json.dump(data, f, indent=4)

    return True




def export_all_sg_data(data_file_path):
    '''
    '''
    sg_nodes = get_all_sg_nodes()
    return export_sg_data(sg_nodes, data_file_path)




def export_sel_sg_data(data_file_path):
    '''
    '''
    sg_nodes = get_sel_sg_nodes()
    return export_sg_data(sg_nodes, data_file_path)




def import_sg_data(data_file_path):
    '''
    '''
    if not os.path.isfile(data_file_path):
        return dict()

    with open(data_file_path, 'r') as f:
        data = json.load(f)
        return data

    return True




def refrence_shader(shader_file_path):
    '''
    '''
    if not os.path.isfile(shader_file_path):
        return

    if shader_file_path in mc.file(q=True, r=True):
        namespace = mc.file(shader_file_path, q=True, ns=True)

    else:
        selection = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(selection)

        basename = os.path.splitext(os.path.basename(shader_file_path))[0]
        OpenMaya.MFileIO.reference(shader_file_path, False, False, basename)
        namespace = mc.file(shader_file_path, q=True, ns=True)

        OpenMaya.MGlobal.setActiveSelectionList(selection)

    return namespace




def assign_shader(data_file_path, sg_ns=None, geo_ns=None, by_sel=False):
    '''
    '''
    data = import_sg_data(data_file_path)

    if by_sel:
        sel_list = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(sel_list)

    for sg, geo_data in data.iteritems():
        #- shader sg
        if sg_ns:
            sg = '{0}:{1}'.format(sg_ns, sg) #- shader_SG -> material:shader_SG

        if not mc.objExists(sg):
            continue

        #- geometry
        geo_list = OpenMaya.MSelectionList()

        if isinstance(geo_data, dict):
            temp = list()
            for geo, faces in geo_data.iteritems():
                for face in faces:
                    temp.append('{0}.{1}'.format(geo, face.split('.')[-1]))
            geo_data = temp

        for geo in geo_data:
            if geo_ns:
                geo = geo.replace('|', '|{0}:'.format(geo_ns))

            for i in range(5):
                try:
                    geo_list.add('{0}*{1}'.format('*:'*i, geo))
                    break
                except:
                    pass

        if by_sel:
            geo_list.intersect(sel_list)

        mc.sets(get_select_strings(geo_list, cut_shape=False), e=True, forceElement=sg)

    return True

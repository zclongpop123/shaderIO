#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Tue Jul 10 15:40:53 2018
#========================================
import os, re, json
import maya.cmds as mc
import maya.OpenMaya as OpenMaya
from . import shaderUtil
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def get_all_shading_nodes():
    '''
    get scene all shadingEngine nodes.
    '''
    iterator = OpenMaya.MItDependencyNodes(OpenMaya.MFn.kShadingEngine)
    while not iterator.isDone():
        yield iterator.item()
        iterator.next()





def get_sel_shading_nodes():
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
            yield sg_iterator.currentItem()
            sg_iterator.next()

        geo_iterator.next()





def export_shading_nodes(sg_nodes, sg_file_path):
    '''
    '''
    selection = OpenMaya.MSelectionList()
    for sg in sg_nodes:
        if not OpenMaya.MFnDependencyNode(sg).isDefaultNode():
            selection.add(sg)

    if selection.isEmpty():
        return False

    OpenMaya.MGlobal.setActiveSelectionList(selection)
    OpenMaya.MFileIO.exportSelected(sg_file_path, None, True)

    return True





def export_all_shading_nodes(sg_file_path):
    '''
    '''
    return export_shading_nodes(get_all_shading_nodes(), sg_file_path)





def export_sel_shading_nodes(sg_file_path):
    '''
    '''
    return export_shading_nodes(get_sel_shading_nodes(), sg_file_path)





def get_shading_members(sg_node):
    '''
    '''
    sg_api_mfn = OpenMaya.MFnSet(sg_node)
    geo_selection = OpenMaya.MSelectionList()
    if not sg_api_mfn.isDefaultNode():
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
            geo = dagpath.fullPathName().rsplit('.', 1)[0]

        for x in strings:
            if x.count('.') == 0:
                members.append(geo)
            else:
                members.append('{0}.{1}'.format(geo, x.split('.')[-1]))

        iterator.next()

    return members





def export_shading_data(sg_nodes, data_file_path):
    '''
    '''
    data = dict()
    for sg in sg_nodes:
        sg_name    = OpenMaya.MFnDependencyNode(sg).name()
        sg_members = get_select_strings(get_shading_members(sg))
        if sg_members:
            sg_members.sort()
            data[sg_name] = sg_members

    with open(data_file_path, 'w') as f:
        json.dump(data, f, indent=4)

    return True





def export_all_shading_data(data_file_path):
    '''
    '''
    sg_nodes = get_all_shading_nodes()
    return export_shading_data(sg_nodes, data_file_path)





def export_sel_shading_data(data_file_path):
    '''
    '''
    sg_nodes = get_sel_shading_nodes()
    return export_shading_data(sg_nodes, data_file_path)





def import_shading_data(data_file_path):
    '''
    '''
    if not os.path.isfile(data_file_path):
        return dict()

    with open(data_file_path, 'r') as f:
        data = json.load(f)
        return data





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





def set_shading_members(data_file_path, shader_ns=None, geo_ns=None, by_sel=False):
    '''
    '''
    data = import_shading_data(data_file_path)

    if by_sel:
        sel_list = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(sel_list)

    shaderUtil.startProgress(len(data))
    for sg, geo_data in data.iteritems():
        #- shader sg
        if shader_ns:
            sg = '{0}:{1}'.format(shader_ns, sg) #- shader_SG -> material:shader_SG

        if not mc.objExists(sg):
            continue

        #- geometry
        shaderUtil.moveProgress('Set shading members for - {0}'.format(sg))

        geo_selection = OpenMaya.MSelectionList()
        for geo in geo_data:
            if geo_ns:
                geo = geo.replace('|', '|{0}:'.format(geo_ns))

            for i in range(5):
                try:
                    geo_selection.add('{0}*{1}'.format('*:'*i, geo))
                    break
                except:
                    pass

        if by_sel:
            geo_selection.intersect(sel_list)

        if not geo_selection.isEmpty():
            mc.sets(get_select_strings(geo_selection, cut_shape=False), e=True, forceElement=sg)
        else:
            print 'No memebers for - {0}'.format(sg)


    shaderUtil.endProgress()

    return True




def set_arnold_attribute(attr_file_path, geo_ns=None, by_sel=False):
    '''
    '''
    if not os.path.isfile(attr_file_path):
        return

    #- set arnold attribute data
    attr_data = dict()
    with open(attr_file_path, 'r') as f:
        attr_data = json.load(f)

    for geo, attrbutes in attr_data.iteritems():
        if geo_ns:
            geo = geo.replace('|', '|{0}:'.format(geo_ns))
        if not mc.objExists(geo):
            continue

        for attr, value in attrbutes.iteritems():
            shapes = mc.listRelatives(geo, s=True, path=True)
            if shapes:
                if re.match('mtoa_', attr) and not mc.attributeQuery(attr, n=shapes[0], ex=True):
                    mc.addAttr(shapes[0], ln=attr[:-1], at="double3")
                    mc.addAttr(shapes[0], ln=attr[:-1]+'X', at="double", p=attr[:-1])
                    mc.addAttr(shapes[0], ln=attr[:-1]+'Y', at="double", p=attr[:-1])
                    mc.addAttr(shapes[0], ln=attr[:-1]+'Z', at="double", p=attr[:-1])

            if isinstance(value, basestring):
                try:
                    mc.setAttr('{0}.{1}'.format(geo, attr), value, typ='string')
                except:
                    pass
            else:
                try:
                    mc.setAttr('{0}.{1}'.format(geo, attr), value)
                except:
                    pass

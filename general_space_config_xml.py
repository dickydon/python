import pymysql.cursors
import connect
import os

connect = connect.generationLogConfig('192.168.9.62', "fx_config_1", "root", "root", "utf8mb4" )
cursor = connect.cursor()

def fun_list_copy_file():
    cursor.execute('select maps from t_copy ;')
    results=cursor.fetchall()
    copy_maps_list=[]
    for result in results:
        copy_maps_list.append(result["maps"])
    return copy_maps_list

def fun_list_all_map_file():
    maps = os.listdir(path='D:\\3D_104\\Server\\GameEngineProject\\config\\map\\')
    maps_list = []
    for map in maps:
        maps_list.append(os.path.basename( map ).split( '_' )[0])
    maps_list.remove('map')
    fina_maps = []
    for  map in maps_list:
        if map not in fina_maps :
            fina_maps.append(map)
    return fina_maps

def fun_create_cell_node( node, channel, map ):
    node.setAttribute('id', map )
    node.setAttribute('channel', channel )
    node.setAttribute('out_channel', channel )
    node.setAttribute('out_merge_channel', channel )
    node.setAttribute('scene', "../config/map/"+ map + "_scene.json"  )
    node.setAttribute('bossRefresh', "../config/map/"+map + "_bossRefresh.json" )
    node.setAttribute('nav', "../config/map/"+map + "_nav.bytes" )
    return node

def fun_create_copy_node( node, map ):
    node.setAttribute('id', map )
    node.setAttribute('channel', "" )
    node.setAttribute('copy', "1" )
    node.setAttribute('scene', "../config/map/"+ map + "_scene.json"  )
    node.setAttribute('bossRefresh', "../config/map/"+map + "_bossRefresh.json" )
    node.setAttribute('nav', "../config/map/"+map + "_nav.bytes" )
    return node

def fun_distin():
    copy_maps = fun_list_copy_file()
    maps = fun_list_all_map_file()
    normal_maps = []
    for map in maps:
        if  map not in copy_maps:
            normal_maps.append(map)

    import xml.dom.minidom
    impl = xml.dom.minidom.getDOMImplementation()   
    dom = impl.createDocument( None, 'root', None)
    root = dom.documentElement
    f= open('test.xml', 'w', encoding='utf-8')
    for normal_map in normal_maps:
        cell_space = dom.createElement( 'space')
        channel = "3001"
        if int(normal_map) > 140000:
            channel = "3003"
        elif int(normal_map) > 110501:
            channel = "3002"            
        fun_create_cell_node( cell_space, channel, normal_map)
        root.appendChild( cell_space)
    for copy_map in copy_maps:
        copy_space = dom.createElement( 'space')
        fun_create_copy_node(copy_space,copy_map )
        root.appendChild( copy_space)
    dom.writexml(f, addindent='  ', newl= '\n', encoding='utf-8' )

fun_distin()


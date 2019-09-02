import bpy
import glob
import bmesh
from mathutils import Vector, Matrix
from itertools import groupby

def vertex_sort(t):
    return t.co.z

def load_trench():
    base_dir = '/home/warrick/Desktop/trench_wall/'
    paths = glob.glob(base_dir + '*.shp')
    for shape_path in paths:
        bpy.ops.importgis.shapefile(filepath=shape_path)
        

def edit_mode():
    bpy.ops.object.mode_set(mode='EDIT')

def obj_mode():
    bpy.ops.object.mode_set(mode='OBJECT')

def create_bounding_box():
    # just make a cube of min -> max values on every axis.
    # TODO: quite easy to sort scaling because cube scale = 1 unit either direction.
    # e.g. 15 on x axis covers -15, 15. Just sort by math.abs(vert.co.x, y, and z then do accordingly)
    print("creating bounding box")
    obj = bpy.context.object
    me = bpy.context.object.data
    edit_mode()
    bm = bmesh.from_edit_mesh(me)
    bm.faces.ensure_lookup_table()
    bm.verts.ensure_lookup_table()
    bounding_box_center = obj.location
    
    # TODO: refactor into singular function
    max_x_position = sorted(bm.verts, reverse=True, key=lambda v: abs(v.co.x))
    max_x = abs(max_x_position[0].co.x)

    max_y_position = sorted(bm.verts, reverse=True, key=lambda v: abs(v.co.y))
    max_y = abs(max_y_position[0].co.y)

    max_z_position = sorted(bm.verts, reverse=True, key=lambda v: abs(v.co.z))
    max_z = abs(max_z_position[0].co.z)
    obj_mode()
    
    bpy.ops.mesh.primitive_cube_add(location=bounding_box_center)
    bpy.context.scene.objects.active.scale = (max_x, max_y, max_z)

    
    

def bridge_all_loops():
    me = bpy.context.object.data
    bm = bmesh.from_edit_mesh(me)
    
    print(len(bm.verts))
    # sorted_verts = bm.verts.sort(vertex_sort)
    v_sorted = sorted(bm.verts, key=lambda v: (v.co.z))
    z_grouped = dict(groupby(v_sorted, lambda v: (v.co.z)))
    # print(len(z_grouped.keys()))
    
    for index, z_val in enumerate(sorted(z_grouped.keys())):
        print(index)
        print(z_val)
        for vert in z_grouped[z_val]:
            vert.select = True
    
# load_trench()
# bridge_all_loops()

create_bounding_box()


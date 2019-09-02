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
    print("run")
    obj = bpy.context.object
    me = bpy.context.object.data
    edit_mode()
    bm = bmesh.from_edit_mesh(me)
    bm.faces.ensure_lookup_table()
    bm.verts.ensure_lookup_table()
    start_pos = bm.faces[0].verts[0].co + obj.location
    obj_mode()
#     bpy.ops.mesh.primitive_cube_add(location=start_pos)
    bounding_box = bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
    bpy.context.scene.objects.active.scale = (2.2, 1, 1)
    # start expanding cube till no intersects or contains all points.
    

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


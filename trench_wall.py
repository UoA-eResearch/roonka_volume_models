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
    
load_trench()
bridge_all_loops()
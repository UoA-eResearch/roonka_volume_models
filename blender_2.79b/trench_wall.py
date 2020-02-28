import bpy
import glob
import bmesh
from mathutils import Vector, Matrix
from itertools import groupby

from helpers import edit_mode, obj_mode, get_active

'''
Description: Created for the purpose of creating the trench wall volume. Instructions are within the readme.md.
Blender version: 2.79b
'''

resolution = 1


def vertex_sort(t):
    return t.co.z


def load_trench():
    base_dir = '/home/warrick/Desktop/trench_wall/'
    paths = glob.glob(base_dir + '*.shp')
    for shape_path in paths:
        bpy.ops.importgis.shapefile(filepath=shape_path)

def create_bounding_box():
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
    max_y_position = sorted(bm.verts, reverse=True, key=lambda v: abs(v.co.y))
    max_z_position = sorted(bm.verts, reverse=True, key=lambda v: abs(v.co.z))

    max_x = round(abs(max_x_position[0].co.x))
    max_y = round(abs(max_y_position[0].co.y))
    max_z = round(abs(max_z_position[0].co.z))

    obj_mode()

    bpy.ops.mesh.primitive_cube_add(location=bounding_box_center)
    bpy.context.scene.objects.active.scale = (max_x, max_y, max_z)
    bounding_box = bpy.context.active_object
    bounding_box.name = 'bounding_box'
    return bounding_box


def populate_rectangles(bounds):

    def _calculate_axis_iterations(increment, scale):
        print(increment, scale)
        return scale / increment

    print('populate rects')
    # TODO: slice up the bounding box and create cubes. Check if vertices is within the cube. If it is, then keep it. If else, destroy it.
    #resolution
    # box is centered on the volume and scale is uniform, therefore uniform both ways.
    increment = 1
    x_iters = _calculate_axis_iterations(increment, bounds.scale.x)
    y_iters = _calculate_axis_iterations(increment, bounds.scale.y)
    z_iters = _calculate_axis_iterations(increment, bounds.scale.z)
    print(z_iters)
    # x coords
    
    # y coords
    # z coords

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

box = create_bounding_box()
populate_rectangles(box)



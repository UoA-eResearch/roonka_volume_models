
import glob
import bpy
import bmesh
from mathutils import Vector, Matrix

data = bpy.data
objects = data.objects
active_obj = bpy.context.scene.objects.active

def select(obj_name):
    objects[obj_name].select = True


def deselect(obj_name):
    objects[obj_name].select = False

def get_max_vert(vertices, axis):
    ''' returns max vertex from a list of vertices'''
    axis_idx = {
        'x': 0,
        'y': 1,
        'z': 2,
    }
    return sorted(vertices, reverse=True, key=lambda v: abs(v.co[axis_idx[axis]]))[0].co


def get_min_vert(vertices, axis, reverse=True):
    ''' returns max vertex from a list of vertices'''
    axis_idx = {
        'x': 0,
        'y': 1,
        'z': 2,
    }
    return sorted(vertices, reverse=True, key=lambda v: abs(v.co[axis_idx[axis]]))[len(vertices) -1].co

select('Cube')
verts = active_obj.data.vertices
min_x = get_min_vert(verts, 'x')
max_x = get_max_vert(verts, 'x')

min_y = get_min_vert(verts, 'y')
max_y = get_max_vert(verts, 'y')

min_z = get_min_vert(verts, 'z')
max_z = get_max_vert(verts, 'z')

print(min_x, max_x)
print(min_y, max_y)
print(min_z, max_z)

deselect('Cube')


# artefacts now active
active_obj = objects['Artefacts']
art_verts = active_obj.data.vertices
for vert in art_verts:
    print(vert.co)










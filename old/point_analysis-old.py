
import glob
import bpy
import bmesh
from mathutils import Vector, Matrix

# from helpers import edit_mode

def get_bounding_sphere_radius(center_pos):
    ''' returns the radius of bounding sphere '''
    # center_pos = bm.select_history.active.location
    print(center_pos)
    verts = [v for v in bm.verts if v.select]
    verts.sort(key=lambda v:(center_pos - v.co).length)
    farthest_vert = verts[0]
    # distance between verts
    print((farthest_vert.co - center_pos).length)
    farthest_dist = (farthest_vert.co - center_pos).length
    # distance disregarding local z component
    # print((farthest_vert.co.xy - center_pos.xy).length)
    return farthest_dist

def get_max_vertex(vertices, axis, reverse=True):
    ''' returns max vertex from a list of vertices'''
    axis_idx = {
        'x': 0,
        'y': 1,
        'z': 2,
    }
    return sorted(vertices, reverse=reverse, key=lambda v: abs(v.co[axis_idx[axis]]))[0].co

def cull_vertices_outside_bounding_box(obj, vertices):
    print(obj.name)
    max_x = get_max_vertex(obj.data.vertices, 'x')
    min_x = get_max_vertex(obj.data.vertices, 'x', reverse=False)
    max_y = get_max_vertex(obj.data.vertices, 'y')
    max_z = get_max_vertex(obj.data.vertices, 'z')
    print(max_x, min_x, max_y, max_z)

def process_active_obj_verts(artefacts):
    bpy.ops.object.mode_set(mode = 'EDIT')
    mesh = artefacts.data
    print(artefacts.name)
    under = 0
    over = 0
    in_verts = []
    for vert in mesh.vertices:
        euclidean_dist = (vert.co - feature_center_location).length
        if (euclidean_dist < bounding_sphere_radius):
            under = under + 1
        else:
            in_verts.append(vert)
            over = over + 1
    mesh.vertices.foreach_set("select", in_verts)
    print(under, over)
    

# get volumes to analyse (anything startin with F I guess?)
context = bpy.context
scene = context.scene
ob = context.object
feature_center_location = ob.location 
me = ob.data
bm = bmesh.from_edit_mesh(me)

bounding_sphere_radius = get_bounding_sphere_radius(feature_center_location)
print(bounding_sphere_radius)

bpy.ops.object.mode_set(mode = 'OBJECT')

artefacts = bpy.data.objects['Artefacts']

cull_vertices_outside_bounding_box(bpy.data.objects['Cube'], artefacts.data.vertices)

# process_active_obj_verts(artefacts)
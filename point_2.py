
import glob
import bpy
import bmesh
from mathutils import Vector, Matrix
from math import pi, acos


def edit_mode():
        bpy.ops.object.mode_set(mode='EDIT')

def ob_mode():
        bpy.ops.object.mode_set(mode='OBJECT')

def select(obj_name):
    objects[obj_name].select = True

def deselect(obj_name):
    objects[obj_name].select = False

def brek():
    print(10/0)

def is_inside(ray_origin, ray_destination, obj):
    # print(ray_origin, ray_destination, obj)
    mat = obj.matrix_local.inverted()
    f = obj.ray_cast(mat * ray_origin, mat * ray_destination)
    result, loc, normal, face_idx = f

    if face_idx == -1:
        return False

    max_expected_intersections = 1000
    fudge_distance = 0.0001
    direction = (ray_destination - loc)
    dir_len = direction.length
    amount = fudge_distance / dir_len

    i = 1
    while (face_idx != -1):
        loc = loc.lerp(direction, amount)    
        f = obj.ray_cast(mat * loc, mat * ray_destination)
        result, loc, normal, face_idx = f
        print(face_idx)
        if face_idx == -1:
            break
        i += 1
        if i > max_expected_intersections:
            break

    return not ((i % 2) == 0)

def is_inside2(target_pt_global, mesh_obj, tolerance=0.11):
    '''
    Method using comparing of outward facing mesh normal with vertex point.
    '''
    # Convert the point from global space to mesh local space
    target_pt_local = mesh_obj.matrix_world.inverted() * target_pt_global
    # Find the nearest point on the mesh and the nearest face normal
    _, pt_closest, face_normal, _ = mesh_obj.closest_point_on_mesh(target_pt_local)
    # Get the target-closest pt vector
    target_closest_pt_vec = (pt_closest - target_pt_local).normalized()
    # Compute the dot product = |a||b|*cos(angle)
    dot_prod = target_closest_pt_vec.dot(face_normal)
    # Get the angle between the normal and the target-closest-pt vector (from the dot prod)
    angle = acos(min(max(dot_prod, -1), 1)) * 180 / pi
    # Allow for some rounding error
    inside = angle < 90-tolerance
    return inside

data = bpy.data
objects = data.objects
active_obj = bpy.context.scene.objects.active
volume_obj = active_obj
deselect(active_obj.name)

active_obj = objects['Artefacts']
art_offset = active_obj.location
art_verts = active_obj.data.vertices
count =0

for ob in objects:
    if ob.name.startswith('Artefacts'):
        start_pos = ob.location
        end_pos = start_pos + Vector([0, 0, 1000])
        if is_inside(start_pos, end_pos, volume_obj) and is_inside2(ob.location, volume_obj):
            ob.select = True
            count += 1
            print(ob.name)

print('count: {}'.format(count))
# edit_mode()

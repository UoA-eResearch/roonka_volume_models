
import glob
import bpy
import bmesh
from mathutils import Vector, Matrix

data = bpy.data
objects = data.objects
active_obj = bpy.context.scene.objects.active


def edit_mode():
        bpy.ops.object.mode_set(mode='EDIT')


def ob_mode():
        bpy.ops.object.mode_set(mode='OBJECT')


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
    return sorted(vertices, reverse=True, key=lambda v: abs(v.co[axis_idx[axis]]))[len(vertices) - 1].co


def within_bounds():
    print('check if point within the bounding box')


select('F127.001 (hull)_NEAREST_SURFACEPOINT')
active_obj = objects['F127.001 (hull)_NEAREST_SURFACEPOINT']
verts = active_obj.data.vertices
cube = active_obj
box_location = active_obj.location
min_x = get_min_vert(verts, 'x') + box_location
max_x = get_max_vert(verts, 'x') + box_location

min_y = get_min_vert(verts, 'y') + box_location
max_y = get_max_vert(verts, 'y') + box_location

min_z = get_min_vert(verts, 'z') + box_location
max_z = get_max_vert(verts, 'z') + box_location

print(min_x, max_x)
print(min_y, max_y)
print(min_z, max_z)

deselect('F127.001 (hull)_NEAREST_SURFACEPOINT')


def brek():
    print(10/0)


def is_inside(ray_origin, ray_destination, obj):
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

# artefacts now active
active_obj = objects['Artefacts']
art_offset = active_obj.location
select('Artefacts')
art_verts = active_obj.data.vertices
count =0
for vert in art_verts:
    start_pos = art_offset + vert.co
    end_pos = start_pos + Vector([0, 0, 100])
    direction = (end_pos - start_pos)
    if is_inside(start_pos, end_pos, cube):
        count = count + 1
        bpy.ops.mesh.primitive_cube_add(location=vert.co + art_offset, radius=0.001)


print('count: {}'.format(count))
# edit_mode()

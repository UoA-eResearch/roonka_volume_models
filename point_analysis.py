import os
import glob
import bpy
import bmesh
from pprint import pprint
from collections import OrderedDict
from mathutils import Vector, Matrix
from math import pi, acos

# need to install fiona, shapely and attrs into a venv then cp their site-packages into the blender modules folder before these imports can work correctly.
import fiona
from shapely.geometry import mapping, Point, MultiPoint


def edit_mode():
    bpy.ops.object.mode_set(mode='EDIT')


def ob_mode():
    bpy.ops.object.mode_set(mode='OBJECT')


def select(obj_name):
    objects[obj_name].select = True


def deselect(obj_name):
    bpy.data.objects[obj_name].select = False


def end():
    ''' ends script without quitting blender. '''
    print(10/0)


def is_inside_intersection_compare(ray_origin, ray_destination, obj):
    ''' Returns if raycast from vertex intersects faces odd amount of times. Odd = inside, Even = outside '''
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


def is_inside_angle_compare(target_pt_global, mesh_obj, tolerance=0.11):
    ''' Method using comparing of outward facing mesh normal with vertex point. '''
    # Convert the point from global space to mesh local space
    target_pt_local = mesh_obj.matrix_world.inverted() * target_pt_global
    # Find the nearest point on the mesh and the nearest face normal
    _, pt_closest, face_normal, _ = mesh_obj.closest_point_on_mesh(
        target_pt_local)
    # Get the target-closest pt vector
    target_closest_pt_vec = (pt_closest - target_pt_local).normalized()
    # Compute the dot product = |a||b|*cos(angle)
    dot_prod = target_closest_pt_vec.dot(face_normal)
    # Get the angle between the normal and the target-closest-pt vector (from the dot prod)
    angle = acos(min(max(dot_prod, -1), 1)) * 180 / pi
    # Allow for some rounding error
    inside = angle < 90-tolerance
    return inside


def write_to_shapefile(artefact_ids):
    ''' Creates a duplicate shapefile that excludes specified ids '''
    with fiona.open('/home/warrick/Desktop/artefacts/Artefacts.shp') as source:
        source_schema = source.schema
        source_driver = source.driver
        source_crs = source.crs
        with fiona.open(
            './output.shp',
            'w',
            driver=source_driver,
            crs=source_crs,
            schema=source_schema
        ) as sh_output:
            features_written = 0
            for feature in source:
                artefact_id = feature['properties']['Id']
                if artefact_id in artefact_ids:
                    features_written += 1
                    sh_output.write(feature)
    print('Features written to output file: ', features_written)


def find_features_inside_volume():
    ''' Returns list of Id properties from all objects within the active object and are starting with 'Artefact' in the scene.'''
    # TODO: Refactor to remove this section from this function.
    active_obj = bpy.context.scene.objects.active
    volume_obj = active_obj
    deselect(active_obj.name)

    artefact_ids = []
    count = 0
    for ob in bpy.data.objects:
        # TODO: Refactor to yield artefact objects as a separate function.
        if ob.name.startswith('Artefacts'):
            start_pos = ob.location
            end_pos = start_pos + Vector([0, 0, 1000])
            if is_inside_intersection_compare(start_pos, end_pos, volume_obj) and is_inside_angle_compare(ob.location, volume_obj):
                ob.select = True
                count += 1
                artefact_ids.append(ob['Id'])
    print('Points selected: ', count)
    print('Ids in list: ', len(artefact_ids))
    return artefact_ids


artefact_ids = find_features_inside_volume()
write_to_shapefile(artefact_ids)
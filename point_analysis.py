import os
import glob
import bpy
import bmesh
from pprint import pprint
from collections import OrderedDict
from mathutils import Vector, Matrix
from math import pi, acos

import shutil
from os import path

import shapefile

# need to install fiona and attrs into a venv then cp their site-packages into the blender modules folder before these imports can work correctly.
# if you are using blender 2.8, you can simply install fiona using pip by running the following.
# path/to/blenders/python37m pip install fiona
# https://blender.stackexchange.com/a/56013 stack exchange instructions


shapefile_source_path = '/home/warrick/Desktop/artefacts/Artefacts.shp'
output_directory_path = '/home/warrick/Desktop/artefacts/output.shp'


def edit_mode():
    bpy.ops.object.mode_set(mode='EDIT')


def ob_mode():
    bpy.ops.object.mode_set(mode='OBJECT')


def select(obj_name):
    bpy.data.objects[obj_name].select_set(True)


def deselect(obj_name):
    bpy.data.objects[obj_name].select_set(False)


def end():
    ''' ends script without quitting blender. '''
    print(10/0)


def is_inside_intersection_compare(ray_origin, ray_destination, obj):
    ''' Returns if raycast from vertex intersects faces odd amount of times. Odd = inside, Even = outside '''
    # print(ray_origin, ray_destination, obj)
    mat = obj.matrix_local.inverted()
    f = obj.ray_cast(mat @ ray_origin, mat @ ray_destination)
    _, loc, _, face_idx = f

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
        f = obj.ray_cast(mat @ loc, mat @ ray_destination)
        _, loc, _, face_idx = f
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
    target_pt_local = mesh_obj.matrix_world.inverted() @ target_pt_global
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


def write_to_shapefile_fiona(artefact_ids):
    ''' Creates a duplicate shapefile that excludes specified ids '''
    # with fiona.open('/home/warrick/Desktop/artefacts/Artefacts.shp') as source:
    with fiona.open(shapefile_source_path) as source:
        source_schema = source.schema
        source_driver = source.driver
        source_crs = source.crs
        with fiona.open(
            # './output.shp',
            output_directory_path,
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

def write_to_shapefile_pyshp(artefact_ids):

    def _copy_file(f_path):
        if path.exists(f_path):
            src = path.realpath(f_path)
        head, tail = path.split(src)
        dst = src + ".copy"
        # shutil.copy(src, dst)
        return dst


    # dest = _copy_file("/home/warrick/Desktop/roonka/artefacts/Artefacts.shp")
    # dest_dbf = _copy_file("/home/warrick/Desktop/roonka/artefacts/Artefacts.dbf")

    source_shp = open('/home/warrick/Desktop/roonka/artefacts/Artefacts.shp', 'rb')
    source_dbf = open('/home/warrick/Desktop/roonka/artefacts/Artefacts.dbf', 'rb')
    shp_reader = shapefile.Reader(shp=source_shp, dbf=source_dbf)
    # source_fields = shp_reader.fields
    # print(shp_reader.shapeType)
    # print(shp_reader.fields)
    # print(shp_reader.record(3))
    # print(shp_reader.__geo_interface__)
    w = shapefile.Writer("/home/warrick/Desktop/roonka/artefacts/testy")
    w.fields = shp_reader.fields[1:]
    for index, shaperec in enumerate(shp_reader.iterShapeRecords()):
        record = shp_reader.record(index)
        # print(shaperec)
        # print(record)
        if record[0] in artefact_ids:
            w.record(*shaperec.record)
            w.shape(shaperec.shape)
    w.close()



def find_features_inside_volume():
    ''' Returns list of Id properties from all objects within the active object and are starting with 'Artefact' in the scene.'''
    # TODO: Refactor to remove this section from this function.
    active_obj = bpy.context.view_layer.objects.active
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
                select(ob.name)
                count += 1
                artefact_ids.append(ob['Id'])
    print('Points selected: ', count)
    print('Ids in list: ', len(artefact_ids))
    return artefact_ids


artefact_ids = find_features_inside_volume()
print('hi', artefact_ids)

# import fiona
write_to_shapefile_pyshp(artefact_ids)
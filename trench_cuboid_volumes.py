import glob
import bpy
import bmesh
from mathutils import Vector, Matrix

output_path = '/home/warrick/Desktop/'
remesh_octree_depth = 6

def edit_mode():
    bpy.ops.object.mode_set(mode='EDIT')


def ob_mode():
    bpy.ops.object.mode_set(mode='OBJECT')


def select(obj_name):
    bpy.data.objects[obj_name].select = True


def deselect(obj_name):
    bpy.data.objects[obj_name].select = False


def end():
    ''' ends script without quitting blender. '''
    print(10/0)


def deselect_all():
    bpy.ops.object.select_all(action='DESELECT')


def select_objects(str):
    for obj in bpy.data.objects:
        if obj.name.startswith('TIN'):
            obj.select = True


def active_obj():
    return bpy.context.scene.objects.active


data = bpy.data
objects = bpy.data.objects
active_obj = bpy.context.scene.objects.active
# select both objects

layers = bpy.context.selected_objects
print(layers)
cube_spawn_loc =Vector([0, 0, 0])
for layer in layers:
    bpy.ops.object.select_all(action='DESELECT')
    layer.select = True
    print(layer.location)
    cube_spawn_loc += layer.location
    active_obj = layer
    bpy.ops.tesselation.delaunay()

# Joining delaunay layers
print('Joining TINs')
deselect_all()
select_objects('TIN')
bpy.ops.object.join()
join_layer_name = bpy.context.scene.objects.active.name
print(join_layer_name)

# create the cube in the middle of the layers
# print(cube_spawn_loc)
# print(cube_spawn_loc/2)
cube_spawn_loc /= 2
bpy.ops.mesh.primitive_cube_add(location=cube_spawn_loc)

#Remesh
print('remeshing')
remesher = bpy.context.scene.objects.active.modifiers.new(name="Remesh", type="REMESH")
remesher.octree_depth = remesh_octree_depth
remesher.mode = "BLOCKS"
remesher.use_smooth_shade = False
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh")

# Shrinkwrap
print('shrinkwrapping')
shrinker = bpy.context.scene.objects.active.modifiers.new(name="Shrinkwrap", type="SHRINKWRAP")
shrinker.target = bpy.data.objects[join_layer_name]
shrinker.wrap_method = 'NEAREST_VERTEX'
# shrinker.wrap_method = 'NEAREST_SURFACEPOINT'
# shrinker.wrap_method = shrink_method
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Shrinkwrap")

# Smooth?
# Decimate/Subdivide?
# NOTE: only necessary if surface point shrinking. Vertex point seems to simplify the mesh already

# recalculate normals
print('recalculating normals')
edit_mode()
bpy.ops.mesh.normals_make_consistent()
ob_mode()

# Rename & set file name
print('exporting file')
bpy.context.scene.objects.active.name = '_'.join([l.name for l in layers]) + "_connected"
bpy.context.scene.objects.active.select = True
output_filename = bpy.context.scene.objects.active.name 

# export
bpy.ops.wm.collada_export(filepath=output_path + output_filename, selected=True)
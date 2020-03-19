import glob
import bpy
import bmesh
from mathutils import Vector, Matrix

# configurable settings
delete_after_export = False
octree_depth = 7

# shapefile CRS
shpCRS = "EPSG:4326"

# include volume in file name
volume_in_filename = False

def create_hull():
    # CONVERTS TO CONVEX HULL
    context = bpy.context
    scene = context.scene
    ob = context.object
    me = ob.data
    bm = bmesh.new()
    bm.from_mesh(me)
    copy = ob.copy()
    ch = bpy.data.meshes.new("%s convexhull" % me.name)
    bmesh.ops.convex_hull(bm, input=bm.verts)
    bm.to_mesh(ch)
    copy.name = "%s (hull)" % ob.name
    copy.data = ch
    scene.collection.objects.link(copy)
    # bpy.ops.outliner.object_operation(TYPE="DESELECT")
    return copy, ob
    
def remesh(obj, original, shrink_method):
    ''' Remeshes to higher resolution, shrinks and smooths then returns the result. '''
    # bpy.context.collection.objects.active = obj
    obj.select_set(state=True)

    # TODO: separate into separate function
    remesher = obj.modifiers.new(name="Remesh", type="REMESH")
    remesher.octree_depth = octree_depth
    remesher.mode = "SMOOTH"
    remesher.use_smooth_shade = True
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh")

    # TODO: separate into separate function
    shrinker = obj.modifiers.new(name="Shrinkwrap", type="SHRINKWRAP")
    shrinker.target = bpy.data.objects[original.name]
    # shrinker.wrap_method = 'NEAREST_VERTEX'
    shrinker.wrap_method = shrink_method
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Shrinkwrap")

    # TODO: separate into separate function
    smoother = obj.modifiers.new(name="Smooth", type="SMOOTH")
    smoother.factor = 0.9
    smoother.iterations = 40
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Smooth")
    return obj

def singular_select(target_object):
    ''' deselects all except the matching object '''
    # bpy.context.scene.objects.active = obj
    selected_objects = bpy.context.selected_objects
    for obj in selected_objects:
        if target_object == obj:
            # target_object.select = True
            obj.select_set(state=True) # = False
        else:
            print('deselecting: %s' % obj.name)
            obj.select_set(state=False) # = False

def get_object_volume(obj):
    ''' Returns the volume of the object '''
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    return bm.calc_volume()
    
def create_output_file_name(base_dir, object, shrink_type, smooth_iterations, file_type='dae'):
    volume_str = str(round(get_object_volume(object), 3))
    feature_name = object.name.split('.')[0]
    feature_name = feature_name.split('(')[0].strip(' ')
    print(feature_name)
    if volume_in_filename:
        file_name = '{}{}_{}.{}'.format(base_dir, object.name, volume_str, file_type)
    else:
        file_name = '{}{}.{}'.format(base_dir, feature_name, file_type)
    print("file name: " + file_name)
    return file_name

def generate_volume_model_file(shape_file, shrink_method='NEAREST_VERTEX', smooth_iterations=30, file_type='dae', delete=False):
    ''' 
    Imports the file into blender, creates convex hull, remeshes 
    and shrinks in specified way, then exports newly shrunk model 
    as the specified file type. 
    '''
    def _delete_original_and_hull():
        ''' deletes original model and hull '''
        original.select_set(state=True)
        bpy.ops.object.delete(use_global=False)

    bpy.ops.importgis.shapefile(filepath=shp, shpCRS=shpCRS)
    convex_hull, original = create_hull()
    obj = remesh(convex_hull, original, shrink_method)
    singular_select(obj)
    output_path = create_output_file_name(base_dir, obj, shrink_method, smooth_iterations, file_type)
    if file_type == 'stl':
        bpy.ops.export_mesh.stl(filepath=output_path, use_selection=True)
    if file_type == 'dae':
        bpy.ops.wm.collada_export(filepath=output_path, selected=True)
    if delete:
        _delete_original_and_hull()
    bpy.ops.geoscene.clear_georef()

if __name__ == '__main__':
    # change the 'base_dir' line quotes to match the folder path where all the .shp files are on your PC.
    # The directory needs to include all the files related to the .shp file.
    base_dir = r"C:\Users\VR Backpack\Desktop\reintros\\"
    shapefiles = glob.glob(base_dir + '*.shp')
    for shp in shapefiles:
        generate_volume_model_file(shape_file=shp, delete=delete_after_export)
        # generate_volume_model_file(shape_file=shp, shrink_method='NEAREST_SURFACEPOINT', delete=delete_after_export)
        # TODO: May need to do something regarding multipatches?
        # TODO: adding a workflow which smooths out big extrusions such as in F142. Potentially using Opensubdiv and catmull clark subdivision.
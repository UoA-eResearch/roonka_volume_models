import glob
import bpy
import bmesh
from mathutils import Vector, Matrix


# subdivide_amount = 1

# TODO: importing shapefile programmatically https://blender.stackexchange.com/questions/52216/blendergis-import-call-from-python-script

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
    copy.name = "%s (convex hull)" % ob.name
    copy.data = ch
    scene.objects.link(copy)
    return copy, ob
    
def remesh(obj, original):
    ''' remeshes a convex hull with smoothing settings to around 8 octotree '''
    bpy.context.scene.objects.active = obj

    # TODO: separate into separate function
    remesher = obj.modifiers.new(name="Remesh", type="REMESH")
    remesher.octree_depth = 6
    remesher.mode = "SMOOTH"
    remesher.use_smooth_shade = True
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh")

    # TODO: separate into separate function
    shrinker = obj.modifiers.new(name="Shrinkwrap", type="SHRINKWRAP")
    shrinker.target = bpy.data.objects[original.name]
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Shrinkwrap")

    # TODO: separate into separate function
    smoother = obj.modifiers.new(name="Smooth", type="SMOOTH")
    smoother.factor = 0.9
    smoother.iterations = 30
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Smooth")

base_dir = '/home/warrick/Desktop/roonka_features/'
shapefiles = glob.glob(base_dir + '*.shp')
for shp in shapefiles:
    bpy.ops.importgis.shapefile(filepath=shp)
    convex_hull, original = create_hull()
    remesh(convex_hull, original)
    bpy.ops.export_mesh.stl(filepath=base_dir + bpy.context.scene.objects.active.name + '-TEST.stl')


# bpy.ops.importgis.shapefile(filepath="/home/warrick/Desktop/roonka_features/F157.shp")
# convex_hull, original = create_hull()
# remesh(convex_hull, original)

# bpy.ops.mesh.subdivide(number_cuts=3)
# alternative method
# remesh up with increased octo-tree (around 8+), apply, shrinkwrap + apply -> smooth in various ways but most importantly using regular smooth, high repititions, factor that seemed to work nicely was /0.8
# tl;dr: remesh(octo=8, type=smooth) -> shrinkwrap(mode=surface) -> smooth(factor=0.8, repeat=30-100)
#sometimes smooth way more than that even
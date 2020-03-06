import glob
import bpy
import bmesh
from mathutils import Vector, Matrix

'''
Description: Creates a singular convex hull from a selected object in the scene.
'''

# Configure these settings as required
delete_after_export = False
octree_depth = 7

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


create_hull()
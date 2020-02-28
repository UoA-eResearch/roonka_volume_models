import bpy
import glob
import bmesh
from mathutils import Vector, Matrix

'''
Description: Creates a convex hull from a shapefile containing a series of layers
Blender version: 2.79b
'''

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
    scene.objects.link(copy)
    # bpy.ops.outliner.object_operation(TYPE="DESELECT")
    return copy, ob

create_hull()
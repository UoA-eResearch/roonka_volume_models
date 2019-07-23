import bpy
import bmesh
from mathutils import Vector, Matrix

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
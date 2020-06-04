
import bpy

'''
Description: Helper methods
Blender version: 2.79b
'''

class Helper:

    @classmethod
    def edit_mode():
        bpy.ops.object.mode_set(mode='EDIT')


    @classmethod
    def obj_mode():
        bpy.ops.object.mode_set(mode='OBJECT')

    @classmethod
    def set_active(obj):
        return bpy.context.active_object = obj

    @classmethod
    def get_active():
        return bpy.context.active_object


    @classmethod
    def get_max_vertex(vertices, axis):
        ''' returns max vertex from a list of vertices'''
        return sorted(vertices, reverse=True, key=lambda v: abs(v.co[axis]))[0]
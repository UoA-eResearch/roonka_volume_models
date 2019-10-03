
import bpy

def deselect_all():
    bpy.ops.object.select_all(action='DESELECT')


# edit to match your desired output directory
output_dir = '/Users/wcor690/Desktop/'

for ob in bpy.data.objects:
    deselect_all()
    ob.select = True
    output_filename = ob.name + ".dae"
    bpy.ops.wm.collada_export(filepath=output_dir + output_filename, selected=True)
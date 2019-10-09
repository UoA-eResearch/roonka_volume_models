
def create_bounding_box():
    print("creating bounding box")
    obj = bpy.context.object
    me = bpy.context.object.data
    edit_mode()
    bm = bmesh.from_edit_mesh(me)
    bm.faces.ensure_lookup_table()
    bm.verts.ensure_lookup_table()
    bounding_box_center = obj.location

    # TODO: refactor into singular function
    max_x_position = sorted(bm.verts, reverse=True, key=lambda v: abs(v.co.x))
    max_y_position = sorted(bm.verts, reverse=True, key=lambda v: abs(v.co.y))
    max_z_position = sorted(bm.verts, reverse=True, key=lambda v: abs(v.co.z))

    max_x = round(abs(max_x_position[0].co.x))
    max_y = round(abs(max_y_position[0].co.y))
    max_z = round(abs(max_z_position[0].co.z))

    obj_mode()

    bpy.ops.mesh.primitive_cube_add(location=bounding_box_center)
    bpy.context.scene.objects.active.scale = (max_x, max_y, max_z)
    bounding_box = bpy.context.active_object
    bounding_box.name = 'bounding_box'
    return bounding_box
# bpy.ops.mesh.subdivide(number_cuts=3)
# alternative method
# remesh up with increased octo-tree (around 8+), apply, shrinkwrap + apply -> smooth in various ways but most importantly using regular smooth, high repititions, factor that seemed to work nicely was /0.8
# tl;dr: remesh(octo=8, type=smooth) -> shrinkwrap(mode=surface) -> smooth(factor=0.8, repeat=30-100)
#sometimes smooth way more than that even
# Notes

## todo

- [ ] refactor modifier additions
- [ ] convert to filetype suitable for use
- [ ] investigate removing erosion or large protusions e.g. in F142 vs F142b

## original approach

- bpy.ops.mesh.subdivide(number_cuts=3)

## current method

- remesh up with increased octree (around 8+), apply, shrinkwrap + apply -> smooth in various ways but most importantly using regular smooth, high repititions, factor that seemed to work nicely was /0.8
- tl;dr: remesh(octree type=smooth) -> shrinkwrap(mode=surface) -> smooth(factor=0.8, repeat=30-100)
- sometimes smooth way more than that even

## other potential methods

- create a cube, remesh, have it encapsulate the target shape, shrinkwrap. Doing so creates a different output due to the way the remeshing creates vertices.
- Josh asked if stepping could be removed. Using nearest vertex shrinkwrapping could be a potential solution.
- shrinkwrapping using project in both negative and positive passes of the z-axis. This is probably more suitable for Roonka in particular.

### pros and cons to continuous lines

- pro - doesn't have the stepped appearance
- consideration - if using convex hull the volumes calculated for irregular inputs might be a lot different.
- consideration - if using nearest vertex shrinkwrap the volumes will be less altered by irregularities but still probably more than the stepped version.
- con - might lead to different volume calculation (potentially smaller volumes)
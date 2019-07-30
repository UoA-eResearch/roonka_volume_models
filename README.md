# Roonka Volume Meshes

## How to use

1. Download this repository using either git or selecting the green 'clone or download' button on the repository main page.
2. Unzip the file and extract 'mesh_create.py' somewhere memorable and take note of the path as it's the script that will be run.
3. Launch Blender (script developed on Blender v2.79)
4. In Blender, split the scene view window in half and change the editor type from '3D View' to 'Text Editor'.
5. On the bottom of the text editor window, to the right of the file name, select the folder icon to open a new file.
6. Navigate to the extracted 'mesh_create.py' file from earlier to open it in the text editor.
7. Near the bottom of the file, find the line that starts with 'base_dir=' and edit the text within the quotes to equal the folder path where your .shp files are located. **Note: If your path includes backslashes, add an r before the quotes begin e.g. r'\<path\>'**
8. Save the edits to the file using the 'Text' menu in the text editor toolbar.
9. Select 'run script' from the bottom toolbar.
10. After some time processing, the .dae models should have been exported and can be located in the same folder as the path specified in the base_dir.

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

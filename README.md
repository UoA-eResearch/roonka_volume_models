# Roonka 3D Tools

## Sections

* Volume Creation from Layered Shapefiles
* Point selection using volumes

## How to use

### Volume Creation From Layered Shapefiles

#### Prerequisites

Currently this script has only been tested on versions 2.79 and 2.78 of Blender and does not yet work on Blender 2.8. Please make sure you have installed and enabled the add-ons '3D Printing Toolbox' and [BlenderGIS](https://github.com/domlysz/BlenderGIS) installed for the correct version of Blender.

#### How to install add-ons

Simply go to the link for the add-on and download the .zip file using the green clone/download button. In Blender, navigate to the preferences >> add-ons >> install and navigate to the .zip file that was downloaded earlier. Once installed you should have the add-on listed which can then be selected using the check box.

#### Set up and running

1. Download this repository using either git or selecting the green 'clone or download' button on the repository main page.
2. Unzip the file and extract 'mesh_create.py' somewhere memorable and take note of the path as it's the script that will be run.
3. Launch Blender (script developed on Blender v2.79)
4. In Blender, split the scene view window in half and change the editor type from '3D View' to 'Text Editor'.
5. On the bottom of the text editor window, to the right of the file name, select the folder icon to open a new file.
6. Navigate to the extracted 'mesh_create.py' file from earlier to open it in the text editor.
7. Near the bottom of the file, find the line that starts with 'base_dir=' and edit the text within the quotes to equal the folder path where your .shp files are located. **Note: If your path includes backslashes replace them with forward slashes, also add an 'r' before the quotes begin. Finally, if your path doesn't include a final trailing forward slash, add one to the end of the path  
    An example Linux path: base_dir = '/home/warrick/Desktop/roonka_features/'

    An example Windows path: r'C:/Users/username/Desktop/files_to_process/'
8. Save the edits to the file using the 'Text' menu in the text editor toolbar.
9. Select 'run script' from the bottom toolbar.
10. After some time processing, the .dae models should have been exported and can be located in the same folder as the path specified in the base_dir.

### Point Selection Using Volumes

#### Prerequesites

* Blender 2.79 **(Does not yet work with 2.8)**
* To import the artefacts shapefile you will need BlenderGIS installed like the volume creation script.
* Fiona - **note:** This is a python library. Blender uses it's own internal python. In order to install modules for Python, create a virtual environment to install fiona and attrs to, then copy those module folders into Blenders python modules directory.

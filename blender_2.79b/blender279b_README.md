# Roonka 2.79b Workflow Tools

## Version

Blender 2.79b

## Contents

* Volume Creation from Layered Shapefiles
* Point selection using volumes
* Trench Creation from point layers
* Point selection using convex hulls (Roonka Features)

## Volume Creation From Layered Shapefiles

### Description

Creates smooth 3D models with valid volumes from shapefiles containing multiple, stacked, 2D layers.

### Prerequisites

* Currently this script has only been tested on versions 2.79 and 2.78 of Blender and does not yet work on Blender 2.8. 
* Ensure you have installed and enabled the add-ons: 
* '3D Printing Toolbox'
* [BlenderGIS](https://github.com/domlysz/BlenderGIS) installed for the correct version of Blender.

### Installing add-ons

Simply go to the link for the add-on and download the .zip file using the green clone/download button. In Blender, navigate to the preferences >> add-ons >> install and navigate to the .zip file that was downloaded earlier. Once installed you should have the add-on listed which can then be selected using the checkbox.

### Usage

1. Download this repository using either git or selecting the green 'clone or download' button on the repository main page.
2. Unzip the file and extract 'mesh_create.py' somewhere memorable and take note of the path as it's the script that will be run.
3. Launch Blender.
4. In Blender, split the scene view window in half and change the editor type from '3D View' to 'Text Editor'.
5. On the bottom of the text editor window, to the right of the file name, select the folder icon to open a new file.
6. Navigate to the extracted 'mesh_create.py' file from earlier to open it in the text editor.
7. Near the bottom of the file, find the line that starts with 'base_dir=' and edit the text within the quotes to equal the folder path where your .shp files are located. **Note: If your path includes backslashes replace them with forward slashes, also add an 'r' before the quotes begin. Finally, if your path doesn't include a final trailing forward slash, add one to the end of the path. An example Linux path: base_dir = '/home/warrick/Desktop/roonka_features/'

    An example Windows path: ```r'C:/Users/username/Desktop/files_to_process/'```
8. Save the edits to the file using the 'Text' menu in the text editor toolbar.
9. Select 'run script' from the bottom toolbar.
10. After some time processing, the .dae models should have been exported and can be located in the same folder as the path specified in the base_dir.

## Point Selection Using Volumes

### Description

This script selects all artefacts that are within a selected volume (feature in the context of the Roonka project) and exports them to a shapefile.

### Prerequisites

* Blender 2.79b
* To import the artefacts shapefile you will need BlenderGIS installed like the volume creation script.
* Fiona - **note: This is a python library. Blender uses it's own internal python so pip install will not work.**
 * One way to install the modules is to install them into a virtual environment then copy the site-package directories to a location Blender's Python will find them.
 * Instructions for how to install modules to Blender's Python can be found here substituting 'bs4' for 'fiona' and 'attrs': <http://lacuisine.tech/2017/10/19/how-to-install-python-libs-in-blender-part-1/>.
* Once the modules are installed the script can be run.

### Usage

* Open up a text-editor window in Blender.
* Open the 'point_analysis.py' script in this repository.
* Edit the path variables for you desired output directory.
* __Make sure the 'Id' attribute of the points within the shapefile are unique values. I have included an updated Artefacts shapefile with unique Ids in the artefacts folder included.__
* Edit the shapefile path to match the location of the shapefile you are importing. This is for when we the script creates an edited clone of this shapefile. In this case it should be the path of the Artefacts shapefile.
* Import the Artefacts shapefile using BlenderGIS - specify import as separate objects so the points keep their GIS attributes.
* Select/or create a closed mesh that you wish to find points within.
* With the mesh selected, run the script.
* After this is run, the output shapefile should be found in the directory specified in the output path variable.

## Trench Rectangular Volumes

### Description

This script creates a model that contains a volume from multiple shapefiles that resemble stacked layers.

### Prerequisites

* Blender 2.79b

### Usage

* Open up 'trench_cuboid_volumes.py' in a text editor window in Blender
* Edit the output path line at the top of the file to a directory that suits you.
* Load in the shapefiles containing the points you wish to convert into a volume.
* Select the layers you wish to convert into a trench using 3D or outliner windows.
* Run the script.
* The trench volume will be generated in the scene and the output .dae file should be created at the output directory.

## Bulk Importer/Exporters

### Description

This script loads multiple files into the blender scene.

### Usage

* Open up the importer/exporter script.
* Change the file paths where comments have been added to suit your case.
* Run the script.

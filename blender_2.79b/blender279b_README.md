# Roonka 2.79b Workflow Tools

## Version

Blender 2.8

## Contents

* Volume Creation from Layered Shapefiles
* Point selection using volumes
* Trench Creation from point layers

## Volume Creation From Layered Shapefiles

### Description

Creates smooth 3D models with valid volumes from shapefiles containing multiple, stacked, 2D layers.

### Prerequisites

Currently this script has only been tested on versions 2.79 and 2.78 of Blender and does not yet work on Blender 2.8. Please make sure you have installed and enabled the add-ons '3D Printing Toolbox' and [BlenderGIS](https://github.com/domlysz/BlenderGIS) installed for the correct version of Blender.

### Installing add-ons

Simply go to the link for the add-on and download the .zip file using the green clone/download button. In Blender, navigate to the preferences >> add-ons >> install and navigate to the .zip file that was downloaded earlier. Once installed you should have the add-on listed which can then be selected using the checkbox.

### Usage

1. Download this repository using either git or selecting the green 'clone or download' button on the repository main page.
2. Unzip the file and extract 'mesh_create.py' somewhere memorable and take note of the path as it's the script that will be run.
3. Launch Blender 
4. In Blender, split the scene view window in half and change the editor type from '3D View' to 'Text Editor'.
5. On the bottom of the text editor window, to the right of the file name, select the folder icon to open a new file.
6. Navigate to the extracted 'mesh_create.py' file from earlier to open it in the text editor.
7. Near the bottom of the file, find the line that starts with 'base_dir=' and edit the text within the quotes to equal the folder path where your .shp files are located. **Note: If your path includes backslashes replace them with forward slashes, also add an 'r' before the quotes begin. Finally, if your path doesn't include a final trailing forward slash, add one to the end of the path  
    An example Linux path: base_dir = '/home/warrick/Desktop/roonka_features/'

    An example Windows path: ```r'C:/Users/username/Desktop/files_to_process/'```
8. Save the edits to the file using the 'Text' menu in the text editor toolbar.
9. Select 'run script' from the bottom toolbar.
10. After some time processing, the .dae models should have been exported and can be located in the same folder as the path specified in the base_dir.

## Point Selection Using Volumes

### Prerequisites

* Blender 2.79 
* To import the artefacts shapefile you will need BlenderGIS installed like the volume creation script.
* Fiona - **note: This is a python library. Blender uses it's own internal python so pip install will not work.**
  * One way to install the modules is to install them into a virtual environment then copy the site-package directories to a location Blender's Python will find them.
  * Instructions for how to install modules to Blender's Python can be found here substituting 'bs4' for 'fiona' and 'attrs': <http://lacuisine.tech/2017/10/19/how-to-install-python-libs-in-blender-part-1/>
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

Creates a model that contains a volume from multiple shapefiles that resemble stacked layers.

### Prerequesites

* Blender 2.79
e* Load in the layers you wish to connect.

### Usage

* Open up 'trench_cuboid_volumes.py' in a text editor window in Blender
* Edit the output path line at the top of the file to a directory that suits you.
* Load in the shapefiles containing the points you wish to convert into a volume.
* Select the layers you wish to convert into a trench using 3D or outliner windows
* Run the script
* The trench volume will be generated in the scene and the output .dae file should be created at the output directory.

## Bulk Importer/Exporters

### Usage

* Open up the importer/exporter
* Change the file paths where comments have been added to suit your case.
* Run the script

## ArcScene Desktop / ArcGIS Pro Model Converter

### Description

This script imports 3D Collada model files into ArcScene and ArcGIS as well as outputing a corresponding shapefile with supporting data files in the same directory as the models are located.

### Usage

* Open up ArcGIS Pro/ArcScene Desktop and create/open the scene you wish to use.
* In the toolbar there should be an icon that when hovered over says "Python" followed by some text. Click that and it should open up a window where you can paste/type in code to run in ArcScene.
* Move the folder containing all the .dae models to the ArcGIS folder that contains AddIns and other ArcGIS files. E.g  C:\Users\VR Backpack\Documents\ArcGIS.
* In the code, change the path to the folder where the ".dae" models are located. Make sure to keep the path within the r" " quotemarks and use the same backslashes as well as the final "\\" for the end of the path. It should match the formatting of the path existing in the code.
In the python window, paste in the import lines (lines 1-3) and press enter. You may need to press enter twice for the import statement to be run instead of just going to a new line in the python window.
* copy and paste inline 4 then press enter twice.
* Paste in lines 6-14 and press enter twice. There should be a lot of pausing as it loads in the models. Eventually you should see all the models loaded into the scene. You will also find all the shapefiles and their associated files in the original directory the .dae files were located as the output directory are the same as the input directory.
* If the script is to be rerun you will need to delete the existing shapefiles that are to be remade as well as their associated files as ArcScene doesn't allow duplicate files to be created.
## ArcScene Desktop/ArcGIS Pro Model Converter

### Prerequisites

* An ArcGIS Pro or ArcScene Desktop installation.

### Description

This script imports 3D Collada model files into ArcScene and ArcGIS as well as outputing a corresponding shapefile with supporting data files in the same directory as the models are located.

### Usage

* Open up ArcGIS Pro/ArcScene Desktop and create/open the scene you wish to use.
* In the toolbar there should be an icon that when hovered over says "Python" followed by some text. Click that and it should open up a window where you can paste/type in code to run in ArcScene.
* Move the folder containing all the .dae models to the ArcGIS folder that contains AddIns and other ArcGIS files. E.g  C:\Users\VR Backpack\Documents\ArcGIS.
* In the code, change the path to the folder where the ".dae" models are located. Make sure to keep the path within the r" " quotemarks and use the same backslashes as well as the final "\\" for the end of the path. It should match the formatting of the path existing in the code.
* Copy and paste the edited code into the python terminal, you may need to press enter multiple times for the code to execute. After some delay, the models will be loaded into the scene. You will also find all the shapefiles and their associated files in the original directory the .dae files were located as the output directory are the same as the input directory.
* If the script is to be rerun you will need to delete the existing shapefiles that are to be remade as well as their associated files as ArcScene doesn't allow duplicate files to be created.

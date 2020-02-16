# required imports
import time
import glob
import os

# Setting context
# arcgis pro
os.chdir(r"C:\Users\VR Backpack\Desktop\Warrick_Dataset")
# arcgis desktop
arcpy.env = r"C:\Users\VR Backpack\Desktop\Warrick Dataset"




# switch to desired time between imports if thrashing occurs.
delayTime = 0.5

# fixed problem of invalid table names as well as duplicate names when dealing with multiple files.
for idx, file in enumerate(glob.glob("*.dae")):
	arcpy.Import3DFiles_3d(r"C:\Users\VR Backpack\Desktop\Warrick_Dataset\\" + file, arcpy.ValidateTableName( r"C:\Users\VR Backpack\Documents\ArcGIS\Default.gdb\\" + str(idx)))
	time.sleep(delayTime)
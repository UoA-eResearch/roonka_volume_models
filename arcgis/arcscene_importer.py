# required imports
import time
import glob
import os
import arcpy

target_directory = r"C:\Users\VR Backpack\Desktop\Warrick_Dataset"
geo_db_directory = r"C:\Users\VR Backpack\Documents\ArcGIS\Default.gdb\\"

out_dir = r"C:\Users\VR Backpack\Documents\ArcGIS\Warrick_Dataset_n=10"

# Setting context
# arcgis pro
os.chdir(target_directory)
# arcgis desktop
arcpy.env = target_directory




# switch to desired time between imports if thrashing occurs.
# run a smaller batch and see the succeeded elapsed time as a guide for a minimum amount.
delayTime = 0.5

# fixed problem of invalid table names as well as duplicate names when dealing with multiple files.
for idx, file in enumerate(glob.glob("*.dae")):
	arcpy.Import3DFiles_3d(
		r"C:\Users\VR Backpack\Desktop\Warrick_Dataset\\" + file,
		arcpy.ValidateTableName(geo_db_directory + str(idx)
		))
	time.sleep(delayTime)

	# tried importing with added info other that input file and output file which resulted in corrupted import and corrupted subsequent imports. Issue was resolved by reverting to a blank scene.






	# worked using centroid file for out_dir set to dataset within arcgis docs. infile and outfile still target dir on deskop. No input needed for spatial reference (supposedly inferred from centroid shapefile.)
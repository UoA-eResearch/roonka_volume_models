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

# 	# worked using centroid file for out_dir set to dataset within arcgis docs. infile and outfile still target dir on deskop. No input needed for spatial reference (supposedly inferred from centroid shapefile.)
# 	for index, file in enumerate(glob.glob("*.dae")):
# ...     file_name, file_ext = file.split('.')
# ...arcpy.Import3DFiles_3d(
# 	in_files=target_dir + file,
# 	out_featureClass=target_dir + file_name + ".shp"


# for index, file in enumerate(glob.glob("*.dae")):
# ...     file_name, file_ext = file.split('.')
# ...     arcpy.Import3DFiles_3d(in_files=target_dir + file, out_featureClass=target_dir + file_name + ".shp", in_featureClass=out_dir + file_name + "_Centroid.shp", symbol_field="Feature")


# # Working -- with individual centroid field.
# for index, file in enumerate(glob.glob("*.dae")):
# ...     file_name, file_ext = file.split('.')
# ...     arcpy.Import3DFiles_3d(in_files=target_directory + file, out_featureClass=target_directory + file_name + ".shp", in_featureClass=out_dir + file_name + "_Centroid.shp", symbol_field="Feature")


# working -- attempt with master centroid file.
# placement seems to be the same in the import 3d files toolbox with the inferred spatial reference so seems like a good enough solution.

# Instructions
# Move the folder containing the .dae files into ArcGIS' main directory (typically ...\Documents\ArcGIS )
# change the target directory path to your path for this folder.
# change the out_dir to the path to the shapefile that contains all the centroids.
# download / move the 4326.prj file into the same folder as the .dae files as the import function calls the files from that location.
target_directory = r"C:\Users\VR Backpack\Desktop\Warrick_Dataset_n=78\\"
out_dir = r"C:\Users\VR Backpack\Documents\ArcGIS\Warrick_Dataset_n=78\\"
os.chdir(target_directory)
arcpy.env = target_directory
for index, file in enumerate(glob.glob("*.dae")):
		file_name, file_ext = file.split('.')
		arcpy.Import3DFiles_3d(
			in_files=target_directory + file,
			out_featureClass=target_directory + file_name + ".shp",
			in_featureClass=out_dir + "Feature_Centroids_n_78.shp",
			symbol_field="Feature",
			spatial_reference=out_dir + "4326.prj"
		)
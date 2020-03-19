import os
import glob
import arcpy

#  ========== EDIT BELOW ===========
directory = r"C:\Users\VR Backpack\Documents\ArcGIS\BulkEx2\\"
# include extension in feature centroid filename (e.g. .shp)
feature_centroids_filename = "Feature_MidPoints.shp"

# Alter the spatial reference path to your projection file
spatial_reference_path = "Coordinate Systems/Geographic Coordinate Systems/World/WGS 1984.prj"

# Alter the symbol field to match the column in your centroid shapefile that contains the model file names.
symbol_field = "File"

os.chdir(directory)
for index, file in enumerate(glob.glob("*.dae")):
		file_name, file_ext = file.split('.')
		arcpy.Import3DFiles_3d(
			in_files=directory + file,
			out_featureClass=directory + file_name + ".shp",
			in_featureClass=directory + feature_centroids_filename,
			# append dae if using Feature column
			symbol_field=symbol_field + ".dae",
			# spatial_reference=spatial_reference_path
			spatial_reference=spatial_reference_path
		)
		if index > 2:
			break



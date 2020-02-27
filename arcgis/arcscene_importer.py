import os
import glob
import arcpy
directory = r"C:\Users\VR Backpack\Documents\ArcGIS\Warrick_Dataset_n=78\\"
os.chdir(target_directory)
for index, file in enumerate(glob.glob("*.dae")):
		file_name, file_ext = file.split('.')
		arcpy.Import3DFiles_3d(
			in_files=directory + file,
			out_featureClass=directory + file_name + ".shp",
			in_featureClass=directory + "Feature_Centroids_n_78.shp",
			symbol_field="Feature",
			spatial_reference="Coordinate Systems/Geographic Coordinate Systems/World/WGS 1984.prj"
		)



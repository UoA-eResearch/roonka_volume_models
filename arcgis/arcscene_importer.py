# import arcypy
import os
import glob

# print("hi")

# C:\Users\VR Backpack\Desktop\Warrick_Dataset

os.chdir("C:\Users\VR Backpack\Desktop\Warrick_Dataset")
all_files = glob.glob("*")
# print(all_files)

for file in glob.glob("*.dae"):
	arcpy.Import3DFiles_3d(file, "C:\Users\VR Backpack\Documents\ArcGIS\default.gdb\t")


	# arcpy.Import3DFiles_3d(r"C:\Users\VR Backpack\Desktop\Warrick_Dataset\F025b.dae", r"C:\Users\VR Backpack\Documents\ArcGIS\Default.gdb\t")
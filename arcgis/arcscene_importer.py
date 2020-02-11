# import arcypy
import os
import glob

# print("hi")

# C:\Users\VR Backpack\Desktop\Warrick_Dataset

print(r"C:/blay/" + "hi")

# os.chdir("C:\Users\VR Backpack\Desktop\Warrick_Dataset")
# all_files = glob.glob("*")
# # print(all_files)

base = r"C:\Users\VR Backpack\Desktop\Warrick_Dataset\*.dae"
for file in glob.glob(r"C:\Users\VR Backpack\Desktop\Warrick_Dataset\*.dae"):
	str = r"""C:\Users\VR Backpack\Desktop\Warrick_Dataset\\""" + file
	print(os.path.join(r"""Users\VR Backpack\Desktop\Warrick_Dataset\\""", file))
	arcpy.Import3DFiles_3d(os.path.join(r"""Users\VR Backpack\Desktop\Warrick_Dataset\\""", file), r"C:\Users\VR Backpack\Documents\ArcGIS\Default.gdb\t")

for file in glob.glob(r"C:\Users\VR Backpack\Desktop\Warrick_Dataset\*.dae"): str = r"""C:\Users\VR Backpack\Desktop\Warrick_Dataset\\""" + file arcpy.Import3DFiles_3d(os.path.join(r"""Users\VR Backpack\Desktop\Warrick_Dataset\\""", file), r"C:\Users\VR Backpack\Documents\ArcGIS\Default.gdb\t"


# for file in glob.glob("*.dae"):
# 	arcpy.Import3DFiles_3d(file, "C:\Users\VR Backpack\Documents\ArcGIS\default.gdb\t")


# worked
# arcpy.Import3DFiles_3d(r"C:\Users\VR Backpack\Desktop\Warrick_Dataset\F025b.dae", r"C:\Users\VR Backpack\Documents\ArcGIS\Default.gdb\t")


# attempt 2 - iterative
# for file in glob.glob("*.dae"): arcpy.Import3DFiles_3d(r"C:\Users\VR Backpack\Desktop\Warrick_Dataset\" + file, r"C:\Users\VR Backpack\Documents\ArcGIS\Default.gdb\o"




for file in glob.glob("*.dae"):
...     arcpy.Import3DFiles_3d(r"C:\Users\VR Backpack\Desktop\Warrick_Dataset\\" + file, r"C:\Users\VR Backpack\Documents\ArcGIS\Default.gdb\x") 


# replace with path to folder containing shape files
arcpy.env = r"C:\Users\VR Backpack\Desktop\Warrick Dataset"
# fixed problem of invalid table names as well as duplicate names when dealing with multiple files.
for idx, file in enumerate(glob.glob("*.dae")):
...     arcpy.Import3DFiles_3d(r"C:\Users\VR Backpack\Desktop\Warrick_Dataset\\" + file, arcpy.ValidateTableName( r"C:\Users\VR Backpack\Documents\ArcGIS\Default.gdb\\" + str(idx)))
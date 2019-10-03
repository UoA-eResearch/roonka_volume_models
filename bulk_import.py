import bpy
import glob


def import_shapefiles(base_dir):
    paths = glob.glob(base_dir + '*.shp')
    for path in paths:
        bpy.ops.importgis.shapefile(filepath=path)


def import_collada_files(base_dir):
    paths = glob.glob(base_dir + '*.dae')
    for path in paths:
        bpy.ops.wm.collada_import(filepath=path)


# change this to the path of the directory/folder containing all the files you wish
# to import
base_dir = '/home/warrick/Desktop/roonka_features/'

# change this to shapefile or collada depending on what you wish to import.
import_file_type = 'shapefile'

if import_file_type is 'shapefile':
    import_shapefiles(base_dir)
elif import_file_type is 'collada':
    import_collada_files(base_dir)
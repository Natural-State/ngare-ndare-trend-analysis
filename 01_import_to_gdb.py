import arcpy
import os
import glob
import re
import time

# Define directories
proj_dir = r"H:\My Drive\ArcPro projects\Ngare Ndare HW"
gee_layers_dir = os.path.join(proj_dir, "gee_layers")
gdb_dir = os.path.join(proj_dir, "Ngare_Ndare_HW.gdb")

# Read layer list from GEE folder
# lyr_pattern = "*Ngare_Ndare*.tif"
# raster_list = glob.glob(os.path.join(gee_layers_dir, lyr_pattern))
# print(raster_list)

# Read subset for just trend analysis over custom temporal period
lyr_pattern = "*2015_to_2020*.tif"
raster_list = glob.glob(os.path.join(gee_layers_dir, lyr_pattern))
print(raster_list)

arcpy.env.workspace = gdb_dir
# arcpy.Delete_management("temp_ras")
# temp_ras_list = arcpy.ListRasters()

# x = raster_list[0]
for x in raster_list:
    start_time = time.time()
    arcpy.CopyRaster_management(in_raster=x, out_rasterdataset="temp_ras", nodata_value="nan")
    match = re.search(r'\\([^\\]*)\.tif$', x)
    copy_ras_name = os.path.join(gdb_dir, match.group(1))
    arcpy.Rename_management(in_data="temp_ras", out_data=copy_ras_name)
    end_time = time.time()
    print("IMPORT COMPLETE: " + copy_ras_name)
    print("TIME TO IMPORT: " + str(end_time - start_time))


import arcpy
import arcpy
import os
import re
import pandas
from datetime import datetime

# https://pro.arcgis.com/en/pro-app/latest/arcpy/mapping/map-class.htm
# The Map object is the primary object for referencing and managing layers and tables within an ArcGIS Pro project.

proj_dir = r"H:\My Drive\ArcPro projects\Ngare Ndare HW"
gee_layers_dir = os.path.join(proj_dir, "gee_layers")
gdb_dir = os.path.join(proj_dir, "Ngare_Ndare_HW.gdb")

os.getcwd()
arcpy.env.overwriteOutput = True

arcpy.env.workspace = gdb_dir
aprx = arcpy.mp.ArcGISProject("CURRENT")
Map = aprx.listMaps("Map")[0]

ras_list = arcpy.ListRasters("*tree_cov")
ras_list.sort()

ras_list = arcpy.ListRasters("*non_tree_veg_cov")
ras_list.sort()

ras_list = arcpy.ListRasters("*nonveg*")
ras_list.sort()

ras_list = arcpy.ListRasters("*pvalue*")
ras_list.sort()

print(ras_list)

for x in ras_list:
    print(x)
    lyr_path = os.path.join(gdb_dir, x)
    normalized_path = os.path.normpath(lyr_path)
    Map.addDataFromPath(normalized_path)

lyr_list = Map.listLayers("*tree_cov")
lyr_names = [layer.name for layer in lyr_list]
symbology_file = r"H:\My Drive\ArcPro projects\Ngare Ndare HW\tree_cov.lyrx"
for i in lyr_list:
    arcpy.ApplySymbologyFromLayer_management(i, symbology_file)

lyr_list = Map.listLayers("*non_tree_veg_cov")
lyr_names = [layer.name for layer in lyr_list]
symbology_file = r"H:\My Drive\ArcPro projects\Ngare Ndare HW\non_tree_veg_cov.lyrx"
for i in lyr_list:
    arcpy.ApplySymbologyFromLayer_management(i, symbology_file)

lyr_list = Map.listLayers("*nonveg*")
lyr_names = [layer.name for layer in lyr_list]
symbology_file = r"H:\My Drive\ArcPro projects\Ngare Ndare HW\nonveg_cov.lyrx"
for i in lyr_list:
    arcpy.ApplySymbologyFromLayer_management(i, symbology_file)

lyr_list = Map.listLayers("*pvalue*")
lyr_names = [layer.name for layer in lyr_list]
symbology_file = r"H:\My Drive\ArcPro projects\Ngare Ndare HW\p_value.lyrx"
for i in lyr_list:
    arcpy.ApplySymbologyFromLayer_management(i, symbology_file)

lyr_list = Map.listLayers("*sens_slope*")
lyr_names = [layer.name for layer in lyr_list]
symbology_file = r"H:\My Drive\ArcPro projects\Ngare Ndare HW\sens_slope.lyrx"
for i in lyr_list:
    arcpy.ApplySymbologyFromLayer_management(i, symbology_file)

lyr_list = Map.listLayers("*significant*")
lyr_names = [layer.name for layer in lyr_list]
symbology_file = r"H:\My Drive\ArcPro projects\Ngare Ndare HW\significant.lyrx"
for i in lyr_list:
    arcpy.ApplySymbologyFromLayer_management(i, symbology_file)
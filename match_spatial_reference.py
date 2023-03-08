"""
    This function applies the spatial reference of one input data source
    (most likely TDS data) to another data source (most likely a shapefile
    like dvof_source or gait shapefile). The spatial reference of the second
    parameter will be applied to the first parameter.
"""
# necessary imports
import arcpy as ap
from arcpy import AddMessage as write

def check_set_spatial_reference(shapefile, tds_data):
    write("Checking Spatial Reference...")
    shp_desc = ap.Describe(shapefile)
    tds_desc = ap.Describe(tds_data)
    shp_sr = shp_desc.spatialReference
    tds_sr = tds_desc.spatialReference

    if shp_sr.name != tds_sr.name:
        write("Applying {} projection to shapefile...".format(tds_sr.name))
        ap.DefineProjection_management(shapefile, tds_sr)
    else:
        write("Shapefile and TDS projection match confirmed: {}".format(tds_sr.name))
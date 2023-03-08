"""
    This function takes in a dictionary of feature layers.
    The keys of the dictionary are "Points" and "Surfaces".
    This function will create a list of the "Points" layers
    and then add to that list each "Surfaces" layer after 
    converting it to a point feature class. It will then return
    the list of point feature classes.
"""
# necessary imports
import arcpy as ap
from arcpy import AddMessage as write



def convert_tds_srf_to_pnt(layer_dict):
    working_list = layer_dict['Points']
    if len(layer_dict['Surfaces']) == 0:
        write("No qualifying surface features present.")
        return working_list
    else:
        write("Surface features with qualifying height present. Preparing for processing...")
        for lyr in layer_dict['Surfaces']:
            name = lyr+"_pnts"
            fc_path = "in_memory\\{}".format(name)
            pnt_type = "CENTROID"
            ap.management.FeatureToPoint(lyr, fc_path, pnt_type)
            working_list.append(fc_path)
            write("{} converted to Points.".format(lyr))
    return working_list
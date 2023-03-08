import arcpy as ap

'''
    a function that allows for cleaner code
    Input: Feature Class or Feature Layer
    Output: Integer representing number of features in the input
'''

def get_count(fc_layer):
    results = int(ap.GetCount_management(fc_layer).getOutput(0))

    return results
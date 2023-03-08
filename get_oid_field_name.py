"""
    This function was made to get the OID field name
    of a feature class/feature layer in which it may 
    not be clear if the input features are contained 
    within a file geodatabase or a shapefile.

    The assumption is that the function will be called
    only on one feature class in the course of the program
    and that every subsequent run will be retrieving the same
    information.
"""


def get_oid_field_name(input_features, oid_name=[]):
    if oid_name == []:
        field_list = ap.ListFields(input_features, field_type='OID')
        name = field_list[0].name
        oid_name.append(name)
        return name
    else:
        return oid_name[0]
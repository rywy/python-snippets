#-------------------------------------------------------------------------------
# Name:        arcgis truncate feature layer
# Purpose:     ArcGIS API truncate all records if they exist in feature layer
#
# Author:      Ryan Nosek

#-------------------------------------------------------------------------------

import os, sys
from arcgis.gis import GIS
from arcgis.features import FeatureLayer

try:
    gis = GIS("https://your-org.maps.arcgis.com/", "username", "pw")
    fl_item = gis.content.get('itemid############')
    fl_item_LayerID = FeatureLayer.fromitem(fl_item, layer_id=0)
    qry = fl_item_LayerID.query(where='1=1', returnCountOnly='true')
    if qry > 0:
        fl_item_LayerID.manager.truncate()

except Exception as e:
    trace_back = sys.exc_info()[2]
    line = trace_back.tb_lineno
    print ("Error "  + str(e) + ". Near line: " + str(line))



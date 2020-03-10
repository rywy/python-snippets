#-------------------------------------------------------------------------------
# Name:        Soda to ArcGIS ETL
# Purpose:     Query SODA API to get latest records, load into a hosted feature Service
#   1st step: setup your hosted feature service by publishing the same geojson file
#   (schema, file name) that will be later used/referenced in this workflow.
#   2nd step: **CONFIGURE** variables below for your web GIS, SODA api query, etc.
#   3rd step: Schedule this script as a task and let it auto update
# Author:      Ryan Nosek - borrowed heavily from Piyali Kundu and Sean McGinnis
#
#-------------------------------------------------------------------------------

import urllib, json, requests, datetime, os, sys
from datetime import datetime
from datetime import timedelta
from datetime import date
from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection
from arcgis.features import FeatureLayer


try:
    # **CONFIGURE** your web GIS
    gis = GIS("https://your-org-or-enterprise", "username", "password")
    target_item_featureLayer = gis.content.get('uniqueItemId')

    # **CONFIGURE** Socrata Variables
    item_id = "v6vf-nfxy"
    # Main Socarata URL
    socarata_url = "https://data.cityofchicago.org/"
    # Note the default is 1,000 and max is 50,000
    max_records = "50000"
    # Order by Date, desc
    order_by_date = "created_date%20DESC"

    #  **CONFIGURE** additional variables specific to your SODA item
    call_type = "sr_short_code%20!=%20%27311IOC%27"
    no_dupes = "duplicate%20=%20%27False%27"
    status_open = "status%20=%20%27Open%27"
    # Note: Null geometries exist in 311 data; hack here ask for no null's in fields
    # containing geometries
    null_geom = "x_coordinate%20is%20not%20null%20and%20latitude%20is%20not%20null%20"

    # Script Defined Variables
    # Resource URL
    resource_url = socarata_url + "resource/" + item_id + ".geojson"
    # Date Handling
    # Number of days for data
    day_count = 14
    total_days = day_count + 1
    today = date.today()
    begin_date = today - timedelta(days = total_days)
    # adding 1 day to ensure we capture records created today
    end_date = today + timedelta(days = 1)

##    print("Begin Date: " + str(begin_date))
##    print("End Date: " + str(end_date))
##    print("URL: " + resource_url)

    # NOTE(helper): this is what an un-serialized soda api request looks like:
    # https://data.cityofchicago.org/resource/v6vf-nfxy.json?$limit=50000&$where=sr_type != '311IOC' and duplicate = 'False' and status = 'Open' and x_coordinate is not null

    # **CONFIGURE** modify based on your SODA item properties and query defined above
    # construct the soda api url query, serialized
    query_url = resource_url + "?$limit=" + max_records + "&$order=" + order_by_date + "&$where=" + call_type + "%20and%20" + no_dupes + "%20and%20" + status_open + "%20and%20" + null_geom + "and%20created_date%20between%20%27" + str(begin_date) +"%27%20and%20%27" + str(end_date) +"%27"

    # Make the request to the socarata item
    socrata_response = requests.get(query_url).json()

##    print(socrata_response)
##    print(query_url)
##    print("Records returned: " + str(len(socrata_response)))

    with urllib.request.urlopen(query_url) as url:
        data = json.loads(url.read().decode())

    # **CONFIGURE** create the directory on your filesystem, then enter path below
    os.chdir('C:/jsontest')

    # **CONFIGURE** file name
    with open('soda2arcgis_chi311.geojson', 'w') as f:
        json.dump(data, f)

    # **CONFIGURE** full file path
    local_json_file = 'C:/jsontest/soda2arcgis_chi311.geojson'

    # prep web GIS for
    target_featureLayer_Collection = FeatureLayerCollection.fromitem(target_item_featureLayer)
##    target_featureLayer = FeatureLayer.fromitem(target_item_featureLayer, layer_id=0)

    json_data = open(local_json_file)
    data2 = json.load(json_data)
##    print("number of records: " + str(len(data2['features'])))

    if len(data2['features'])>0:
        target_featureLayer_Collection.manager.overwrite(local_json_file)
##        print("success overwriting")

except Exception as e:
    trace_back = sys.exc_info()[2]
    line = trace_back.tb_lineno
    print ("Error "  + str(e) + ". Near line: " + str(line))


# python-snippets
python snippets useful in different workflow. reduce reuse recycle

<h3>soda2arcgis_schedtask.py</h3>Configures a query against a SODA API item from current timestamp backwards x amount of days; takes response then ETL into ArcGIS feature layer. This particular script expects featurelayer item in ArcGIS to already exist with the same schema and filename*. *Since we are doing an Overwrite operation (not append), the filenameand type must match the original filename that created the ArcGIS featurelayer. Meant to be used as a scheduled task, producing near-realtime retreival of information from a SODA API item.  

<h3>arcgis_truncateFeatureLayer.py</h3>Truncates all features in a service. Meant to be run as a scheduled task.  

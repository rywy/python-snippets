# python-snippets
python snippets useful in different workflow. reduce reuse recycle

soda2arcgis_schedtask - configure a query against a SODA API item and ETL into ArcGIS feature layer. This particular script expects featurelayer item in ArcGIS to already exist with the same schema and filename*. *Since we are doing an Overwrite operation (not append), the filename must match the original filename that created the ArcGIS featurelayer. Meant to be used as a scheduled task, producing near-realtime retreival of information from a SODA API item.  

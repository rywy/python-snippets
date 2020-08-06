# python-snippets
Various python snippets to help make the world a better place.

<h3>soda2arcgis_schedtask.py</h3>Configures a query against a SODA API item from current timestamp backwards x amount of days; takes the SODA JSON response and extracts, transforms and loads into an ArcGIS feature layer. This particular script expects the featurelayer item in ArcGIS to already exist with the same schema and filename*. *Since we are doing an Overwrite operation (not append), the filename and type must match the original filename that created the ArcGIS featurelayer*. Meant to be used as a scheduled task, producing near-ish realtime retreival of information from a SODA API item and ETLing into ArcGIS Hosted Feature Layer.

<h3>arcgis_truncateFeatureLayer.py</h3>Truncates all features in a service. Meant to be run as a scheduled task.  

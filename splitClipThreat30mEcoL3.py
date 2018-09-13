import arcpy, os

arcpy.env.workspace = r"Z:\projects\GAP\DataReleaseCONUS\data" # Where the clip shapefile and input raster are stored
outputWorkspace = r"Z:\projects\GAP\DataReleaseCONUS\data\temp" # Where the output images will be stored
arcpy.env.overwriteOutput = True

rasterlist = arcpy.ListRasters() # Get a list of input rasters

clipShapefile = r"us_eco_l3_no_st_dissolve.shp" # Clip shapefile

# Create set of FIDs in the clip shapefile
clipShapes = set()
with arcpy.da.SearchCursor(clipShapefile, ['ID']) as cursor: #NEED to add an ID column that = US_L3CODE? or just change ID below
    for row in cursor:
        clipShapes.add(row[0])

# Loop through input rasters, and clip by each shape in the input shapefile
for raster in rasterlist:
    rastername, rasterext = os.path.splitext(raster)
    for i in clipShapes:
        j=str(i)
        print j 
        j=j.zfill(2) # pads 1-9 with a 0 for filenaming
        newRaster = "{}_clip_{}.tif".format(rastername, j)
        newRasterPath = os.path.join(outputWorkspace, newRaster)
        if arcpy.Exists('clipLayer'): # Remove existing 'clipLayer' feature layer if it still exists for some reason
            arcpy.Delete_management('clipLayer')
        arcpy.MakeFeatureLayer_management(clipShapefile, 'clipLayer', ' "ID" = {}'.format(i)) #create a layer with only polygon i
        arcpy.Clip_management(raster, "#", newRasterPath, 'clipLayer', "0", "ClippingGeometry") #clip based on layer, clipping geometry will use the polygon extent only
        arcpy.Delete_management('clipLayer')

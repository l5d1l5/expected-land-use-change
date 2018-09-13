# Name: threatCalc.py
# Description: calculates 'threat' from land use change projections
# Requirements: Spatial Analyst Extension
# Author: Jason Kreitler
# Comments: takes 270m input of "threat.tif" and resammples to 30m, 
# tabulates area of each class within each L3 ecoregion, cleans up results table. 
##########################################################################

import arcpy, os 
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.overwriteOutput = True
env.workspace = "Z:/projects/GAP/DataReleaseCONUS/data/temp"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")
rasterlist = arcpy.ListRasters() # Get a list of input rasters

# now loop through rasters in /data/temp and tabulate area 
# of each ecological system (or other) that falls in a threat class

#global values
inZoneData = r"W:\Projects\GAP\Nat_GAP_LandCover\natgaplandcov_v2_2_1.img"
zoneField = "ECOLSYS_LU" #can change to different types

# # Loop through input rasters, 
for raster in rasterlist:
    rastername, rasterext = os.path.splitext(raster)
    inClassData = raster
    classField = "VALUE" 
    outTable = os.path.join(env.workspace, "ecolSys_" + rastername + ".dbf")
    processingCellSize = 30
    arcpy.env.snapRaster = raster
    arcpy.env.extent = raster 
    L3eco=rastername[-2:] #last 2 digits of the name (doesn't have file ext)
    expression = str(L3eco) #make it an expression for calculate field below
    
    if os.path.isfile(outTable):
        print L3eco + "...is already done"    
    else:
    	print "working on..." + L3eco 
    	# Execute TabulateArea
    	TabulateArea(inZoneData, zoneField, inClassData, classField, outTable, processingCellSize)

    	# work on output table, add 8 field names, 
    	arcpy.AddField_management(outTable, "L3eco", 'TEXT')
    	arcpy.AddField_management(outTable, "NoThreat", 'FLOAT')
    	arcpy.AddField_management(outTable, "LowThreat", 'FLOAT')
    	arcpy.AddField_management(outTable, "MedThreat", 'FLOAT')
    	arcpy.AddField_management(outTable, "HighThreat", 'FLOAT')
    	arcpy.AddField_management(outTable, "AllThreat", 'FLOAT')
    	arcpy.AddField_management(outTable, "Total", 'FLOAT')
    	arcpy.AddField_management(outTable, "Percent", 'FLOAT')
    	
    	# convert to Ha, sum, %
    	arcpy.CalculateField_management(outTable, "NoThreat", "!VALUE_1!*0.0001", "PYTHON_9.3") 
    	arcpy.CalculateField_management(outTable, "LowThreat", "!VALUE_2!*0.0001", "PYTHON_9.3")
    	arcpy.CalculateField_management(outTable, "MedThreat", "!VALUE_3!*0.0001", "PYTHON_9.3")
    	arcpy.CalculateField_management(outTable, "HighThreat", "!VALUE_4!*0.0001", "PYTHON_9.3")
    	arcpy.CalculateField_management(outTable, "AllThreat", "sum([!LowThreat!, !MedThreat!, !HighThreat!])", "PYTHON_9.3")
    	arcpy.CalculateField_management(outTable, "Total", "sum([!NoThreat!,!LowThreat!, !MedThreat!, !HighThreat!])", "PYTHON_9.3")
    	arcpy.CalculateField_management(outTable, "Percent", "(!AllThreat!/!Total!)*100","PYTHON_9.3")
    	arcpy.CalculateField_management(outTable, "L3eco", '"'+expression+'"',"PYTHON_9.3")

# now clean up the tables by merging to one
masterTable=r'Z:\projects\GAP\DataReleaseCONUS\data\temp\masterTable.dbf'
dbfList = arcpy.ListTables()
arcpy.Merge_management(dbfList,masterTable)

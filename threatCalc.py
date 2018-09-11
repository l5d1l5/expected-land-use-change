# Name: threatCalc.py
# Description: calculates 'threat' from land use change projections
# Requirements: Spatial Analyst Extension
# Author: Jason Kreitler
# Comments: takes 270m input of "threat.tif" and resammples to 30m, 
# tabulates area of each class within each L3 ecoregion, cleans up results table. 
##########################################################################

import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.overwriteOutput = True
env.workspace = "Z:/projects/GAP/DataReleaseCONUS/data"


# Set local variables
inZoneData = "us_eco_l3_no_st.shp"
zoneField = "US_L3CODE"
inClassData = "Threat30m.tif"
classField = "VALUE"
outTable = "Threat30m_L3ecoregions.dbf"
processingCellSize = 30

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

arcpy.Resample_management("Threat.tif","Threat30m.tif","30","NEAREST")

# Execute TabulateArea
TabulateArea(inZoneData, zoneField, inClassData, classField, outTable, processingCellSize)

# work on output table, add 7 field names, 
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


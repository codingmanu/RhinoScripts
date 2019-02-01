#---------------------------------------------------------------------------------------------#
# Copyright Manuel Gomez (2019)                                                               #
#                                                                                             #
# This script selects all polysurfaces with volume smaller than the one indicated by the      #
# user.																					      #
#                                                                                             #
#---------------------------------------------------------------------------------------------#
# Create button in Rhino and add this command:                                                #
#      ! _-RunPythonScript "SelectSmallerThanVolume.py"                                       #
#---------------------------------------------------------------------------------------------#
# Version 1.0 (2019-01-31)                                                                    #
#    - Initial rev.                                                                           #
#---------------------------------------------------------------------------------------------#


import rhinoscriptsyntax as rs
import Rhino

def getUnitSystemDescription():
        unitSystemInt = rs.UnitSystem()

        if unitSystemInt == 2:
            return "mm3"
        elif unitSystemInt == 3:
            return"cm3"
        elif unitSystemInt == 4:
            return "m3"
        elif unitSystemInt == 8:
            return "in3"
        elif unitSystemInt == 9:
            return "ft3"

maxVolume = rs.GetReal("Max Volume in " + getUnitSystemDescription())

object_ids = []
object_ids = rs.ObjectsByType(16)

for object_id in object_ids:
    #check to see if the object is closed before calculating volume
    if rs.IsObjectSolid(object_id):
        blockVolume=rs.SurfaceVolume(object_id)[0]
        if blockVolume < maxVolume:
        	rs.SelectObject(object_id)


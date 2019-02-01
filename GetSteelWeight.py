#---------------------------------------------------------------------------------------------#
# Copyright Manuel Gomez (2019)                                                               #
#                                                                                             #
# This script calculates volume and translates to weight for steel density (0.284 lbs/in3)    #
#                                                                                             #
#---------------------------------------------------------------------------------------------#
# Create button in Rhino and add this command:                                                #
#      ! _-RunPythonScript "GetSteelWeight.py"                                            #
#---------------------------------------------------------------------------------------------#
# Version 1.0 (2019-01-20)                                                                    #
#    - Initial rev.                                                                           #
#---------------------------------------------------------------------------------------------#

import rhinoscriptsyntax as rs

if rs.UnitSystem() != 8:
    print("Units should be set to inches.")
    exit()

object_ids = []
object_ids = rs.SelectedObjects()

while not object_ids:
    object_ids = rs.GetObjects("Select some closed surfaces or polysurfaces",8+16)

#loop between objects

totalVolume = 0.0

for object_id in object_ids:
    #check to see if the object is closed before calculating volume
    if rs.IsObjectSolid(object_id):
        blockVolume=rs.SurfaceVolume(object_id)
        totalVolume = totalVolume + blockVolume[0]
    else:
        print "Object is not closed"

totalWeight = totalVolume * 0.284

print "The volume is " + "%.2f" % totalVolume + "sq.in"
print "The weight is " + "%.2f" % totalWeight + "lbs"
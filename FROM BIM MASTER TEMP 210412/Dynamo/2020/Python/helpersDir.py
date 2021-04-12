# Importing Reference Modules
import clr
clr.AddReference('ProtoGeometry')
import Autodesk
from Autodesk.DesignScript.Geometry import *

# create empty lists to store values
subDir = []

# give geometry a nickname for easy reference
geo = Autodesk.DesignScript.Geometry

# dir returns a list of module/class/object attributes
# for each item in topDir
for i in dir(geo) :
	# create a string equivalent to geo.i
	# eg 'Autodesk.DesignScript.Geometry.Application'
	dir_str = getattr(geo, i)
	# to find nested dir
	# append to subDir the dir of dir(geo)
	subDir.append(dir(dir_str))

# output dir(geo) and sub dir
OUT = dir(geo), subDir
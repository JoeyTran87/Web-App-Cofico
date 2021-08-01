# Load the Python Standard and DesignScript Libraries
import sys, os
import clr

pathRevitAPI = r"C:\Program Files\Autodesk\Revit 2020" #Revit API path
sys.path.append(pathRevitAPI) # append Path for Add reference
clr.AddReference('RevitAPI')

pathDynamoModule1 = r"C:\Program Files\Autodesk\Revit 2020\AddIns\DynamoForRevit"
if os.path.exists(pathDynamoModule1):
    sys.path.append(pathDynamoModule1)

pathDynamoModule2 = r"C:\Program Files\Autodesk\Revit 2020\AddIns\DynamoForRevit\Revit"
if os.path.exists(pathDynamoModule2):
    sys.path.append(pathDynamoModule2)

clr.AddReference('ProtoGeometry')
import Autodesk.DesignScript.Geometry
from Autodesk.DesignScript.Geometry import *
clr.AddReference('DSCoreNodes')
from DSCore import Math

# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

pointA = IN[0]#[0]
pointB = IN[1]#[0]
flipX = IN[2]
flipY = IN[3]
flipZ = IN[4]
stepMax = IN[5]
stepHeight = IN[6]
scale = IN[7]

iniBoundingBox = BoundingBox.ByCorners(pointA,pointB)
minBBpoint = iniBoundingBox.MinPoint
maxBBpoint = iniBoundingBox.MaxPoint

p1 = Point.ByCoordinates(0,0,0)
p2 = Point.ByCoordinates(stepMax*scale,stepMax*scale,stepHeight)
cub = Cuboid.ByCorners(p1,p2)#BoundingBox.ByCorners(p1,p2)#
arrayNumberX = Math.Round(Math.Abs(maxBBpoint.X-minBBpoint.X)/stepMax)
arrayNumberY = Math.Round(Math.Abs(maxBBpoint.Y-minBBpoint.Y)/stepMax)
arrayNumberZ = Math.Round(Math.Abs(maxBBpoint.Z-minBBpoint.Z)/stepHeight)
#cub = Geometry.Translate(cub,minBBpoint.X,minBBpoint.Y,minBBpoint.Z)
arrayCub = []
for xx in range(int(arrayNumberX)):
	for yy in range(int(arrayNumberY)):
		for zz in range(int(arrayNumberZ)):			
			p1 = Point.ByCoordinates(0,0,0)
			p3 = Point.ByCoordinates(minBBpoint.X + flipX*xx*stepMax ,minBBpoint.Y  + flipY*yy*stepMax,minBBpoint.Z + flipZ*zz*stepHeight)
			vec = Vector.ByTwoPoints(p1,p3)			
			p1a = Geometry.Translate(p1,vec)
			p2a = Geometry.Translate(p2,vec)

			cub = Geometry.Translate(cub,minBBpoint.X + flipX*xx*stepMax ,minBBpoint.Y  + flipY*yy*stepMax,minBBpoint.Z + flipZ*zz*stepHeight)
            arrayCub.append(cub)
			#newCub = BoundingBox.ByCorners(p1a,p2a).ToCuboid()
			#arrayCub.append(newCub)

# Assign your output to the OUT variable.
OUT = cub,arrayCub, len(arrayCub)
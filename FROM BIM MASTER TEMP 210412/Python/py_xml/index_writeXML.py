import xml.etree.ElementTree as ET
import openpyxl
import xmlLibs
from xmlLibs import *

pathName = r'C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\pythonXml\2101-005_ACCREDO ASIA - BRIEF.xlsx'

pathXMLfile = r'C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\pythonXml\2101-005_ACCREDO ASIA - BRIEF.xml'

sheetName = "OP04-FO01 (New)"

# project_info = projectDataFromExcel(ET,pathName,sheetName) # OUT = XML Tree data


# projectData = ET.tostring(project_info.xmlInfo).decode('utf-8',"ignore")

# with open(pathXMLfile, "w") as myXMLfile:
#     myXMLfile.write(projectData)
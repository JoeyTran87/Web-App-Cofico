import openpyxl, json
import index_libs
from index_libs import *

import re

pathName = r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\pythonExcel\2101-005_ACCREDO ASIA - BRIEF.xlsx"
sheetName = "OP04-FO01 (New)"

jsonPath = r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\pythonExcel\2101-005_ACCREDO ASIA - BRIEF.json"

cel_WrittenDate = 'G3'
cel_ProjectNumber = 'W3'
cel_Client = 'H5'
cel_ProjectName = 'H6'
cel_Location = 'H7'
cel_Location_Alt = 'B21' #issue: label & value combined - need to split
cel_Package = 'H8'
cel_CFA = 'D24'
cel_EstimatedStartDate = 'M31'
cel_EstimatedEndDate = 'L32'
cel_ScopeOfWork = 'A38'
cel_ContractType = 'A43'
cel_ContractCondition = 'A44'

sheetData = excelSheetData(pathName,sheetName)

project_info = {}

project_info['cel_WrittenDate'] = processExcelString(sheetData[cel_WrittenDate].value)
project_info['cel_ProjectNumber'] = processExcelString(sheetData[cel_ProjectNumber].value)
project_info['cel_Client'] = processExcelString(sheetData[cel_Client].value)
project_info['cel_ProjectName'] = processExcelString(sheetData[cel_ProjectName].value)
project_info['cel_Location'] = processExcelString(sheetData[cel_Location].value)
project_info['cel_Location_Alt'] = processExcelString(sheetData[cel_Location_Alt].value)
project_info['cel_Package'] = processExcelString(sheetData[cel_Package].value)
project_info['cel_CFA'] = processExcelString(sheetData[cel_CFA].value)
project_info['cel_EstimatedStartDate'] = processExcelString(sheetData[cel_EstimatedStartDate].value)
project_info['cel_EstimatedEndDate'] = processExcelString(sheetData[cel_EstimatedEndDate].value)
project_info['cel_ScopeOfWork'] = processExcelString(sheetData[cel_ScopeOfWork].value)
project_info['cel_ContractType'] = processExcelString(sheetData[cel_ContractType].value)
project_info['cel_ContractCondition'] = processExcelString(sheetData[cel_ContractCondition].value)

exDat = jsonString([project_info])
print (exDat)
# print (str(project_info))
# print(project_info.get('cel_WrittenDate'))

# print (["{0}:{1}".format(p,project_info.get(p)) for p in project_info])
writeJsonFile_fromString(jsonPath,exDat)

# stringData = project_info.get('cel_Package')


# print(str(stringData).split('\r\n'))
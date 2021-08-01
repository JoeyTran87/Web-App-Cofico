import xml.etree.ElementTree as ET
import openpyxl

# def excelSheetData(pathName,sheetName):
#     workBook = openpyxl.load_workbook(pathName)
#     sheetData = workBook[sheetName]
#     # workBook.close()
#     return sheetData
    
def createXMLItem1(ET,parent,itemName,itemAtt, itemAttVal,itemText):
    item = ET.SubElement(parent, itemName)
    item.set(itemAtt,itemAttVal)
    item.text = itemText

def createXMLItem2(ET,parent,itemName,itemText):
    item = ET.SubElement(parent, itemName)
    item.text = itemText

class projectDataFromExcel:
    def __init__(self,ET,pathName,sheetName):
        
        sheetData = excelSheetData(pathName,sheetName)
        
        cel_WrittenDate = 'G3'
        cel_ProjectNumber = 'W3'
        cel_Client = 'H5'
        cel_ProjectName = 'H6'
        cel_Location = 'H7'
        cel_Location_Alt = 'B21'
        cel_Package = 'H8'
        cel_CFA = 'D24'
        cel_EstimatedStartDate = 'M31'
        cel_EstimatedEndDate = 'L32'
        cel_ScopeOfWork = 'A38'
        cel_ContractType = 'A43'
        cel_ContractCondition = 'A44'
        
        project_info = {}
        project_info['cel_WrittenDate'] = str(sheetData[cel_WrittenDate].value)
        project_info['cel_ProjectNumber'] = sheetData[cel_ProjectNumber].value
        project_info['cel_Client'] = sheetData[cel_Client].value
        project_info['cel_ProjectName'] = sheetData[cel_ProjectName].value
        project_info['cel_Location'] = sheetData[cel_Location].value
        project_info['cel_Location_Alt'] = sheetData[cel_Location_Alt].value
        project_info['cel_Package'] = sheetData[cel_Package].value
        project_info['cel_CFA'] = sheetData[cel_CFA].value
        project_info['cel_EstimatedStartDate'] = sheetData[cel_EstimatedStartDate].value
        project_info['cel_EstimatedEndDate'] = sheetData[cel_EstimatedEndDate].value
        project_info['cel_ScopeOfWork'] = sheetData[cel_ScopeOfWork].value
        project_info['cel_ContractType'] = sheetData[cel_ContractType].value
        project_info['cel_ContractCondition'] = sheetData[cel_ContractCondition].value
        
        self.Info = project_info
        
        self.xmlInfo = getXmlInfo(project_info)
    
def excelSheetData(pathName,sheetName):
    workBook = openpyxl.load_workbook(pathName)
    sheetData = workBook[sheetName]
    # workBook.close()
    return sheetData

def getXmlInfo(project_info):
    data = ET.Element('ProjectInfo')
    for info in project_info:
        item = ET.SubElement(data, info)        
        item.text = project_info.get(info)
    return data

# def xmlString(data): # cho trường hợp bị lỗi JSON acsii encoder \u1111	
# 	res = ''
# 	fmr = '<{0} {1} = "{2}">{3}</{0}>'
# 	res2 = ''
# 	res3=[]
# 	try:
# 		for dat in data:
# 			try:
# 				dicStr = ""
# 				fm = "{0}{1}{2}{3}{4}{5}{6}"	
# 				#fm.format("{","123","}")	
# 				for d in dat:
# 					try:
# 						#res.append(type(dat.get(d)).__name__)#(dumps(d, indent = 2,sort_keys = True,ensure_ascii = True))
# 						tn = type(dat.get(d)).__name__
# 						if tn == "str":
# 							dicStr += fm.format("\"",d,"\"",":","\"",dat.get(d),"\"")+","
# 						if tn =="float":
# 							dicStr += fm.format("\"",d,"\"",":","",dat.get(d),"")+","
# 					except Exception, ex:
# 						res3.append(ex)
# 						pass
# 				res += fmr.format("{",dicStr[:-1],"}") +","	
# 			except:
# 				pass
# 		res2 = fmr.format("[",res[:-1],"")+"]"
# 	except:
# 		pass
# 	return res2
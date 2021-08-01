import openpyxl, json
import tempfile
from shutil import copyfile

import pandas as pd
import numpy as np
import re

def excelSheetData(pathName,sheetName):
    workBook = openpyxl.load_workbook(pathName)
    sheetData = workBook[sheetName]
    return sheetData

# for data in sheetData:
    # for cell in data:
    #     print(cell.value)

# class projectInfo:
#     def __init__(self):
#         self.infoDictionary = {}

# def writeFileFromTxtString(PATH, exDat): #from txt string
# 	with open(PATH,"w") as f:
# 		f.write(exDat)	
# 	return exDat

def writeJsonFile(jsonpath,data):
	with open(jsonpath,'w') as fs:
		json.dump(data,fs)

def writeJsonFile_fromString(jsonpath,data):
	with open(jsonpath,'w') as fs:
		fs.write(data.encode('utf-8').decode('utf-8'))#,"backslashreplace"))##.encode('utf-8').decode('utf-8'))



def jsonStringSingle(dat): # cho trường hợp bị lỗi JSON acsii encoder \u1111	
	res = ""
	fmr = "{0}{1}{2}"
	dicStr = ""
	fm = "{0}{1}{2}{3}{4}{5}{6}"
	try:
		for d in dat:
			try:
				tn = type(dat.get(d)).__name__
				if tn == "str":
					dicStr += fm.format("\"",d,"\"",":","\"",dat.get(d),"\"")+","
				if tn =="float":
					dicStr += fm.format("\"",d,"\"",":","",dat.get(d),"")+","
			except:
				pass
		res += fmr.format("{",dicStr[:-1],"}")
	except:
		pass
	return res

def jsonStringSingle2(dat): # cho trường hợp bị lỗi JSON acsii encoder \u1111	
	res = r"{}"
	return res.format(dat)

def jsonString(data): # cho trường hợp bị lỗi JSON acsii encoder \u1111	
	res = ""
	fmr = "{0}{1}{2}"
	res2 = ""
	res3=[]
	try:
		for dat in data:
			try:
				dicStr = ""
				fm = "{0}{1}{2}{3}{4}{5}{6}"	
				#fm.format("{","123","}")	
				for d in dat:
					try:
						#res.append(type(dat.get(d)).__name__)#(dumps(d, indent = 2,sort_keys = True,ensure_ascii = True))
						tn = type(dat.get(d)).__name__
						if tn == "str":
							dicStr += fm.format("\"",d,"\"",":","\"",dat.get(d),"\"")+","
						if tn =="float":
							dicStr += fm.format("\"",d,"\"",":","",dat.get(d),"")+","
					except:
						pass
				res += fmr.format("{",dicStr[:-1],"}") +","	
			except:
				pass
		res2 = fmr.format("[",res[:-1],"")+"]"
	except:
		pass
	return res2


#
#
def processExcelString(data):    
    combineString = ""
    try:
        splitString = fun1(str(data).replace('\n', ' ').replace('\r', ''),cond1).split(" ")
        for s in splitString:
            try:
                combineString += s# +" "
            except :
                pass
    except:
        pass
    return combineString#[:-1]
strIn = """Bê tông vách hố thang trục (5/H)
Bê tông vách hố thang trục (10/H)
Bê tông vách bể xử lý nước thải đến cote -1.900
Bê tông vách tường chắn đất, cột C74, C75, C76, C77, C78, C79 trục (6-9/H) đến cote +3.000
Bê tông cột C81, C82, C83, C84, C82a, C83a
Vách bể tự hoại trục (11-12/L-M)
Bê tông vách tường chắn đất, cột C74, C75, C76, C77, C78, C79 trục (6-9/H) từ cote +3.000 đến cote +4.700
Vách bể tự hoại trục (11-12/L-M)
Cột C20, C21, C28 bể XLNT
Vách thang máy 1F trục (5/H) đến cote +3.000
Cột C66, C68, C70, vách W15, W15a tầng 1
Vách thang máy 1F trục (10/H) đến cote +3.000
C47, C48, C49, C53, C54, C62, C63, C64, C67, C69, C71 trục (8-10/P2-G)
W18, W18a trục (9/F-G)
"""
cond1="""u	u
ú	u
ù	u
ủ	u
ũ	u
ụ	u
ư	u
ứ	u
ừ	u
ử	u
ữ	u
ự	u
e	e
é	e
è	e
ẻ	e
ẽ	e
ẹ	e
ê	e
ế	e
ề	e
ể	e
ễ	e
ệ	e
o	o
ó	o
ò	o
ỏ	o
õ	o
ọ	o
ơ	o
ớ	o
ờ	o
ở	o
ỡ	o
ợ	o
ô	o
ố	o
ồ	o
ổ	o
ỗ	o
ộ	o
a	a
á	a
à	a
ả	a
ã	a
ạ	a
ă	a
ắ	a
ằ	a
ẳ	a
ẵ	a
ặ	a
â	a
ấ	a
ầ	a
ẩ	a
ẫ	a
ậ	a
i	i
í	i
ì	i
ỉ	i
ĩ	i
ị	i
y	y
ý	y
ỳ	y
ỷ	y
ỹ	y
ỵ	y
đ	d"""

cond2="""bê tông	Concrete
vách	Wall
hố thang	Elevator Pit
bể xử lí nước thải	Water Treatment Tank
bể XLNT	Water Treatment Tank
XLNT	Water Treatment
bể tự hoại	Sewage tank
cột	Column
chắn đất	Param Wall
thang máy	Elevator
trục	Grid
đến cote	Level Elevation"""
def fun1(str,cond1):
	res = re.sub(" ","",str)
	for cd in cond1.split("\n"):
		res = re.sub(cd.split("\t")[0],cd.split("\t")[1],res).lower()
	return res#re.sub(" ","",str)
def fun2(cond2):
	res = []
	for cd2 in cond2.split("\n"):
		r=[]
		r.append(fun1(cd2.split("\t")[0]))
		r.append(fun1(cd2.split("\t")[1]))
		res.append(r)
	return res
def fun3(str,conds):
	res = ""
	for cd in conds:
		if cd[0] in str:
			res += "#"+cd[1]
	return res
def fun4(strIn,cond2): #hastag LIST
	res = []
	for str in strIn.split("\n"):
		res.append(fun3(fun1(str),fun2(cond2)))
	return res
def fun41(strIn,cond2): #hastag 1 LINE
	res = ""
	for str in strIn.split("\n"):
		res += fun3(fun1(str),fun2(cond2)) +"\n"
	return res	
def writeTxtFromTxtString(PATH, exDat): #from txt string
	with open(PATH,"w") as f:
		f.write(exDat.encode('utf8'))	
	return exDat
#write txt

# Assign your output to the OUT variable.

# print(fun1(strIn,cond1))
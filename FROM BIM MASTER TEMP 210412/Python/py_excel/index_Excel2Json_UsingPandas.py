import openpyxl, json

import pandas as pd
import numpy as np

import index_libs
from index_libs import *

pathName = r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\pythonExcel\2101-005_ACCREDO ASIA - BRIEF.xlsx"
sheetName = "OP04-FO01 (New)"

excelfile = pd.read_excel(pathName, sheetName, index_col=None, na_values=["NA"])

# for d in excelfile:
#     print (d)   
print (excelfile)   
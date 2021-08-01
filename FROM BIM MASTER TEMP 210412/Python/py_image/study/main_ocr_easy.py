#---------------------------------------------------------#
# set current work directory (CWD)
#---------------------------------------------------------#
import os,sys
os.chdir(os.getcwd())
import easyocr
# from PIL import ImageColor, Image

#---------------------------------------------------------#
# READ IMG
#---------------------------------------------------------#

reader = easyocr.Reader(['en','vi']) # Language codes (ISO 639) # https://www.loc.gov/standards/iso639-2/php/code_list.php

result = reader.readtext('text2.png')

print(result)
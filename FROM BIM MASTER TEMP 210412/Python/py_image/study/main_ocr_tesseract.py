import pytesseract      
from PIL import Image
import pyttsx3 
from googletrans import Translator 
#---------------------------------------------------------#
# set current work directory (CWD)
#---------------------------------------------------------#
import os,sys
os.chdir(os.getcwd())
#---------------------------------------------------------#
# READ TEXT FROM IMG
#---------------------------------------------------------#
img = Image.open('text1.png')     
# describes image format in the output
# print(img)                          
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd =r"C:\Users\USER\AppData\Local\Programs\Python\Python39\Lib\site-packages\pytesseract\pytesseract.py"
#'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'   
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)   
# write text in a text file and save it to source path   
with open('text_read_out.txt',mode ='w') as file: 
    file.write(result)
    print(result)
                   
p = Translator()                      
# translates the text into german language
k = p.translate(result,dest='german')      
print(k)
engine = pyttsx3.init()
  
# an audio will be played which speaks the test if pyttsx3 recognizes it
engine.say(k)                             
engine.runAndWait()
"""Xử lí toàn bộ Block, Leader, Dim : Color by Block"""


import pyautocad
from pyautocad import Autocad, APoint
import pyautocad, utility
from pyautocad import *
from utility import *

def main():
    cad_app = None
    cad_doc = None
    path = None

    #-----------------------# Kiểm tra đường dẫn
    while True:
        path = input('Đường dẫn file CAD: ')
        if os.path.isfile(path):
            break
    file_name = path.split("\\")[-1]
    #-----------------------# Mở Autocad lên nếu chưa mở
    while True:
        try:
            cad_app = comtypes.client.GetActiveObject("AutoCAD.Application")
        except:
            cad_app = comtypes.client.CreateObject("AutoCAD.Application")
        if cad_app:
            break
    # while not acadApp.GetAcadState().IsQuiescent :
    #     time.sleep(5)
    cad_app.Visible = True
    acad = Autocad()
    #-----------------------# Mở Tập tin CAD lên nếu chưa mở
    while True:
        try:
            docs = acad.Application.Documents # print(cad_doc.Name)
            count = docs.Count
            while count > 0:            
                #-----------------------# Nếu File đã đang mở
                count -= 1
                if docs.Item(count).Name == file_name:
                    cad_doc = docs.Item(count)
                    print(cad_doc.Name)
                    break           
                
            if cad_doc == None:
                cad_doc = cad_app.Documents.Open(path)
                print(cad_doc.Name)
                break
            else:
                break
        except:
            pass
    acad.prompt("Hello, Autocad from Python")

    blocks = cad_doc.Blocks

    model_space = cad_doc.ModelSpace




    doc=acad.ActiveDocument
    ms=doc.ModelSpace



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()

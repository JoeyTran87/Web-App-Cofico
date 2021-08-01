import openpyxl,time
import pandas as pd
# import string
# alphabet = string.ascii_lowercase

#-------------------------------------------------------------------------------------------------------#
def write_column(path,sheet_name,column_name,start,data):    
    """GHI DỮ LIỆU VÀO CỘT EXCEL"""
    time_start = time.localtime(time.time())
    print (f"\tTime write start: {time.strftime('%H:%M:%S',time_start)}")    
    workbook = openpyxl.load_workbook(path)
    worksheet= workbook.get_sheet_by_name(sheet_name)
    i = start
    for d in data:
        celname = f"{str(column_name).upper()}{int(i)}"
        worksheet[celname] = d
        i += 1
    time_end = time.localtime(time.time())
    print (f"\tTime write end: {time.strftime('%H:%M:%S',time_end)}")

#-------------------------------------------------------------------------------------------------------#
def write_new_excel(path,sheet_write_name,df,startR = 0,startC =0):
    """Lưu file excel mới với tên Sheet mong muốn"""
    time_start = time.localtime(time.time())
    print (f"\tTime start: {time.strftime('%H:%M:%S',time_start)}")
    with pd.ExcelWriter(path,mode='w') as writter:
        df.to_excel(writter,sheet_write_name,na_rep='NA',startrow=startR,startcol=startC,engine='openpyxl') 
    time_end = time.localtime(time.time())
    print (f"\tTime end: {time.strftime('%H:%M:%S',time_end)}")

#-------------------------------------------------------------------------------------------------------#

def show_excel_sheet(excel_path) -> list:
    """Show danh sách tên các sheet trong file Excel"""
    xl = pd.ExcelFile(excel_path)
    sheets = xl.sheet_names
    for i,shn in enumerate(sheets):
        print(f"\t{shn}")  # see all sheet names
    return sheets
# main_pd()
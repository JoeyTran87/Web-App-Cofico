# -*- coding: utf-8 -*-
"""Sub program : Tra cứu Mã Vật tư thiết bị"""
import os, time,shutil
import pandas as pd
import numpy as np
import unidecode, re
from program_var import *
from handle_search import *
from handle_cmd import *
from handle_excel_files import *

os.chdir(os.getcwd())

#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def main_lookup_plan(path_root):
    global BREAKER, START_END_LINE
    promp_list = [  "Chọn [đường dẫn file] Excel Kế hoạch VTTB",
                    "Chọn [tên Sheet] Excel",
                    "[Xem xét] dữ liệu Kế hoạch sau",
                    "Chọn [SỐ DÒNG] làm TIÊU ĐỀ CỘT",
                    "Chọn [SỐ CỘT] dữ liệu (giữ lại)",
                    "[Xem xét] Bảng dữ liệu Kế hoạch đã làm sạch",
                    "Chọn [SỐ CỘT] Dữ kiện TÌM KIẾM",
                    "Chọn [SỐ CỘT] mà Kết quả sẽ TRẢ VỀ",
                    "[Xem xét] dữ liệu [Tra cứu] VTTB",
                    "Chọn [SỐ CỘT] Tra cứu",
                    "Chọn [SỐ CỘT] Kết quả",
                    "[Xem xét] KẾT QUẢ TRA CỨU",
                    "Xuất dữ liệu Excel",
                    "",
                    ""]
    # pd.set_option('display.max_rows', None)
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 30)

    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    show_heading_1('TRÌNH XỬ LÍ DỮ LIỆU KẾ HOẠCH VTTB')

    path_plan = input(f"\t(1). Đường dẫn file Excel Kế hoạch VTTB: <<<Nhập giá trị>>> ")
    print(BREAKER)
    excel_sheet_name = input(f"\t(2). Chọn tên Sheet Excel: <<<Nhập giá trị>>> ")
    print(BREAKER)
    # FIRST REVIEW --> dữ liệu ban đầu RAW
    df_plan = pd.read_excel(path_plan,excel_sheet_name,dtype='string')    
    df_plan_copy = df_plan.copy() # bản sao Dữ liệu ban đầu

    # column_alphabet = [f"{i}" for i in alphabet[:len(df_plan_copy.columns)]] # cột A B C
    # df_plan_copy = pd.concat([df_plan_copy, pd.DataFrame(np.array([column_alphabet]),columns=df_plan_copy.columns)], ignore_index=True)

    column_numbers = [f"Cột {i}" for i in range(len(df_plan_copy.columns))] # cột số
    df_plan_copy = pd.concat([df_plan_copy, pd.DataFrame(np.array([column_numbers]),columns=df_plan_copy.columns)], ignore_index=True)

    print("\t(3). Vui lòng xem xét dữ liệu Kế hoạch sau: ")
    print(BREAKER)
    print(pd.concat([df_plan_copy.head(10),df_plan_copy.tail(5)],ignore_index=False))
    print(BREAKER)
    print(f"\tDữ liệu cần bạn thiết lập để làm dữ liệu sạch hơn")
    print(BREAKER)

    row_header = int(input(f"\t(4.1) Chọn SỐ DÒNG làm TIÊU ĐỀ CỘT (xem SỐ DÒNG ở cột Biên Trái)\n\t(Vd: 4): <<<Nhập giá trị>>> ")) # 5
    # print(df_plan_copy.loc[row_header])
    # for c in df_plan_copy.loc[row_header]:
    #     print(c)
    # print(df_plan_copy[df_plan_copy.columns[1]].iloc[-2])
    print(BREAKER)
    columns = [int(i) for i in input(f"\t(4.2) Chọn danh sách SỐ CỘT dữ liệu được giữ lại(xem SỐ CỘT cuối bảng (3))\n\tSố nguyên và phẩy\n\t(Vd: 1,2,3,4,5,6): <<<Nhập giá trị>>> ").replace(" ","").split(',')] # 8
    print(BREAKER)
    column_drop = input(f"\t(4.3) Chọn SỐ CỘT sẽ giúp LOẠI BỎ GIÁ TRỊ TRỐNG từ việc xem xét các trị cột này(xem SỐ DÒNG cuối bảng (3)\n\t(Vd: 2): <<<Nhập giá trị>>> ")  
    if len(column_drop)== 0:
        column_drop = 0
    else:
        column_drop = int(column_drop)
    spinWaiting(BREAKER)
    # TẠO DỮ LIỆU LÀM SạCH
    try:
        df_plan = pd.read_excel(path_plan,excel_sheet_name
                                ,header = row_header+1,dtype='string'
                                ,usecols=columns)
        df_plan.dropna(subset=[df_plan.columns[column_drop]],inplace=True)
    except:
        pass    
    
    print("\tHoàn tất xử lí dữ liệu")
    print(BREAKER)
    print("\t(5). Vui lòng xem xét Bảng dữ liệu Kế hoạch đã làm sạch sau: ")
    print(BREAKER)
    # copy show cột
    df_plan_copy = df_plan.copy()
    column_numbers = [f"Cột {i}" for i in range(len(df_plan_copy.columns))]
    df_plan_copy = pd.concat([df_plan_copy, pd.DataFrame(np.array([column_numbers]),columns=df_plan_copy.columns)], ignore_index=True)
    #show
    print(df_plan_copy)
    print()
    print(BREAKER)

    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#

    col_lookup_value_index = input(f"\t(5.1) Chọn SỐ CỘT Dữ kiện TÌM KIẾM (xem SỐ CỘT cuối bảng (5)\n\t(?)Là Giá Trị dùng để tìm kiếm\n\t(Vd: 1): <<<Nhập giá trị>>> ")
    print(BREAKER)
    col_lookup_target = input(f"\t(5.2) Chọn SỐ CỘT mà Kết quả sẽ TRẢ VỀ(xem SỐ CỘT cuối bảng (5)\n\t(?)Là Giá Trị mong muốn trả về sau khi tra cứu\n\t Nếu muốn tạo mới cột này nhập N\n\t(Vd: 0 hoặc N): <<<Nhập giá trị>>> ")
    
    
    if len(col_lookup_target) == 0 or col_lookup_target.lower() == 'n':
        col_lookup_target = 'N'   
    else:
        col_lookup_target = int(col_lookup_target)
    if len(col_lookup_value_index) == 0:
        col_lookup_value_index = 0
    else:
        col_lookup_value_index = int(col_lookup_value_index)
    
    
    spinWaiting(BREAKER)
    # 3.EXTRACT LOOK UP VALUE
    df_plan_lookup = df_plan.copy()
    col_lookup_value = df_plan_lookup.columns[col_lookup_value_index]
    extract_lookup_value = 'Lookup Value'
    df_plan_lookup[extract_lookup_value] = [unidecode.unidecode(re.sub('\s+',' ',str(lkv).strip()).upper()) for lkv in df_plan_lookup[col_lookup_value]]
    

    spinWaiting(BREAKER)

    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    # 4.LOAD LOOKUP ARRAY DATA
    lookup_array_path = f"{path_root}\\{SUB_DATA_VTTB}\\{DATA_SEARCH_NAME}.json"
    lookup_array = pd.read_json(lookup_array_path,orient='records',dtype='string')
    print(BREAKER)
    spin_three_dots('\tĐang tải Dữ liệu tra cứu VTTB ')
    print("\tDữ liệu tra cứu VTTB đã được tải")
    print("\t(6). Vui lòng xem xét dữ liệu tra cứu VTTB: ")
    print(BREAKER)
    
    lookup_array_copy = lookup_array.copy()
    column_numbers = [f"Cột {i}" for i in range(len(lookup_array_copy.columns))]
    lookup_array_copy = pd.concat([lookup_array_copy, pd.DataFrame(np.array([column_numbers]),columns=lookup_array_copy.columns)], ignore_index=True)
    
    print (lookup_array_copy)
    print(BREAKER)

    col_lookup = input(f"\t(7) Số hiệu Cột Tra cứu(xem dòng cuối) bảng (6)\n\tLà vùng Tra cứu giá trị tìm kiếm của bảng (5)\n\t(Vd: 6): <<<Nhập giá trị>>> ")
    print(BREAKER)
    #validate
    if len(col_lookup) == 0:
        col_lookup = 0
    else:
        col_lookup = int(col_lookup)
        
    col_lookup_return = input(f"\t(8) SỐ hiệu Cột Kết quả(xem dòng cuối) bảng (6)\n\tLà cột Trả về Giá trị kết quả\n\t(Vd: 2): <<<Nhập giá trị>>> ")
    #validate
    if len(col_lookup_return) == 0:
        col_lookup_return = 1
    else:
        col_lookup_return = int(col_lookup_return)

    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    spin_three_dots('\tĐang tra cứu dữ liệu')
    # 5.LOOK UP
    time_start = time.localtime(time.time())
    print (f"\tTime start: {time.strftime('%H:%M:%S',time_start)}")
    list_result = []
    spin_three_dots('\tĐang tra cứu dữ liệu')  

    for i in df_plan_lookup[extract_lookup_value].index:
        try:            
            lkv = df_plan_lookup[extract_lookup_value][i]
            df_result = searcher(str(lkv),lookup_array,lookup_array.columns[col_lookup])
            # print (df_result)
            # print (df_result[lookup_array.columns[col_lookup_return]])
            result = None
            ri = 200000
            for ii in df_result.index:
                if ii < ri:
                    ri = ii
            try:
                result = df_result[lookup_array.columns[col_lookup_return]][ri]
            except KeyError:
                result = "na"
                pass

            list_result .append(result)
        except:
            list_result .append("na")
            pass       

    col_result = None
    if col_lookup_target == 'N':
        col_result = "Mã VTTB"
        pass
    else:
        col_result = df_plan_lookup.columns[col_lookup_target]

    df_plan_lookup[col_result] = pd.Series(list_result,dtype='string')

    time_end = time.localtime(time.time())
    print (f"\tTime end: {time.strftime('%H:%M:%S',time_end)}")
    # print(f"Duration: {float(time_end)-float(time_start)} seconds")
    spin_three_dots('\tTra cứu dữ liệu hoàn tất')
    print("\t(9). Vui lòng xem xét KẾT QUẢ TRA CỨU: ")
    print (df_plan_lookup)
    print(BREAKER)
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------#
    ask_export = input (f"""\t(10). Bạn muốn xuất thành dữ liệu Excel (y/n): <<<Nhập giá trị>>> """).lower()
    print(BREAKER)

    if ask_export == "y":   
        path_plan_write = ''
        time_write = time.strftime("%y%m%d%H%M%S",time.localtime(time.time()))
        if path_plan.split('.')[-1] == "XLSX":
            new_name = f"{path_plan[:-len(path_plan.split('.')[-1])-1]}-lookup{time_write}.xlsx"
            if not os.path.exists(new_name):
                shutil.copy2(path_plan,new_name)
            path_plan_write = new_name      
        
        excel_sheet_write = f"Lookup{time_write}"
        print(BREAKER)
        print(f"\t Thông tin tra cứu sẽ được ghi tại: {path_plan_write}\n\tSheet tên: {excel_sheet_write} ")
        print(BREAKER)
        df_plan_lookup = df_plan_lookup.drop(columns=[extract_lookup_value])
        write_new_excel(path_plan_write,excel_sheet_write,df_plan_lookup)
        print(BREAKER)
        print("\tGhi Excel hoàn tất")

    
    # print(breaker)
    # print('\t Ctrl + C để thoát cửa sổ Command line')
    print(BREAKER)
    
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    path_root = os.getcwd()
    try:
        while True:
            main_lookup_plan(path_root)
    except KeyboardInterrupt:
        quit()

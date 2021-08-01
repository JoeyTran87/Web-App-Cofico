# -*- coding: utf-8 -*-
"""Sub program : Quản lí cơ sở dữ liệu Vật tư thiết bị"""
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
import os,shutil,re
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from program_var import BREAKER,START_END_LINE,USER_INPUT_PREFIX
from handle_search import *
from handle_cmd import *
from handle_excel_files import *

#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
# GLOBAL
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
class menu_program():
    def __init__(self,path,dir_root = '.') -> any:
        self.menu_name_file_ext = str(path).split('.')[-1]
        self.menu_file_name  = str(path).split('\\')[-1][:-len(self.menu_name_file_ext)-1]
        #----------------------------------------------# tải Tên chương trình  + Mô tã + Menu từ file thiết lập menu 
        self.menu_name,  self.menu_description, menu = read_configure_file(path)
        #----------------------------------------------# clean data menu
        menu.dropna(subset = [menu.columns[2]],inplace = True)
        menu = menu.fillna('NA')
        self.menu_col_count = len(menu.columns)
        #----------------------------------------------# insert new column + reorder columns
        # col = menu['Group_Number']+menu['Number']
        # menu.drop(columns = ['Group_Number','Number'],inplace = True)
        # menu = pd.DataFrame(col,columns = ['Merge_Number']).join(menu)        
        menu['Merge_Number'] = menu['Group_Number']+menu['Number']
        #----------------------------------------------# load Path Source
        # col_path = dir_root+'\\'+menu['Source_Sub_Dir']+'\\'+menu['Source_Name']
        # menu.drop(columns = ['Source_Sub_Dir','Source_Name'],inplace = True)
        # menu = pd.DataFrame(col_path,columns = ['Path_Source']).join(menu)
        menu['Path_Source']= dir_root+'\\'+menu['Source_Sub_Dir']+'\\'+menu['Source_Name']
        #----------------------------------------------# final Menu data
        self.menu = menu
        self.menu_list = [f"{self.menu.iloc[m][2]}" for m in self.menu.index]
        self.menu_numbers = [f"{self.menu.iloc[m][self.menu_col_count]}" for m in self.menu.index]
        self.menu_path_source_list = [f"{self.menu.iloc[m][self.menu_col_count+1]}" for m in self.menu.index]
        #----------------------------------------------# load TIPS
        self.tips_KS = HOTKEYS_GENERAL

        #----------------------------------------------# TEST QUICK - XÓA KHI TEST XONG
        # print(self.menu_path_source_list)

    #-------------------------------------------------------------# SHOW
    def show_title(self) -> str:
        show_heading_1(self.menu_name)
    def show_title_3(self) -> str:
        show_heading_3(self.menu_name)
    def show_description(self,button_text = 'Mô tả/ Description:') -> str:
        print(button_1(button_text))
        print_text_box_L(self.menu_description)
    def show_tips(self,button_text = 'Mẹo/Tips:') -> str:
        print(button_1(button_text))
        print_text_box_L(self.tips_KS)
    #-------------------------------------------------------------# GET
    def get_path(self,index):
        return self.menu.iloc[index][self.menu_col_count+1]
    #-------------------------------------------------------------# ASK
    def ask_menu(self,button_text = 'Menu Steps:',promp = 'Vui lòng nhập số hiệu') -> str:
        print(button_1(button_text))
        ask =  ask_input_2(self.menu_list,input_prefix = f"{promp}\n{USER_INPUT_PREFIX}")
        print(BREAKER)
        return ask
    def ask_step(self,index,promp = '',pre_promp = 'Vui lòng'):
        step = [index,self.menu.iloc[index][2]]
        return input(f"[Bước {step[0]}] {pre_promp} {step[1]}\n{promp}\n{USER_INPUT_PREFIX}")
    #-------------------------------------------------------------# ASK
    def warning(self,index,promp = 'Vui lòng thử lại'):
        note = self.menu.iloc[index][4]
        # print(f"[!] {note} [!] {promp}")
        print_text_box_L(f"{note}\n{promp}",hoz = '_ ', ver = '!')


        
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------# MENU LIST : THỨ TỰ CẦN ĐƯỢC GIỮ CỐ ĐỊNH KO ĐỔI
tip_subprogram = f"\t"
menu_data_main = [
    'Cập nhật dữ liệu từ tập tin [Excel]',
    'Sửa [Tên cột] dữ liệu',
    'Làm sạch dữ liệu',
    'Sắp xếp Dữ liệu [Tăng dần] / [Giảm dần]',
    'Xây dựng dữ liệu tra cứu',
    'Hợp nhất dữ liệu',
    'Báo cáo [Phân tích] dữ liệu',
    'Danh sách [Top] Vật tư thiết bị',
    'Biểu đồ [Top] Vật tư thiết bị',
]
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------# MENU NUMBER : LÀ SỐ HIỆU BỘ TRÌNH CON, ĐỂ GIÚP DEBUG , LOG LỖI
menu_data_main_number = '80'
menu_data_analyse = [
    '[Top] Vật tư thiết bị',
    'Biểu đồ'
]
menu_sub_update_by_excel = [   
                "Chọn [đường dẫn file] Excel dữ liệu",
                "Chọn [tên Sheet] Excel",
                "[Xem xét] dữ liệu đã tải",
                "Chọn [SỐ DÒNG] làm TIÊU ĐỀ CỘT",
                "Chọn [SỐ + THỨ TỰ CỘT] dữ liệu [giữ lại]",
                "Chọn [SỐ CỘT] sẽ giúp [LOẠI BỎ GIÁ TRỊ TRỐNG]",
                "Thiết lập [Tên cột dữ liệu] mới",
                "[Xem xét] Bảng dữ liệu đã làm sạch",
                "Xuất dữ liệu cơ sở",
                ]
sub_title = """\tCác bước bạn sẽ thực hiện như sau đây:"""
tip_df = """\t(Mẹo) Bạn nên xem xét kỹ \n\t[Chỉ số Dòng] bên cột biên bên trái, và \n\t[Chỉ số Cột] ở Dòng dữ liệu cuối cùng)"""
promp_try = '[!] Chưa phù hợp, vui lòng thử lại'
promp_return = '[!] Chưa phù hợp, Tiến trình sắp [thoát] về [Main Menu]'
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
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def main_data(path_root,sub_dir,dat_name) -> any:
    """Đây là chương trình Phụ của Chương trình E-USD\n- Chuyên xử lí [ Dữ liệu Cơ sở] cho Toàn bộ chương trình"""
    path_data = ''#f"{path_root}\\{sub_dir}\\{dat_name}.json"
    # if not os.path.exists(path_data):
    #     warning(f"Đường dẫn tập tin dữ liệu [Không tồn tại]\n\t{path_data}")
    #     return
    path_menu_conf = f"{path_root}\\{SUB_CONFIGURE}\\menu_data_main.txt"
    menu = menu_program(path_menu_conf)
    menu.show_title()
    menu.show_description()
    menu.show_tips()
    ask_menu = menu.ask_menu()
    while ask_menu != 'q_' and ask_menu != 'z_' and ask_menu != 'qq' and ask_menu != 'zz': 
        flag_loop = True
        while flag_loop:
            #-----------------------------------------------------# User chọn Data đe bien tap
            path_data_conf =  f"{path_root}\\{SUB_CONFIGURE}\\menu_data_types.txt"
            menu_data = menu_program(path_data_conf)
            #-----------------------------------------------------# bien tap du lieu bang file excel
            if ask_menu == "0":
                while not os.path.exists(path_data):
                    path_data = menu_data.get_path(int(menu_data.ask_menu(button_text='Bạn chọn dữ liệu nào sau đây:')))                    
                    data_builder(path_root,sub_dir,dat_name,menu_sub_update_by_excel,path_data=path_data)
                    break
            elif ask_menu == "1":
                while not os.path.exists(path_data):
                    path_data = menu_data.get_path(int(menu_data.ask_menu(button_text='Bạn chọn dữ liệu nào sau đây:')))
                    change_df_column_names(path_data)
                    break
                flag_loop = False
            elif ask_menu == "2":
                pass
            ask_menu = menu.ask_menu()
    if ask_menu == 'q_':
        return
    elif ask_menu == 'z_':
        spin_three_dots('Bạn đang khởi động lại tiến trình')
        main_data(path_root,sub_dir,dat_name,menu)
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
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def data_archive(path_data):
    """### Description
    - Sao lưu tập tin dữ liệu đầu vào
    ### Input:
    - path_data (str) --> đường dẫn tập tin dữ liệu đầu vào"""
    """SAO LƯU DỮ LIỆU  (JSON FILE)"""        
    spin_three_dots(f"\tĐang lưu trữ dữ liệu hiện hành ")    
    if os.path.exists(path_data):
        # logging.debug (f"ARCHIVE FROM {PATH_DU_LIEU}")
        time_mod = time.strftime("%y%m%d%H%M%S",time.localtime(float(os.stat(path_data).st_mtime)))    
        path_data_archived = f"{path_data[:-len(path_data.split('.')[1])-1]}-{time_mod}.json"
        # logging.debug (f"ARCHIVE TO {PATH_ARCHIVE_DATA}")    
        if os.path.exists(path_data_archived):
            time_mod = time.strftime("%y%m%d%H%M%S",time.localtime(time.time()))
            path_data_archived = f"{path_data[:-len(path_data.split('.')[1])-1]}-{time_mod}.json"
        shutil.copy2(path_data,path_data_archived)
        
        spin_three_dots(f"\tĐang lưu trữ dữ liệu tra cứu hiện hành, phục vụ cập nhật dữ liệu mới ")
        # logging.info('ARCHIVE SUCCESSFUL')
        print(f"\tDữ liệu đã được Sao lưu: {path_data_archived}")
        spinWaiting(BREAKER)   
    else:
        # logging.warning('Cannot archive current search data')
        print(f"\tKhông có dữ liệu để xử lí")
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def data_lookup_builder(data,path,column_name) -> pd.DataFrame: # DU LIEU TRA CUU LA BẢN SAO CUA DU LIEU VTTB - CÓ THEM CỘT GIÁ TRỊ GHÉP DE TRA CUU VÀ CỘT BOOLLEAN KHỚP 
    """### Description
    - Tạo dữ liệu tra cứu từ dữ liệu đầu vào
    ### Input:
    - data (DataFrame) --> dữ liệu đầu vào
    - path (str) --> đường dẫn lưu dữ liệu tra cứu (đầu ra)
    - column_name (str) --> Tên cột chứa Nội dung tra cứu"""
    spin_three_dots(f"\tTiến trình đang thực hiện ")
    # HỎI XÁC NHẬN UPDATE DỮ LIỆU TRA CỨU ?
    # ask_update_data = input(promp_update_data_search).lower()
    # if ask_update_data == "y":        
    spin_three_dots(f"\tĐang cập nhật dữ liệu [Tra cứu] ")
    data_search = data.copy()
    data_search = data_search.replace(np.nan, NA_REPLACE, regex=True)
    data_search [column_name] = concat_df_series(data)
    data_search.to_json(path,orient='records')
    # VALIDATE TẬP TIN DỮ LIỆU MỚI TẠO:
    if os.path.exists(path) and float(os.stat(path).st_size)/1000 > 0:
        # logging.info(f"Update Search Data SUCCESSFULL\t{PATH_DU_LIEU_VTTB_TRA_CUU_JSON}")
        print(f"\tHoàn tất cập nhật Dữ liệu tra cứu: {path}")
        spinWaiting(BREAKER)
    return data_search
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
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def data_builder(path_root,sub_dir,dat_name,menu,path_data=None) -> pd.DataFrame:
    """### Description
    - Phương thức Xử lí dữ liệu
    Sử dụng Đại trà, không cụ thể cho loại dữ liệu nào
    ### Input:
    - path_root (str) --> dirpath
    - sub_dir (str) --> folder name
    - data_name (str) --> file path
    - header (str)
    - menu (list) : ['','','']"""
    path_data_last = ''
    if path_data and os.path.exists(path_data):
        path_data_last = path_data
    else:
        path_data_last = f"{path_root}\\{sub_dir}\\{dat_name}.json"
    # ----------------------------------------------------------# Setup PANDAS
    # pd.set_option('display.max_rows', None)                       
    # pd.set_option('display.max_columns', 10)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 30)

    # ----------------------------------------------------------# show menu
    menu_path = f"{path_root}\\{SUB_CONFIGURE}\\menu_data_builder.txt"
    menu_ = menu_program(menu_path)
    menu_.show_title_3()
    menu_.show_description()
    # menu_.show_tips()
    ask_menu = menu_.ask_menu(promp = 'Bạn sẵn sàng? (y/n)')    
    # ask_menu = show_menu_1(header,'Các bước bạn sẽ thực hiện',menu,f"{USER_INPUT_PREFIX} Bạn sẵn sàng? (y/n)")

    if ask_menu.lower() == 'y':
        # ----------------------------------------------------------# ask : Chọn [đường dẫn file] Excel dữ liệu
        path_data=menu_.ask_step(0)
        while not os.path.exists(path_data):
            menu_.warning(0)
            path_data = menu_.ask_step(0)
        # ----------------------------------------------------------# show tên sheet excel
        print(button_1("Danh sách các [Sheet]:"))
        sheets = show_excel_sheet(path_data)
        # ----------------------------------------------------------# ask : Chọn [tên Sheet] Excel
        flag_sheet = False 
        while flag_sheet == False:
            excel_sheet_name = menu_.ask_step(1)
            try:
                # excel_sheet_name = menu_.ask_step(1)
                # if excel_sheet_name.lower() == 'q_':
                #     return
                # elif excel_sheet_name.lower() == 'r_':
                #     flag_sheet = False   
                # else:
                flag_sheet = excel_sheet_name in sheets
            except:
                menu_.warning(1)
                flag_sheet = False
                
        ask_max_cols = 10
        tips= ''
        try:
            action = 'Chọn [số lượng] cột [tối đa]'
            ask_max_cols = int(input (f'\t{action}{USER_INPUT_PREFIX}'))
        except:
            warning_1(action,f"{promp_try}\n\tTrình tạo Dữ liệu vẫn tiếp tục bước tiếp theo\n\tXử dụng giá trị mặc định là {ask_max_cols}")
            pass
        pd.set_option('display.max_columns', ask_max_cols)
        if ask_max_cols > 10:
             pd.set_option('display.max_colwidth', 10)
        
        try:
            df = pd.read_excel(path_data,excel_sheet_name)#,dtype='string')
            df = df[df.columns[0:ask_max_cols]]
            df_copy = insert_column_index_row(df)
        except:
            print(f"\t[!]Có lỗi gì đó xảy ra, có thể bạn đã thực hiện thao tác {promp_try}\n\tTrình xử lí sẽ thoát về Main Menu")
            return

        print(f"\t[{2}] {menu[2]}: {USER_INPUT_PREFIX} ")
        print(BREAKER)
        print(df_copy)
        print(BREAKER)

        row_header = int(input((f"\t[{3}] {menu[3]}: {USER_INPUT_PREFIX} ")))
        print(BREAKER)
        
        flag_columns = False
        columns = []
        tips = '\n\t\tChọn 1 cột--Nhập--1 số nguyên\n\t\tChọn nhiều cột--Dùng--Dấu Phẩy [,]\n\t\tHủy tiến trình--Nhập--[Q_]'
        while flag_columns != True:
            columns = ask_input_1(4,menu[4],tips,input_prefix=USER_INPUT_PREFIX)            
            if columns.lower() == 'q_':
                return 
            try:
                columns = [int(i) for i in columns.replace(" ","").split(',')]
                flag_columns = True
            except:
                warning_1(menu[4],f"{promp_try}\n\t[Tips] Có thể bạn đã nhập [không phải] là số Nguyên, hay Danh sách số nguyên")
                flag_columns = False
                pass


        print(BREAKER)
        
        flag_column_drop = False
        column_drop = columns[0] # mặc định là cột đầu tiên
        tips = '\n\t\tChọn 1 cột--Nhập--1 số nguyên\n\t\tChọn tất cả cột--Nhập--A\n\t\tChọn nhiều cột--Dùng--Dấu Phẩy [,]\n\t\tHủy tiến trình--Nhập--[Q_]'            
        while flag_column_drop != True:            
            column_drop = ask_input_1(5,menu[5],tips, input_prefix=USER_INPUT_PREFIX)
            if column_drop.lower() == 'a':
                column_drop = columns
                flag_column_drop = True
                break
            elif column_drop.lower() == 'q_':
                return            
            else:
                try:
                    column_drop = [int(i) for i in column_drop.replace(" ","").split(',')]                
                    flag_column_drop = set(column_drop).issubset(columns)
                except:
                    warning_1(menu[5],f"{promp_try}\n\t[Tips] Có thể bạn đã nhập [không phải] là số Nguyên, hay Danh sách số nguyên")
                    flag_column_drop = False
                    break        
        
        spinWaiting(BREAKER)
        #-------------------------------------------------------------------# Xử lí DF = Lọc cột giữ lai + Bỏ NA
        df_copy = None
        try: 
            df_copy = pd.read_excel(path_data,excel_sheet_name
                                    ,header = row_header+1,dtype='string'
                                    ,usecols=columns)
            
            if type(column_drop) == int:
                df_copy.dropna(subset=[df.columns[column_drop]],inplace=True)
            elif type(column_drop) == list:
                # transfer to New DF column indexs  
                new_column_drop = []
                for  i,v in enumerate(columns):
                    for  j in column_drop:
                        if j == v:
                            new_column_drop.append(i) 
                df_copy.dropna(subset=[df_copy.columns[c] for c in new_column_drop],inplace=True)
        except:
            warning_1(menu[5],f"{promp_try} lần xử lí kế tiếp\n\tTrình tạo Dữ liệu vẫn tiếp tục bước tiếp theo")
            pass                
        
        print("\tHoàn tất xử lí dữ liệu, bạn sắp [Xem nhanh] dữ liệu của bạn")
        print(BREAKER)
        print(df_copy.head(3))
        print(BREAKER)
        
        #-------------------------------------------------------------------# Thiết lập Tiêu đề cột
        column_names = change_new_df_column_names(path_data_last,df_copy)
        print(BREAKER)
        print((f"\t[{7}] {menu[7]}: {USER_INPUT_PREFIX} "))
        print(BREAKER)
        #-------------------------------------------------------------------# Copy show cột
        df_copy.columns = column_names
        df_copy_show =  insert_column_index_row(df_copy)
        #-------------------------------------------------------------------# Show Du lieu
        print(df_copy_show)
        print(BREAKER)


        #-------------------------------------------------------------------# Ghi  Du lieu ra file
        df_copy = data_write_file(df_copy,path_data_last,title=menu[8])    
        return df_copy
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def data_write_file(df,path_data,title = None) -> pd.DataFrame:
    """### Description
    - [IO]
    - Phương thức Ghi dữ liệu ra Tập tin
    Sử dụng Đại trà, không cụ thể cho loại dữ liệu nào
    ### Input:
    - df (DataFrame) : Dữ liệu
    - path_data (str) : đường dẫn tập tin"""
    ask_export_data=''
    if title:
        ask_export_data = input((f"\t[{8}] Bạn sắp {title} (y/n)\n\t{USER_INPUT_PREFIX} "))
    else: 
        ask_export_data = 'y'
    
    if ask_export_data.lower() == 'y':
        try:            
            ask_append = input(f"\tBạn chọn:\n\t[1] [Nối tiếp] vào dữ liệu cũ \n\t[2]Ghi đè /thay thế dữ liệu cũ\n{USER_INPUT_PREFIX} ").lower()
            print(BREAKER)
            while ask_append == "1" or ask_append == "2":
                if ask_append == "2":    
                    #-------------------------------------------------------------------# Ghi ra JSON File    
                    df.to_json(path_data,orient='records')
                    print(f'\tThành công tạo dữ liệu mới: {USER_INPUT_PREFIX} {path_data}')
                    break
                elif ask_append == "1":
                    df = pd.concat([df,pd.read_json(path_data,orient='records')], ignore_index=True)
                    df.to_json(path_data,orient='records')  
                    print('\tThành công Nối tiếp Dữ liệu')
                    print(f'\tThành công tạo dữ liệu mới: {USER_INPUT_PREFIX} {path_data}')
                    break
                else:
                    warning('Tiến trình chưa hoàn tất, vui lòng thử lại')
                    ask_append = input(f"\tBạn chọn:\n\t[1] [Nối tiếp] vào dữ liệu cũ \n\t[2]Ghi đè /thay thế dữ liệu cũ\n{USER_INPUT_PREFIX} ").lower()                         
        except:
            warning(f"Có gì đó không ổn\n\tDữ liệu đã [không được ghi]\n\tTrình xử lí đang thoát [về Main Menu]")
            pass
    return df
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def data_combine(data_1,data_2,path_combine):
    """Hợp nhất 2 dữ liệu"""
    data_1_copy = insert_column_index_row(data_1)
    data_2_copy = insert_column_index_row(data_2)
    # print(data_1_copy)                  # xem xét trươc khi thiêt lap
    # print(data_2_copy)                  # xem xét trươc khi thiêt lap    

    #-------------------------------------------------------------------# Thiết lập Chỉ số Độc nhất / INDEX cho dữ liệu
    index_col_name = 'MaThietBi'
    data_1.index = data_1[index_col_name]
    data_2.index = data_2[index_col_name]
    # data_1.drop(index_col_name,axis = 1,inplace = True)
    # print(data_1.iloc[0])

    #-------------------------------------------------------------------# HỢP NHẤT 2 dữ liệu, ghi đè, giữ lại Dữ liệu thứ 2
    data_combine = pd.concat([data_1,data_2])
    data_combine = data_combine[~data_combine.index.duplicated(keep='last')]
    # print(data_combine)

    

    #-------------------------------------------------------------------# Ghi  Du lieu ra file
    data_write_file(data_combine,path_combine,title="Hợp nhất 2 dữ liệu")

    ask_prior = input(f"\tBạn ưu tiên giữ dữ liệu nào\n\t[1] Dữ liệu thứ nhất\n\t[2] Dữ liệu thứ hai\n\t{USER_INPUT_PREFIX}")
    ask_column_pair = input(f"\tChọn [Chỉ số Cột]:{USER_INPUT_PREFIX}")


    if ask_prior == '1':
        pass
    pass
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def change_new_df_column_names(path_data_last,df):
    """Thiết lập Tên cột dữ liệu mới cho Dữ liệu DF mới tạo"""
    #-------------------------------------------------------------------# Tiêu đề cột Dữ liêu cũ
    df_last = pd.read_json(path_data_last,orient='records')
    column_names_last = ','.join(df_last.columns)
    tips = '[!]Bạn [Nên] sử dụng các tên đã có [nếu cần thiết] và đủ [Số lượng Cột] '
    print(f'\t[Tên cột] của dữ liệu [Gần nhất]: \n{column_names_last}\n\t{tips}')
    print(BREAKER)
    column_names_current = df.columns
    #-------------------------------------------------------------------# Thiết lập Tiêu đề cột
    flag_names = False
    column_names = []
    tips = '\n\t\tChọn nhiều tên cột--Dùng--Dấu Phẩy [,]\n\t\tHủy tiến trình--Nhập--[Q_]\n\t\tReset bước này--Nhập--[R_]'            
    while not flag_names:
        column_names = input(f"\t[{6}] {menu[6]}: {USER_INPUT_PREFIX}")
        if column_names.lower() == 'q_':
            return 
        elif column_names.lower() == 'r_':
            flag_names = False
        else:
            try:
                column_names = column_names.split(',')        
                flag_names = len(column_names) == len(column_names_current)
                print(BREAKER)
            except:
                warning_1(menu[6],f"{promp_try}\n\t[Tips] Có thể bạn đã nhập [không] đủ số lượng cột")
                flag_names = False
    return column_names
def change_df_column_names(path_data):
    """Đổi Tên cột dữ liệu"""
    df = pd.read_json(path_data,orient='records')
    #-------------------------------------------------------------------# Tiêu đề cột Dữ liêu cũ
    column_names_current = df.columns
    column_names_last = ','.join(column_names_current)
    #-------------------------------------------------------------------# Thiết lập Tiêu đề cột
    tips = 'Bạn [Nên]:\n - Sử dụng các tên đã có [nếu cần thiết]\n - Nhập đủ [Tên] theo [Số lượng Cột]\n - Ghép các tên cột với Dấu Phẩy [,]'
    print(button_1('Tên cột'),button_1('của dữ liệu đươc tải'))
    print(f'\t{column_names_last}')
    print_text_box_L(tips)
    #-------------------------------------------------------------------# Validate tên cột
    flag_names = False
    column_names = []        
    while not flag_names:
        column_names = input(f"Nhập [Tên cột] mới\n{USER_INPUT_PREFIX} :")#f"\t[{6}] {menu[6]}: {USER_INPUT_PREFIX}")
        if column_names.lower() == 'q_':
            return 
        elif column_names.lower() == 'r_':
            flag_names = False
        else:
            try:
                column_names = column_names.split(',')        
                flag_names = len(column_names) == len(column_names_current)
                print(BREAKER)
            except:
                warning_1(menu[6],f"{promp_try}\n\t[Tips] Có thể bạn đã nhập [không] đủ số lượng cột")
                warning('Tiến trình chưa hoàn tất, vui lòng thử lại')
                flag_names = False
    if flag_names:
        df.columns = column_names
        ask_confirm = input(f"\tBạn muốn [ghi dữ liệu] (y/n):\n{USER_INPUT_PREFIX} ").lower()
        while ask_confirm == "y" or ask_confirm == "n":
            if ask_confirm == "y":
                data_archive(path_data)
                data_write_file(df,path_data)
            elif ask_confirm == "n":
                break
            warning('Tiến trình chưa hoàn tất, vui lòng thử lại')
            ask_confirm = input(f"\tBạn muốn [ghi dữ liệu] (y/n):\n{USER_INPUT_PREFIX} ").lower()
            
    
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def insert_column_index_row(df) -> pd.DataFrame:
    """Chèn thêm 1 dóng cuối bảng - là Số hiệu Cột của Dataframe"""
    column_numbers = [f"Cột {i}" for i in range(len(df.columns))] # cột số
    df = pd.concat([df, pd.DataFrame(np.array([column_numbers]),columns=df.columns)], ignore_index=True)    
    return df
    
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def read_configure_file(menu_path) -> any:
    "Phương thức đọc tập tin TXT configure, trả về Tên, mô tả, và DS menu"
    content = ''
    with open(menu_path,'r',encoding='utf-8') as f:
        content = [l for l in f.readlines()]
    content = ''.join(content)
    # print(content)
    # print([(m.start(0), m.end(0)) for m in re.finditer('\*',content)][-1])

    name = content.split('*')[1].strip()
    description = content.split('*')[2].strip()
    menu = pd.read_csv(menu_path,header=4+len(description.splitlines()),sep = '\t',dtype='str')
    return name,description,menu


if __name__ == '__main__':
    try:
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', 30)

        os.chdir(os.getcwd())
        path_root = os.getcwd()
        
        sub_dir = SUB_DATA_VTTB
        dat_name = DATA_NAME
        header = 'Trình xử lí dữ liệu VTTB'
        menu = menu_sub_update_by_excel

        # #-----------------------------------------------------------------------# load data VTTB
        # path_data_1 = f"{path_root}\\{SUB_DATA_VTTB}\\{DATA_NAME}.json"
        # data_1 = pd.read_json(path_data_1,orient='records')
        # #-----------------------------------------------------------------------# load data VTTB ton kho
        # path_data_2 = f"{path_root}\\{SUB_DATA_VTTB}\\{DATA_NAME_TON_KHO}.json"
        # data_2 = pd.read_json(path_data_2,orient='records')       
        # #-----------------------------------------------------------------------# load data TOng hop
        # # data_3 = data_builder(path_root,sub_dir,dat_name,header,menu)
        # path_data_3 = f"{path_root}\\{SUB_DATA_VTTB}\\{DATA_NAME_COMBINE}.json"
        # data_3 = pd.read_json(path_data_3,orient='records')      
        # #-----------------------------------------------------------------------# [build] data TOng hop tra cuu
        # path_data_4 = f"{path_root}\\{SUB_DATA_VTTB}\\{DATA_NAME_COMBINE_TRA_CUU}.json"
        # #data_4 = data_lookup_builder(data_3,path_data_4,DF_COLUMN_SEARCH_NAME)
        # #-----------------------------------------------------------------------# load data TOng hop tra cuu        
        # data_4 = pd.read_json(path_data_4,orient='records')

        
        main_data(os.getcwd(),SUB_DATA_VTTB,DATA_NAME_TON_KHO)

        menu_path = f"{path_root}\\{SUB_CONFIGURE}\\menu_data_types.txt"
        # test_menu = menu_program(menu_path)
        # print(os.path.exists(test_menu.get_path(2)))

        

        pass
    except KeyboardInterrupt:
        quit()
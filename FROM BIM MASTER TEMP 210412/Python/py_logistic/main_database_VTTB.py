# -*- coding: utf-8 -*-
"""Sub program : Quản lí cơ sở dữ liệu Vật tư thiết bị"""
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
import os,shutil
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from program_var import *
from handle_search import *
from handle_cmd import *
from handle_excel_files import *
from handle_decor_func import *
from main_program_configure import menu_program

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
    #-----------------------------------------------------# Main menu
    path_menu_conf = f"{path_root}\\{SUB_FOLDER_CONFIG}\\menu_data_main.txt"
    menu = menu_program(path_menu_conf)
    #-----------------------------------------------------# Menu Data
    path_data_conf =  f"{path_root}\\{SUB_FOLDER_CONFIG}\\menu_data_selector.txt"
    menu_data = menu_program(path_data_conf)

    menu.show_title_3()
    menu.show_description()
    menu.show_tips()
    while True:
        try:
            ask_menu = menu.ask_menu(button_text='Menu chương trình')
            if 'Interrupter' in ask_menu or type(ask_menu) == bool:
                raise Exception('Interrupted')
                continue
            if int(ask_menu):
                if not int(ask_menu) in range(len(menu.menu_list)):
                    print_text_box_R('Nhập sai. Vui lòng nhập đúng số hiệu menu',hoz='- ',ver='!')        
            #-----------------------------------------------------# BUILD DATA TỪ EXCEL
            elif ask_menu == "0":
                #-----------------------------------------------------# chọn dữ liệu đê bien tap                
                path_data = ask_data(menu_data)                
                while True:
                    try:
                        data_builder(path_root,path_data=path_data)[1]
                        print_text_box_L('Hoàn tất biên tập dữ liệu')                            
                    except:
                        print_text_box_L('Có lỗi trong quá trình biên tập, Vui lòng thử lại',hoz='- ',ver='!')
                        continue
            elif ask_menu == "1":
                #-----------------------------------------------------# chọn dữ liệu đê bien tap                
                path_data = ask_data(menu_data)     
                while True:
                    try:
                        path_data = menu_data.get_path(int(menu_data.ask_menu(button_text='Bạn chọn dữ liệu nào sau đây:')))
                        change_df_column_names(path_data)
                    except:
                        print_text_box_L('Có lỗi trong quá trình biên tập, Vui lòng thử lại',hoz='- ',ver='!')
                        continue

            elif ask_menu == "2":
                path_data = ask_data(menu_data)     
                while True:
                    try:
                        path_data = menu_data.get_path(int(menu_data.ask_menu(button_text='Bạn chọn dữ liệu nào sau đây:')))
                        # 
                    except:
                        print_text_box_L('Có lỗi trong quá trình biên tập, Vui lòng thử lại',hoz='- ',ver='!')
                        continue
            elif ask_menu == "3":
                path_data = ask_data(menu_data)     
                while True:
                    try:
                        path_data = menu_data.get_path(int(menu_data.ask_menu(button_text='Bạn chọn dữ liệu nào sau đây:')))
                        # 
                    except:
                        print_text_box_L('Có lỗi trong quá trình biên tập, Vui lòng thử lại',hoz='- ',ver='!')
                        continue
            elif ask_menu == "4":
                path_data = ask_data(menu_data)     
                while True:
                    try:
                        path_data = menu_data.get_path(int(menu_data.ask_menu(button_text='Bạn chọn dữ liệu nào sau đây:')))
                        # 
                    except:
                        print_text_box_L('Có lỗi trong quá trình biên tập, Vui lòng thử lại',hoz='- ',ver='!')
                        continue
            elif ask_menu == "5":
                path_data = ask_data(menu_data)     
                while True:
                    try:
                        path_data = menu_data.get_path(int(menu_data.ask_menu(button_text='Bạn chọn dữ liệu nào sau đây:')))
                        # 
                    except:
                        print_text_box_L('Có lỗi trong quá trình biên tập, Vui lòng thử lại',hoz='- ',ver='!')
                        continue
            elif ask_menu == "6":
                path_data = ask_data(menu_data)     
                while True:
                    try:
                        path_data = menu_data.get_path(int(menu_data.ask_menu(button_text='Bạn chọn dữ liệu nào sau đây:')))
                        # 
                    except:
                        print_text_box_L('Có lỗi trong quá trình biên tập, Vui lòng thử lại',hoz='- ',ver='!')
                        continue
            elif ask_menu == "7":
                path_data = ask_data(menu_data)     
                while True:
                    try:
                        path_data = menu_data.get_path(int(menu_data.ask_menu(button_text='Bạn chọn dữ liệu nào sau đây:')))
                        # 
                    except:
                        print_text_box_L('Có lỗi trong quá trình biên tập, Vui lòng thử lại',hoz='- ',ver='!')
                        continue
            elif ask_menu == "8":
                path_data = ask_data(menu_data)     
                while True:
                    try:
                        path_data = menu_data.get_path(int(menu_data.ask_menu(button_text='Bạn chọn dữ liệu nào sau đây:')))
                        # 
                    except:
                        print_text_box_L('Có lỗi trong quá trình biên tập, Vui lòng thử lại',hoz='- ',ver='!')
                        continue
        except Exception as ex:
            if ex.args[0] == 'Interrupted':
                ask_menu = ask_menu.split(':')[-1]
                if ask_menu.lower() == 'qq': # quit = QQ
                    print_text_box_R('Bạn chọn [Thoát] chương trình\nChương trình đang thoát\nHẹn gặp lại bạn lần sau',hoz= ' - ')
                    quit()
                elif ask_menu.lower() == 'zz': # restart = ZZ
                    print_text_box_R('Bạn chọn [Restart] chương trình\nChương trình đang Khởi động lại',hoz=' - ')
                    continue
                elif ask_menu.lower() == 'q_': # reset = Q_
                    print_text_box_R('Bạn chọn [Thoát]/ [Bỏ qua] tiến trình\nLưu ý: Có thể các bước sau sẽ lỗi thì thiếu đầu vào',hoz=' - ')
                    continue
                elif ask_menu.lower() == 'z_': # reset = Q_
                    print_text_box_R('Bạn chọn [Backward]/Quay lại 1 bước tiến trình\nChương trình đang quay lại 1 bước',hoz=' - ')
                    continue
                elif ask_menu == True or ask_menu == False : # output Boolean
                    menu.show_warning()
                    continue
            else:
                menu.show_warning()
        
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
    

def ask_data(menu_data):
    """Hỏi user chọn data, trả về Đường dẫn tồn tại hoặc None"""
    path_data = None
    while True:
        try:
            menu_data.show_title_3()
            ask_data = menu_data.ask_menu(button_text='Vui lòng chọn dữ liệu để biên tập:',breaker = BREAKER_SEC)
            if 'Interrupter' in ask_data or type(ask_data) == bool:
                raise Exception('Interrupted',ask_data)
                continue
            path_data = menu_data.get_path(int(ask_data))
            if not int(ask_data) and not int(ask_data) in range(len(menu_data.menu_list)):
                raise Exception('Wrong input',ask_data)
            else:
                print(f'Bạn sắp biên tập dữ liệu {path_data}')
                break
        except Exception as ex:
            if ex.args[0] == 'Interrupted':
                ask_data = ask_data.split(':')[-1]
                if ask_data.lower() == 'qq': # quit = QQ
                    print_text_box_R('Bạn chọn [Thoát] chương trình\nChương trình đang thoát\nHẹn gặp lại bạn lần sau',hoz= ' - ')
                    quit()
            else:
                print_text_box_L('Nhập sai số hiệu\nVui lòng thử lại',hoz='- ',ver='!')
    return path_data
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

# @loop_flow_1()
def data_builder(path_root,path_data=None) -> pd.DataFrame:
    """### Description
    - Phương thức Xử lí dữ liệu
    Sử dụng Đại trà, không cụ thể cho loại dữ liệu nào
    ### Input:
    - path_root (str) --> dirpath"""
    
    df_copy = []
    path_data_last = ''
    # ----------------------------------------------------------# Setup PANDAS
    # pd.set_option('display.max_rows', None)                       
    # pd.set_option('display.max_columns', 10)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 30)
          
    # ----------------------------------------------------------# Load menu = Verify menu data
    menu_path = f"{path_root}\\{SUB_FOLDER_CONFIG}\\menu_data_builder.txt"
    if os.path.exists(menu_path):
        menu_ = menu_program(menu_path)
        menu_.show_title_3()
        menu_.show_description()
    else:
        return
    # ----------------------------------------------------------# Load menu = Verify Data soruce
    if not path_data or not os.path.exists(path_data):
        print_text_box_L('Không tồn tại nguồn dữ liệu')
        return
    # ----------------------------------------------------------# LOOP START
    while True:        
        try:
            path_data_last = path_data
            menu_.ask_menu(promp = 'Enter để tiếp tục',button_text='Đấy là toàn bộ quá trình bạn sẽ thực hiện:')
            
            # ----------------------------------------------------------# ask : Chọn [đường dẫn file] Excel dữ liệu
            while True:
                try:
                    path_data_excel = menu_.ask_step(0)
                    if not os.path.exists(path_data_excel):
                        raise Exception('Path not exist')
                    # ----------------------------------------------------------# show tên sheet excel
                    print(button_1("Danh sách các [Sheet]:"))
                    sheets = show_excel_sheet(path_data_excel)
                    break
                except:
                    menu_.warning(0)
            # ----------------------------------------------------------# ask : Chọn [tên Sheet] Excel
            
            while True:
                try:
                    excel_sheet_name = menu_.ask_step(1,pre_promp='Vui lòng')
                    if not excel_sheet_name in sheets:
                        raise Exception('Sheet not exist')
                    break
                except Exception as ex:
                    menu_.warning(1)

            # ----------------------------------------------------------# Thiết lập số lượng cột tôi đa
            ask_max_cols = 10
            while True:
                try:
                    ask_max_cols = int(menu_.ask_step(2))
                    if ask_max_cols > 10:
                        menu_.warning(2)                        
                        ask_max_cols = 10      
                    pd.set_option('display.max_columns', ask_max_cols)
                    break
                except:
                    menu_.warning(2)

            # ----------------------------------------------------------# Tải dữ liệu excel
            df = pd.read_excel(path_data_excel,excel_sheet_name)#,dtype='string')
            df = df[df.columns[0:ask_max_cols]]
            df_copy = insert_column_index_row(df)
            # ----------------------------------------------------------# User review
            print(button_1('Tải Dữ liệu hoàn tất:'),'\n',df_copy)
            print(BREAKER_SEC)
            menu_.ask_step(3,pre_promp='Sau khi',post_promp='Enter để tiếp tục')
            
            # ----------------------------------------------------------# Chọn dòng Tiêu đề Cột
            row_header = 0
            while True:
                try:
                    row_header = int(menu_.ask_step_w_tips(4))
                    if df.iloc[row_header].to_list():
                        break
                except:
                    menu_.warning(4)
            # ----------------------------------------------------------# Chọn các cột dữ liệu
            columns = []
            while True:
                try:
                    columns = menu_.ask_step_w_tips(5)
                    columns = [int(i) for i in columns.replace(" ","").split(',')]
                    if [df[df.columns[i]] for i in columns]: 
                        break                    
                except:
                    menu_.warning(5)


            # ----------------------------------------------------------# Chọn cột dữ liệu Lọc NA
            column_drop = columns[0] # mặc định là cột đầu tiên
            while True: #flag_column_drop != True:     
                try:       
                    column_drop = menu_.ask_step_w_tips(6)
                    if column_drop.lower() == 'a':
                        column_drop = columns
                    else:
                        column_drop = [int(i) for i in column_drop.replace(" ","").split(',')]                
                        if not set(column_drop).issubset(columns):
                            raise Exception('Lỗi')
                    
                    #-------------------------------------------------------------------# Xử lí DF = Lọc cột giữ lai + Bỏ NA
                    df_copy = None
                    df_copy = pd.read_excel(path_data_excel,excel_sheet_name
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
                    if type(df_copy) == DataFrame:
                        break
                except:
                    menu_.warning(6)
            
            print_text_box_L("Hoàn tất xử lí dữ liệu, Bạn sắp xem nhanh [1 phần] dữ liệu kết quả:")
            print(df_copy.head(10))
            
            #-------------------------------------------------------------------# Thiết lập Tiêu đề cột
            df_last = pd.read_json(path_data_last,orient='records')
            column_names_last = ','.join(df_last.columns)
            while True:
                try:
                    print_text_box_L(f"Bạn đang xem Danh sách [Tên cột] của dữ liệu [Hiện hữu]:")
                    print(column_names_last)
                    column_names_current = df_copy.columns
                    column_names = []                
                    column_names = menu_.ask_step_w_tips(7,post_promp = "Nhập danh sách tên cột") # input(f"\t[{6}] {menu[6]}: {USER_INPUT_PREFIX}")                
                    column_names = column_names.split(',')                   
                    if len(column_names) == len(column_names_current):
                        #-------------------------------------------------------------------# Show Du lieu
                        df_copy.columns = column_names
                        df_copy_show =  insert_column_index_row(df_copy)
                        print(df_copy_show)
                        break
                    else:
                        raise Exception('Lỗi')
                except Exception as ex:
                    menu_.warning(7)                         

            menu_.ask_step(8,post_promp='Enter để Xác nhận:')            
            #-------------------------------------------------------------------# Ghi  Du lieu ra file
            menu_write = menu_.get_step(9)

            #-------------------------------------------------------------------# Fill gia1 tri NA
            df_copy.fillna('NA',inplace= True)

            data_write_file(df_copy,path_data_last,menu = menu_write)
            # df_copy = data_write_file(df_copy,path_data_last,title=menu[8])
            
            break
            
        except:
            continue
#-----------------------------------------------------------------------------------------------------------------------------------------#
def data_write_file_append(df,path_data) -> pd.DataFrame:
    """Trình xừ lí: Ghi dữ liệu ra Tập tin [Nối tiếp]
    ### Input:
    - df (DataFrame) : Dữ liệu
    - path_data (str) : đường dẫn tập tin"""
    df = pd.concat([df,pd.read_json(path_data,orient='records')], ignore_index=True)
    df.to_json(path_data,orient='records')  
    print_text_box_L('Thành công Nối tiếp Dữ liệu')
    print(f'[OUT] Dữ liệu mới: {path_data}')
    return df
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def data_write_file(df,path_data,title = None,menu = None) -> pd.DataFrame:
    """Trình xừ lí: Ghi dữ liệu ra Tập tin ([Ghi đè] hoặc [Nối tiếp])
    ### Input:
    - df (DataFrame) : Dữ liệu
    - path_data (str) : đường dẫn tập tin
    - title: tên tiến trình
    - menu: menu tiến trình"""
    # index = 0
    # tips = ''
    # if type(menu) == list and len(menu)>= 2:
    #     index = int(menu[0])
    #     title = menu[1]
    #     tips = menu[2]    
    while True:
        try:
            ask_export_data = menu_program.ask_step_w_tips_free(menu,pre_promp='Vui lòng xác nhận (y/n) bạn muốn: ')
            path_xml = f"{path_data.split('.json')[0]}.xml"
            if ask_export_data ==  True:
                ask_append = input(f"{button_1('Chọn kiểu ghi:')}:\n\t[1] [Nối tiếp] vào dữ liệu cũ \n\t[2] [Ghi đè] /thay thế dữ liệu cũ\n{USER_INPUT_PREFIX} ").lower()
                print(BREAKER)                  
                if ask_append == "1":
                    df = pd.concat([df,pd.read_json(path_data,orient='records')], ignore_index=True)                    
                    
                    df.to_xml(path_xml)  
                    df.to_json(path_data,orient='records')  

                    print_text_box_L('Thành công Nối tiếp Dữ liệu')
                    print(f'[OUT] Dữ liệu mới:\n{path_data}\n{path_xml}')
                    return df
                elif ask_append == "2":    
                    #-------------------------------------------------------------------# Ghi ra JSON File    
                    df.to_xml(path_xml)  
                    df.to_json(path_data,orient='records')
                    print(f'[OUT] Dữ liệu mới:\n{path_data}\n{path_xml}')
                    return df
                else:
                    warning('Tiến trình chưa hoàn tất, vui lòng thử lại') 
        except:
            warning('Tiến trình chưa hoàn tất, vui lòng thử lại') 
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
def change_new_df_column_names(path_data_last,df,menu=None,step_number=0):
    """Thiết lập Tên cột dữ liệu mới cho Dữ liệu DF mới tạo"""
    #-------------------------------------------------------------------# Tiêu đề cột Dữ liêu cũ
    df_last = pd.read_json(path_data_last,orient='records')
    column_names_last = ','.join(df_last.columns)
    if type(menu) == menu_program:
        menu.ask_step_w_tips(step_number,post_promp = "Nhập danh sách tên cột")
    else:
        return
    print_text_box_L(f"Bạn đang xem Danh sách [Tên cột] của dữ liệu [Hiện hữu]:")
    print(column_names_last)

    column_names_current = df.columns
    #-------------------------------------------------------------------# Thiết lập Tiêu đề cột
    flag_names = False
    column_names = []    
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

# @loop_flow_1()
def change_df_column_names(path_data):
    try:
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
    except:
        return 'fail'
    
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

        menu_path = f"{path_root}\\{SUB_FOLDER_CONFIG}\\menu_data_types.txt"
        # test_menu = menu_program(menu_path)
        # print(os.path.exists(test_menu.get_path(2)))

        

        pass
    except KeyboardInterrupt:
        quit()
# -*- coding: utf-8 -*-
"""Chương trình Vận tải - Kho vận - Điện tử 
Cofico e-USD Program
Version 01"""
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#

import pandas as pd
import os,json
from handle_cmd import *
from handle_search import *
from handle_string import concat_df_series
import logging

from program_var import *
from handle_data_user import *
from main_tra_cuu_VTTB_ke_hoach import *
from main_database_VTTB import *
from main_program_configure import menu_program,menu_manager

#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
# GLOBAL VARIABLE
debug_file_name = f"{os.getcwd()}\\debug\\debug-{time.strftime('%y%m%d %H%M%S',time.localtime(time.time()))}.txt"
logging.basicConfig(filename = debug_file_name,
                    level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Program START')
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#
# FUNCTION: BIÊN TẬP DỮ LIỆU CƠ SỞ
#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
def edit_database():
    """Chỉnh sửa Dữ liệu cơ sở"""
    global PATH_ROOT_DIR
    global DATA_VTTB , PATH_DATA_VTTB
    global DATA_VTTB_TRA_CUU , PATH_DATA_VTTB_TRA_CUU
    global DATA_TON_KHO , PATH_DATA_TON_KHO
    global DATA_COMBINE , PATH_DATA_COMBINE
    global DATA_COMBINE_TRA_CUU,PATH_DATA_COMBINE_TRA_CUU
    print(BREAKER)
    show_heading_1('trình biên tập dữ liệu vttb\n[dANH MỤC] - [TỒN KHO] - [TỔNG HỢP]')
    #---------------------------------------------------# BIÊN TẬP DỮ LIỆU [DANH MỤC] VTTB
    ask_skip = input(f'\t Bạn sắp biên tập Dữ liệu [Danh mục] VTTB, bỏ qua chọn n (y/n):{USER_INPUT_PREFIX} ')
    if ask_skip.lower() == 'y':
        spin_three_dots('Backup data ')              
        data_archive(PATH_DATA_VTTB)
        spinWaiting(BREAKER)             
        DATA_VTTB = data_builder(PATH_ROOT_DIR,SUB_DATA_VTTB,DATA_NAME,menu_sub_update_by_excel,header = 'biên tập dữ liệu [danh mục] vttb')
        spin_three_dots('Backup data ')   
        data_archive(PATH_DATA_VTTB_TRA_CUU)                
        spinWaiting(BREAKER)           
        show_heading_3('trình cập nhật dữ liệu [tra cứu] vttb')     
        DATA_VTTB_TRA_CUU = data_lookup_builder(DATA_VTTB,PATH_DATA_VTTB_TRA_CUU,DF_COLUMN_SEARCH_NAME)
    print(BREAKER)
    #---------------------------------------------------# BIÊN TẬP DỮ LIỆU VTTB [TỒN KHO]
    print(BREAKER)
    ask_skip = input(f'\tBạn sắp biên tập Dữ liệu VTTB [Tồn kho], bỏ qua chọn n (y/n):{USER_INPUT_PREFIX} ')
    if ask_skip.lower() == 'y':
        spin_three_dots('Backup data ')
        spinWaiting(BREAKER)
        data_archive(PATH_DATA_TON_KHO)
        spinWaiting(BREAKER)             
        DATA_TON_KHO = data_builder(PATH_ROOT_DIR,SUB_DATA_VTTB,DATA_NAME_TON_KHO,menu_sub_update_by_excel,header = 'biên tập dữ liệu vttb [tồn kho]')
        print(BREAKER)
    #---------------------------------------------------# BIÊN TẬP DỮ LIỆU VTTB [TỔNG HỢP]
    print(BREAKER)
    ask_skip = input(f'\tBạn sắp biên tập Dữ liệu VTTB [TỔNG HỢP], bỏ qua chọn n (y/n):{USER_INPUT_PREFIX} ')
    if ask_skip.lower() == 'y':
        spin_three_dots('Backup data ')
        spinWaiting(BREAKER)
        data_archive(PATH_DATA_COMBINE)
        spinWaiting(BREAKER)        
        DATA_COMBINE = data_builder(PATH_ROOT_DIR,SUB_DATA_VTTB,DATA_NAME_COMBINE,menu_sub_update_by_excel,header = 'biên tập dữ liệu vttb [tổng hợp]')
        print(BREAKER)
        spin_three_dots('Backup data ')   
        data_archive(PATH_DATA_COMBINE_TRA_CUU)                
        spinWaiting(BREAKER)           
        show_heading_3('trình cập nhật dữ liệu [Tổng Hợp] [Tra Cứu] vttb')     
        DATA_COMBINE_TRA_CUU = data_lookup_builder(DATA_COMBINE,PATH_DATA_COMBINE_TRA_CUU,DF_COLUMN_SEARCH_NAME)
       
    
    
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#

def data_refresh():
    """Cập nhật Dữ liệu cơ sở : DM VTTB + TON KHO + TRA CUU"""
    global PATH_ROOT_DIR
    global DATA_VTTB_COLUMN_HEADS
    global DATA_VTTB , PATH_DATA_VTTB
    global DATA_VTTB_TRA_CUU , PATH_DATA_VTTB_TRA_CUU
    global DATA_TON_KHO , PATH_DATA_TON_KHO
    global DATA_COMBINE , PATH_DATA_COMBINE
    global DATA_COMBINE_TRA_CUU,PATH_DATA_COMBINE_TRA_CUU

    DATA_VTTB = pd.read_json(PATH_DATA_VTTB, orient='records') if os.path.exists(PATH_DATA_VTTB) else None
    DATA_VTTB_TRA_CUU = pd.read_json(PATH_DATA_VTTB_TRA_CUU, orient='records') if os.path.exists(PATH_DATA_VTTB_TRA_CUU) else None
    DATA_TON_KHO = pd.read_json(PATH_DATA_TON_KHO, orient='records') if os.path.exists(PATH_DATA_TON_KHO) else None
    DATA_COMBINE = pd.read_json(PATH_DATA_COMBINE, orient='records') if os.path.exists(PATH_DATA_COMBINE) else None
    DATA_COMBINE_TRA_CUU =  pd.read_json(PATH_DATA_COMBINE_TRA_CUU, orient='records') if os.path.exists(PATH_DATA_COMBINE_TRA_CUU) else None

    DATA_VTTB_COLUMN_HEADS = DATA_VTTB.columns

    logging.info('Update data path SUCCESSFUL')
    # print('\tRefresh Done !!')

#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#
# START FUNCTION
#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
def start_program():
    """
        BẮT ĐẦU CHƯƠNG TRÌNH LOGISTIC
    """
    global PATH_ROOT_DIR,PATH_ROOT_DIR_EXIST,USER_NAME, USER_DATA, PATH_USER_LOG,TIME_START,DATA_VTTB_TRA_CUU ,DATA_VTTB
    global DATA_TON_KHO,PATH_DATA_TON_KHO,DATA_NAME_TON_KHO,PATH_DATA_VTTB_TON_KHO_EXIST
    global PATH_DATA_VTTB,PATH_DATA_VTTB_TRA_CUU,PATH_DATA_DM_VTTB_EXIST,PATH_DATA_VTTB_SEARCH_EXIST
    global DATA_NAME, DATA_SEARCH_NAME,DATA_VTTB_COLUMN_HEADS,SUBFOLDER_DATA_USER,ASK_MENU
    global DATA_NAME_COMBINE,DATA_COMBINE,PATH_DATA_COMBINE,PATH_DATA_VTTB_COMBINE_EXIST
    global DATA_NAME_COMBINE_TRA_CUU,DATA_COMBINE_TRA_CUU,PATH_DATA_COMBINE_TRA_CUU,PATH_DATA_VTTB_COMBINE_TRA_CUU_EXIST
    global DATA_LIST, DATA_PATH_LIST,DATA_PATH_EXIST_LIST
    
    global PATH_CONFIG , MENU_PROGRAM


    #-------------------------------------------------------# ASK DIR ROOT & USERNAME & SAY WELCOME
    spinWaiting(BREAKER)
    while PATH_ROOT_DIR_EXIST == False:
        PATH_ROOT_DIR = input(f"\tVui lòng Chọn đường dẫn Thư mục gốc:{USER_INPUT_PREFIX} ")
        spin_three_dots(f"\tĐang kiểm tra Root path ")
        PATH_ROOT_DIR_EXIST = os.path.isdir(PATH_ROOT_DIR)
        print(f"\t(Checked!) Thư mục gốc có tồn tại !")
        # TODO: KIỂM TRA SUBFOLDER BÊN TRONG CÓ ĐÚNG LÀ DÀNH CHO CHƯƠNG TRÌNH LOGISTIC KO

    logging.info('Root Path VERIFIED') 
    # TODO: TIẾN TRÌNH LOGIN
    # user_name,user_password = login()
    # print(f"\tMật mã:\t{'*'*len(user_password)}",end='\r')    
    # check_user_name_already(user_name,user_password,fake_data)
    # print(user_name,user_password,time_start)
    USER_NAME = input(f"\tVui lòng cho biết TÊN của bạn:{USER_INPUT_PREFIX} ").upper()
    TIME_START = time.strftime("%y%m%d %H%M%S",time.localtime(time.time()))       
    #-------------------------------------------------------# TẠO DỮ LIỆU NGƯỜI DÙNG
    PATH_USER_LOG = f"{PATH_ROOT_DIR}\\{SUBFOLDER_DATA_USER}\\{USER_NAME}-{TIME_START}.txt"
    log_user_action(f"PATH_ROOT\t{PATH_ROOT_DIR}")
    log_user_action(f"USER_NAME\t{USER_NAME}")
    log_user_action(f"TIME_OPEN\t{TIME_START}")    
    logging.info(f"User Data INITIATED\t{PATH_USER_LOG}")
    
    show_heading_4(PROMP_SAY_HI.format(USER_NAME))
    show_heading_4(PROMP_WELCOME.format(USER_NAME))
    
    logging.debug('User input DONE')

    #----------------------------------------------------# CHECK CÓ DỮ LIỆU VTTB
    PATH_DATA_VTTB = f"{PATH_ROOT_DIR}\\{SUB_DATA_VTTB}\\{DATA_NAME}.json"
    PATH_DATA_DM_VTTB_EXIST = os.path.exists(PATH_DATA_VTTB)
    
    #----------------------------------------------------# CHECK CÓ DỮ LIỆU VTTB TRA CỨU
    PATH_DATA_VTTB_TRA_CUU = f"{PATH_ROOT_DIR}\\{SUB_DATA_VTTB}\\{DATA_SEARCH_NAME}.json"#PATH_ROOT_DIR+"\\"+data_search_name+".json"
    PATH_DATA_VTTB_SEARCH_EXIST = os.path.isfile(PATH_DATA_VTTB_TRA_CUU)      

    #----------------------------------------------------# CHECK CÓ DỮ LIỆU VTTB TỒN KHO
    PATH_DATA_TON_KHO = f"{PATH_ROOT_DIR}\\{SUB_DATA_VTTB}\\{DATA_NAME_TON_KHO}.json"
    PATH_DATA_VTTB_TON_KHO_EXIST = os.path.isfile(PATH_DATA_TON_KHO)      
    
    #----------------------------------------------------# CHECK CÓ DỮ LIỆU VTTB TỔNG HỢP
    PATH_DATA_COMBINE = f"{PATH_ROOT_DIR}\\{SUB_DATA_VTTB}\\{DATA_NAME_COMBINE}.json"
    PATH_DATA_VTTB_COMBINE_EXIST = os.path.isfile(PATH_DATA_COMBINE)      

    #----------------------------------------------------# CHECK CÓ DỮ LIỆU VTTB TỔNG HỢP TRA CỨU
    PATH_DATA_COMBINE_TRA_CUU = f"{PATH_ROOT_DIR}\\{SUB_DATA_VTTB}\\{DATA_NAME_COMBINE_TRA_CUU}.json"
    PATH_DATA_VTTB_COMBINE_TRA_CUU_EXIST = os.path.isfile(PATH_DATA_COMBINE_TRA_CUU)      

        
    #----------------------------------------------------# CHECK CÓ ĐỦ TOÀN BỘ DỮ LIỆU VTTB TỔNG HỢP TRA CỨU
    flag_have_data = PATH_DATA_DM_VTTB_EXIST == PATH_DATA_VTTB_SEARCH_EXIST == PATH_DATA_VTTB_COMBINE_EXIST == PATH_DATA_VTTB_TON_KHO_EXIST == PATH_DATA_VTTB_COMBINE_TRA_CUU_EXIST ==True
    
    #----------------------------------------------------# UPDATE DATA 
    data_refresh()

    while not flag_have_data:
        print(BREAKER)
        print(f"\tDữ liệu chưa được Tải đầy đủ, bạn sắp đi tới Tiến trình quản lí dữ liệu")
        print(BREAKER)
        print(f"""\tTình trạng tải dữ liệu\n\tVTTB_DM : {PATH_DATA_DM_VTTB_EXIST}\n\tVTTB_DM_TRA_CUU : {PATH_DATA_VTTB_SEARCH_EXIST}\n\tVTTB_TON_KHO : {PATH_DATA_VTTB_TON_KHO_EXIST}\n\tVTTB_TONG_HOP : {PATH_DATA_VTTB_COMBINE_EXIST}\n\tVTTB_TONG_HOP_TRA_CUU : {PATH_DATA_VTTB_COMBINE_TRA_CUU_EXIST}""")
        #----------------------------------------------------# RÀ SOÁT BIÊN TẬP DỮ LIỆU CHO ĐỦ
        edit_database()
        PATH_DATA_DM_VTTB_EXIST = os.path.exists(PATH_DATA_VTTB)
        PATH_DATA_VTTB_SEARCH_EXIST = os.path.isfile(PATH_DATA_VTTB_TRA_CUU)      
        PATH_DATA_VTTB_TON_KHO_EXIST = os.path.isfile(PATH_DATA_TON_KHO)      
        PATH_DATA_VTTB_COMBINE_EXIST = os.path.isfile(PATH_DATA_COMBINE)   
        PATH_DATA_VTTB_COMBINE_TRA_CUU_EXIST = os.path.isfile(PATH_DATA_COMBINE_TRA_CUU)         
        flag_have_data = PATH_DATA_DM_VTTB_EXIST == PATH_DATA_VTTB_SEARCH_EXIST == PATH_DATA_VTTB_COMBINE_EXIST == PATH_DATA_VTTB_TON_KHO_EXIST == PATH_DATA_VTTB_COMBINE_TRA_CUU_EXIST == True

    #----------------------------------------------------# UPDATE DATA 
    data_refresh()
    logging.debug('Data of Material and Equipmetn loaded DONE')
    print(BREAKER)
    
    #-------------------------------------------------------# CONFIGURER
    menu_program = menu_manager(PATH_CONFIG)
    menu_logistic = menu_program.menu_by_global_numbers(['1','2','3','4','5','7','8','QQ','ZZ','MN'])
    #-------------------------------------------------------# ASK MENU
    return menu_program.ask_input(menu_logistic,button_text='Danh sách menu chương trình:')
    

def log_user_action(action):

    """LƯU HOẠT ĐỘNG NGƯỜI DÙNG"""

    global PATH_USER_LOG
    with open(PATH_USER_LOG,'a',encoding='utf-8') as f:
        f.write(f"{action}\n")

#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#
# MAIN PROGRAM
#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
def main():
    # LOAD GLOBAL VARS
    global PATH_ROOT_DIR , PATH_USER_LOG , TIME_END,TIME_START,USER_NAME ,ASK_MENU
    global DATA_VTTB_COLUMN_HEADS, SEARCH_SEPERATOR, SUBFOLDER_DATA_USER
    global DATA_VTTB , PATH_DATA_VTTB , PATH_DATA_DM_VTTB_EXIST
    global DATA_VTTB_TRA_CUU , PATH_DATA_VTTB_TRA_CUU, PATH_DATA_VTTB_SEARCH_EXIST    
    global DATA_TON_KHO , PATH_DATA_TON_KHO , DATA_NAME_TON_KHO , PATH_DATA_VTTB_TON_KHO_EXIST
    global DATA_COMBINE , PATH_DATA_COMBINE , DATA_NAME_COMBINE , PATH_DATA_VTTB_COMBINE_EXIST
    global DATA_COMBINE_TRA_CUU, PATH_DATA_COMBINE_TRA_CUU, DATA_NAME_COMBINE_TRA_CUU , PATH_DATA_VTTB_COMBINE_TRA_CUU_EXIST
    
    global PATH_CONFIG , MENU_PROGRAM        
    #----------------------------------------------------#  SETUP PANDAS
    pd.set_option('display.max_rows', 0)
    pd.set_option('display.max_columns', 30)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 30)

    #----------------------------------------------------# START PROGRAM
    ASK_MENU = start_program()
    
    while ASK_MENU != "qq":
        spinWaiting(BREAKER)
        #----------------------------------------------------#  SHOW SUB MENU
        if ASK_MENU == "1":
            ASK_MENU = show_menu_tree_view(PROMP_MAIN_MENU,level=2,keep_group = '1')
        elif ASK_MENU == "2":
            ASK_MENU = show_menu_tree_view(PROMP_MAIN_MENU,level=2,keep_group = '2')
        elif ASK_MENU == "3":
            ASK_MENU = show_menu_tree_view(PROMP_MAIN_MENU,level=2,keep_group = '3')
        elif ASK_MENU == "4":
            ASK_MENU = show_menu_tree_view(PROMP_MAIN_MENU,level=2,keep_group = '4')
        elif ASK_MENU == "5":
            ASK_MENU = show_menu_tree_view(PROMP_MAIN_MENU,level=2,keep_group = '5')
        elif ASK_MENU == "6":
            ASK_MENU = show_menu_tree_view(PROMP_MAIN_MENU,level=2,keep_group = '6')
        elif ASK_MENU == "7":
            ASK_MENU = show_menu_tree_view(PROMP_MAIN_MENU,level=2,keep_group = '7')
        elif ASK_MENU == "8":
            ASK_MENU = show_menu_tree_view(PROMP_MAIN_MENU,level=2,keep_group = '8')

        #----------------------------------------------------#  TRA CỨU VẬT TƯ
        elif ASK_MENU == "1.0":
            logging.debug('User lookup START')
            search_value = input(promp_search_value)
            while search_value.lower() != "q_":                
                search_result = None
                key_words = []            
                if not SEARCH_SEPERATOR in search_value:
                    #----------------------------------------------------# NẾU TỪ KHÓA TÌM KIẾM CHỈ CÓ 1
                    logging.debug('NO search-seperator in search value inputed')
                    spinWaiting(BREAKER)
                    search_result = searcher (search_value,DATA_VTTB_TRA_CUU,DF_COLUMN_SEARCH_NAME)
                    print (f"\tKết quả tìm kiếm cho từ khóa '{search_value}'\t{search_result.shape[0]}")
                    log_user_action(f"SEARCH\t{key_words}\t{search_result.shape[0]}")
                    print(search_result)  
                else: 
                    #----------------------------------------------------# NẾU TỪ KHÓA TÌM KIẾM NHIỀU HƠN 1, ÁP DỤNG QUY TẮC PHỂU LỌC
                    key_words = search_value.split(SEARCH_SEPERATOR)
                    spinWaiting(BREAKER)
                    print(key_words)
                    for kw in key_words:
                        search_result = searcher (kw,DATA_VTTB_TRA_CUU,DF_COLUMN_SEARCH_NAME)
                        print (f"\tKết quả tìm kiếm cho từ khóa '{kw}'\t{search_result.shape[0]}")
                        print (search_result)
                        print(BREAKER)
                    log_user_action(f"SEARCH\t{key_words}")
                    
                logging.debug('User lookup DONE')
                search_value = input(promp_search_value)            
        #----------------------------------------------------# Xuất excel
        elif ASK_MENU == "1.0.0":
            pass
        #----------------------------------------------------#  XEM CHI TIẾT VTTB THEO MÃ VẬT LIỆU
        elif ASK_MENU == "1.0.1":
            pass
        #----------------------------------------------------#  XEM CHI TIẾT VTTB THEO CHỈ SỐ HÀNG
        elif ASK_MENU == "1.0.2":
            detail_id = input(f"\tIndex:(Là số hiệu Cột đầu tiên của các bảng Thông tin){USER_INPUT_PREFIX} ")
            details = ""
            spinWaiting(BREAKER)
            if int(detail_id):
                details = DATA_VTTB.loc[int(detail_id)]
                print(f"\tBạn đang xem thông tin chi tiết của \n\t\t\t{details}")
                log_user_action(f"WATCH\t{detail_id}")
            else:
                print(f"\tBạn nhập sai kiểu dữ liệu, cần là Số Nguyên\n\tVd: 1234")
                
        #----------------------------------------------------#  XEM CHI TIẾT VTTB THEO CHỈ SỐ HÀNG + TÊN CỘT    
        elif ASK_MENU == "1.0.3":
            try:
                detail_id, column_name = input("Index,Column:(Số hiệu,Tên cột) ").split(",")
                details = ""
                spinWaiting(BREAKER)
                if int(detail_id) and column_name:
                    details = DATA_VTTB.loc[int(detail_id)][column_name]
                    print(f"\tBạn đang xem thông tin chi tiết của \n\t\t\t{details}")
                    log_user_action(f"WATCH\t{detail_id},{column_name}")                    
                else:
                    print(f"\tBạn nhập sai dữ liệu, cần là 1 chuỗi :Số Nguyên,Tên Cột\n\tVd: 1234,TenThietBi")                    
            except:
                logging.error('An error has occurred.')
                pass
        #----------------------------------------------------#  TRA CỨU DỮ LIỆU VẬT TƯ THIẾT BỊ [TỒN KHO]
        elif ASK_MENU == "1.1":
            time_access = time.strftime("%y%m%d %H%M%S",time.localtime(time.time()))
            show_heading_1('Trình tra cứu thông tin tồn kho')            
            log_user_action(f"ACCESS_DATA_STORAGE\t{PATH_DATA_TON_KHO}\t{time_access}")
            log_user_action(f"DATA_STORAGE\t{DATA_TON_KHO.shape[0]}")
        #----------------------------------------------------#  TRA CỨU KẾ HOẠCH VTTB
        elif ASK_MENU == "1.2":
            pass
        #----------------------------------------------------# LƯU DANH MỤC VẬT TƯ YÊU THÍCH
        elif ASK_MENU == "1.3":            
            print(PATH_USER_LOG)
            try:                
                saved_selection = input(f"\tHãy nhập Mã Vật Tư bạn Muốn lưu\n\t(Tip: dùng , để lưu nhiều mã):{USER_INPUT_PREFIX} ")
                #verify
                flag_exist = True
                if flag_exist:
                    time_select = round(time.time())
                    user_selection = {"MaVatTu":saved_selection,"Time":time_select}           
                if not os.path.exists(PATH_USER_LOG):
                    with open(PATH_USER_LOG,'w') as wud:
                        wud.write(json.dumps(user_selection,indent=4,sort_keys=True))
                    spinWaiting(BREAKER)
                    print (f"\tThành công lưu thông tin tại {PATH_USER_LOG}")
            except Exception as ex:
                print (ex)
                logging.error('An error has occurred.')
                print("\t[!] Có lỗi gì đó xảy ra, vui lòng thử lại")
                pass
        #----------------------------------------------------#  XUAT DU LIEU BO SUU TAP
        elif ASK_MENU == "1.3.1":
            pass
        #----------------------------------------------------#  TRA CỨU VẬT TƯ [tổng hợp]
        elif ASK_MENU == "1.4":
            logging.debug('User lookup [Combine Data] START')
            search_value = input(promp_search_value)
            while search_value.lower() != "q_":                
                search_result = None
                key_words = []            
                if not SEARCH_SEPERATOR in search_value:
                    #----------------------------------------------------# NẾU TỪ KHÓA TÌM KIẾM CHỈ CÓ 1
                    logging.debug('NO search-seperator in search value inputed')
                    spinWaiting(BREAKER)
                    search_result = searcher(search_value,DATA_COMBINE_TRA_CUU,DF_COLUMN_SEARCH_NAME)
                    print (f"\tKết quả tìm kiếm cho từ khóa '{search_value}'\t{search_result.shape[0]}")
                    log_user_action(f"SEARCH\t{key_words}\t{search_result.shape[0]}")
                    print(search_result)  
                else: 
                    #----------------------------------------------------# NẾU TỪ KHÓA TÌM KIẾM NHIỀU HƠN 1, ÁP DỤNG QUY TẮC PHỂU LỌC
                    key_words = search_value.split(SEARCH_SEPERATOR)
                    spinWaiting(BREAKER)
                    print(key_words)
                    for kw in key_words:
                        search_result = searcher (kw,DATA_COMBINE_TRA_CUU,DF_COLUMN_SEARCH_NAME)
                        print (f"\tKết quả tìm kiếm cho từ khóa '{kw}'\t{search_result.shape[0]}")
                        print (search_result)#(search_expansion(kw,DU_LIEU_VTTB,DU_LIEU_VTTB_TRA_CUU))
                        print(BREAKER)
                    log_user_action(f"SEARCH\t{key_words}")                                 
                
                logging.debug('User lookup DONE')
                search_value = input(promp_search_value)   
        
        #----------------------------------------------------# Chỉnh sửa bộ sưu tập của bạn
        elif ASK_MENU == "1.4.1":
            pass
        #----------------------------------------------------# Xuất dữ liệu bộ sưu tập của bạn (.txt, .xls, .csv, .json)
        elif ASK_MENU == "1.4.2":
            pass
            
        #----------------------------------------------------# YÊU CẦU VẬT TƯ
        elif ASK_MENU == "3.0.0":
            time_request = time.strftime("%y%m%d %H%M%S",time.localtime(time.time()))
            # request_material(dir_root,subfolder_template,template_PYC_name,template_PNX_name)
            log_user_action(f"REQUEST_SUPPLY\tSoPhieuYeuCauVatTu\t{time_request}")
        
        
        #----------------------------------------------------#  QUẢN LÍ DỮ LIỆU CƠ SỞ
        elif ASK_MENU == "7":
            pass
        elif ASK_MENU == "7.1":
            #----------------------------------------------------#  XEM DỮ LIỆU
            spin_three_dots(f"\tLoading")
            show_heading_3('Dữ liệu [Danh mục] Vật tư thiết bị')
            print(DATA_VTTB)
            spin_three_dots(f"\tLoading")
            show_heading_3('Dữ liệu Vật tư thiết bị [Tồn kho]')
            print(DATA_TON_KHO)
            spin_three_dots(f"\tLoading")
            show_heading_3('Dữ liệu Vật tư thiết bị [Tổng hợp]')
            print(DATA_COMBINE)
        
        elif ASK_MENU == "7.2":
            #----------------------------------------------------# BIÊN TẬP DỮ LIỆU
            print(BREAKER)
            show_heading_1('trình biên tập dữ liệu vttb\n[dANH MỤC] - [TỒN KHO] - [TỔNG HỢP]')           
            
            #---------------------------------------------------#   DATA SELECTING
            path_data = ask_data(MENU_DATA_SELECTOR)
            
            #---------------------------------------------------# BIÊN TẬP DỮ LIỆU [DANH MỤC] VTTB
            ask_skip = input(f'\t Bạn sắp biên tập Dữ liệu [Danh mục] VTTB, bỏ qua chọn n (y/n):{USER_INPUT_PREFIX} ')
            if ask_skip.lower() == 'y':
                spin_three_dots('Backup data ')              
                data_archive(PATH_DATA_VTTB)
                spinWaiting(BREAKER)             
                DATA_VTTB = data_builder(PATH_ROOT_DIR,path_data = path_data)
                spin_three_dots('Backup data ')   
                data_archive(PATH_DATA_VTTB_TRA_CUU)                
                spinWaiting(BREAKER)           
                show_heading_3('trình cập nhật dữ liệu [tra cứu] vttb')     
                DATA_VTTB_TRA_CUU = data_lookup_builder(DATA_VTTB,PATH_DATA_VTTB_TRA_CUU,DF_COLUMN_SEARCH_NAME)
            print(BREAKER)
            #---------------------------------------------------# BIÊN TẬP DỮ LIỆU VTTB [TỒN KHO]
            print(BREAKER)
            ask_skip = input(f'\tBạn sắp biên tập Dữ liệu VTTB [Tồn kho], bỏ qua chọn n (y/n):{USER_INPUT_PREFIX} ')
            if ask_skip.lower() == 'y':
                spin_three_dots('Backup data ')
                spinWaiting(BREAKER)
                data_archive(PATH_DATA_TON_KHO)
                spinWaiting(BREAKER)             
                DATA_TON_KHO = data_builder(PATH_ROOT_DIR,SUB_DATA_VTTB,DATA_NAME_TON_KHO,menu_sub_update_by_excel,header = 'biên tập dữ liệu vttb [tồn kho]')
                print(BREAKER)
            #---------------------------------------------------# BIÊN TẬP DỮ LIỆU VTTB [TỔNG HỢP]
            print(BREAKER)
            ask_skip = input(f'\tBạn sắp biên tập Dữ liệu VTTB [TỔNG HỢP], bỏ qua chọn n (y/n):{USER_INPUT_PREFIX} ')
            if ask_skip.lower() == 'y':
                spin_three_dots('Backup data ')
                spinWaiting(BREAKER)
                data_archive(PATH_DATA_COMBINE)
                spinWaiting(BREAKER)        
                DATA_COMBINE = data_builder(PATH_ROOT_DIR,SUB_DATA_VTTB,DATA_NAME_COMBINE,menu_sub_update_by_excel,header = 'biên tập dữ liệu vttb [tổng hợp]')
                print(BREAKER)
                spin_three_dots('Backup data ')   
                data_archive(PATH_DATA_COMBINE_TRA_CUU)                
                spinWaiting(BREAKER)           
                show_heading_3('trình cập nhật dữ liệu [Tổng Hợp] [Tra Cứu] vttb')     
                DATA_COMBINE_TRA_CUU = data_lookup_builder(DATA_COMBINE,PATH_DATA_COMBINE_TRA_CUU,DF_COLUMN_SEARCH_NAME)
        #----------------------------------------------------#  
        elif ASK_MENU == "7.3":
            show_heading_1('Cập nhật Dữ liệu VTTB [Tổng hợp]')
            pass
        #----------------------------------------------------#  
        elif ASK_MENU == "8" or ASK_MENU == "8.1" :
            # tra cứu Kế hoach VTTB
            main_lookup_plan(PATH_ROOT_DIR)

        #----------------------------------------------------# KHỞI ĐỘNG LẠI CHƯƠNG TRÌNH
        elif ASK_MENU == "zz":
            time_restart = time.strftime("%y%m%d %H%M%S",time.localtime(time.time()))
            log_user_action(f"RESTART_PROGRAM\t{time_restart}")
            spin_three_dots(f"\tChương trình đang khởi động lại")
            # Restart Program
            start_program()
            continue

        elif ASK_MENU == "mn":
            ASK_MENU = input(PROMP_MENU).lower()
            continue        
        else:
            logging.warning(f'Wrong menu index')
            print(f"\tBạn chưa chọn số hiệu Menu, vui lòng chọn, để Chương trỉnh có thể phục vụ bạn !!!")        
        
        #----------------------------------------------------#  ĐIỀU HƯỚNG LỆNH
        spinWaiting(BREAKER)
        ask_next_action = input(PROMP_NEXT_ACTION).lower()
        spinWaiting(BREAKER)
        if ask_next_action == "mn": # NẾU MUỐN HIỆN LẠI MENU TỔNG
            ASK_MENU = input(PROMP_MENU).lower()
        else:
            ASK_MENU = ask_next_action.lower()
    
    TIME_END = time.strftime("%y%m%d %H%M%S",time.localtime(time.time()))
    print(f"\tBạn đang thoát chương trình vào lúc {TIME_END}")
    log_user_action(f"TIME_QUIT\t{TIME_END}")
    spinWaiting(BREAKER)
    logging.info('Program END')
    quit()
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#START PROGRAM
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        TIME_END = time.strftime("%y%m%d %H%M%S",time.localtime(time.time()))
        print(f"---Bạn đang thoát chương trình vào lúc {TIME_END}")
        if os.path.exists (PATH_USER_LOG):
            log_user_action(f"TIME_QUIT\t{TIME_END}")
        spinWaiting(BREAKER)
        logging.info('Program END')
        quit()

# test()


   
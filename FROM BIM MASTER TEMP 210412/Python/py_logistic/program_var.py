# -*- coding: utf-8 -*-
"""PROGRAM_USER_DATA_FOLDER : phụ trách chứa các dữ liệu:
-path_root: tương đường CDE - COMMON 
-lịch sử truy cập của người dùng:
    -user name:
    -password:
    -role
-File download (excel, txt được export)
-----
Không chứa các DỮ LIỆU CƠ SỞ (DM VTTB, VTTB Tồn, KH) của chương trình"""

import re


# GLOBAL PROGRAM VARIABLES
# TODO: TẠO FILE CONFIGURE.JSON , SAU ĐÓ LOAD VÀO KHAI BÁO CAC CÁC BIẾN GLOBAL


PATH_HOME = '' #os.path.expanduser('~')
USER_NAME = '' #os.getlogin()
PROGRAM_USER_DATA_FOLDER = 'cofico_logistic_data' # TODO: FOLDER NÀY NÊN THIẾT LẬP HIDDEN
PROGRAM_USER_DATA_SUBFOLDER_PATH = ''
#-------
#--------------------------------------------------#
# GLOBAL VARIABLE
#--------------------------------------------------#
PATH_ROOT_DIR = ''
PATH_ROOT_DIR_EXIST = False
USER_NAME = ''
USER_PASSWORD = ''
TIME_START = ''
TIME_END = ''
USER_DATA = None
PATH_USER_LOG = ''
# menu
ASK_MENU = ''

# path dữ liệu Excel
DATA_VTTB_TRA_CUU = None
DATA_VTTB = None

#--------------------------------------------------# SUB FOLDER
SUBFOLDER_DATA_USER = "data_user"
SUBFOLDER_TEMPLATE = "template"
SUBFOLDER_REQUEST = "data_yeu_cau_VTTB"

SUB_DATA_VTTB = "data_vat_tu"
SUB_FOLDER_CONFIG = "configures"


#--------------------------------------------------#
# CONFIGURER
#--------------------------------------------------#
NAME_DATA_EDITOR_MAIN = 'menu_data_main'
NAME_DATA_SELECTOR = 'menu_data_selector'
NAME_DATA_BUILDER = 'menu_data_builder'
#-----------------------------------------------------# Main menu
PATH_CONFIG_DATA_EDITOR_MAIN = f"{PATH_ROOT_DIR}\\{SUB_FOLDER_CONFIG}\\{NAME_DATA_EDITOR_MAIN}.txt"
#-----------------------------------------------------# Menu Data SELECTOR
PATH_CONFIG_DATA_SELECTOR =  f"{PATH_ROOT_DIR}\\{SUB_FOLDER_CONFIG}\\{NAME_DATA_SELECTOR}.txt"
#-----------------------------------------------------# Data Builder
PATH_CONFIG_DATA_BUILDER =  f"{PATH_ROOT_DIR}\\{SUB_FOLDER_CONFIG}\\{NAME_DATA_BUILDER}.txt"

MENU_DATA_EDITOR_MAIN = None
MENU_DATA_SELECTOR = None
MENU_DATA_BUILDER = None

def update_config():
    """"""
    global PATH_CONFIG_DATA_EDITOR_MAIN,PATH_CONFIG_DATA_SELECTOR,PATH_CONFIG_DATA_BUILDER
    """"""
    
    PATH_CONFIG_DATA_EDITOR_MAIN = f"{PATH_ROOT_DIR}\\{SUB_FOLDER_CONFIG}\\{NAME_DATA_EDITOR_MAIN}.txt"
    PATH_CONFIG_DATA_SELECTOR =  f"{PATH_ROOT_DIR}\\{SUB_FOLDER_CONFIG}\\{NAME_DATA_SELECTOR}.txt"
    PATH_CONFIG_DATA_BUILDER =  f"{PATH_ROOT_DIR}\\{SUB_FOLDER_CONFIG}\\{NAME_DATA_BUILDER}.txt"
#-------------------------------------------------------------------------------# 
#-------------------------------------------------------------------------------# 
#-------------------------------------------------------------------------------# 
#-------------------------------------------------------------------------------# 
#-------------------------------------------------------------------------------# 



#-------------------------------------------------------------------------------# 
#-------------------------------------------------------------------------------# 
#-------------------------------------------------------------------------------# 
#-------------------------------------------------------------------------------# 
#-------------------------------------------------------------------------------# 
#-------------------------------------------------------------------------------# 


#--------------------------------------------------# DATA DANH MỤC VTTB
PATH_EXCEL_DM_VTTB=''                   # Path Source Excel
DATA_NAME = "data"                      # Data
PATH_DATA_VTTB = ''                     # Path data
PATH_DATA_DM_VTTB_EXIST =False
DATA_VTTB_COLUMN_HEADS = []   

#--------------------------------------------------# DATA DANH MỤC VTTB TRA CỨU
DATA_SEARCH_NAME = "data_search"
PATH_DATA_VTTB_TRA_CUU = ''
PATH_DATA_VTTB_SEARCH_EXIST = False

#--------------------------------------------------# DATA DANH MỤC VTTB TỒN KHO
PATH_DATA_TON_KHO = ''
DATA_TON_KHO = None
DATA_NAME_TON_KHO = 'tonkho'
PATH_DATA_VTTB_TON_KHO_EXIST = False

#--------------------------------------------------# DATA DANH MỤC VTTB TỔNG HỢP
DATA_NAME_COMBINE = "data_combine"
DATA_COMBINE = None
PATH_DATA_COMBINE = ''
PATH_DATA_VTTB_COMBINE_EXIST = False
#--------------------------------------------------# DATA DANH MỤC VTTB TỔNG HỢP TRA CỨU
DATA_NAME_COMBINE_TRA_CUU = "data_combine_search"
DATA_COMBINE_TRA_CUU = None
PATH_DATA_COMBINE_TRA_CUU = ''
PATH_DATA_VTTB_COMBINE_TRA_CUU_EXIST = False
#--------------------------------------------------# Search utilities
DATA_LIST = [DATA_VTTB,DATA_VTTB_TRA_CUU ,DATA_TON_KHO , DATA_COMBINE , DATA_COMBINE_TRA_CUU]
DATA_PATH_LIST = [PATH_DATA_VTTB,PATH_DATA_VTTB_TRA_CUU, PATH_DATA_TON_KHO, PATH_DATA_COMBINE,PATH_DATA_COMBINE_TRA_CUU]
DATA_PATH_EXIST_LIST = [PATH_DATA_DM_VTTB_EXIST,PATH_DATA_VTTB_SEARCH_EXIST,PATH_DATA_VTTB_TON_KHO_EXIST,PATH_DATA_VTTB_COMBINE_EXIST,PATH_DATA_VTTB_COMBINE_TRA_CUU_EXIST]
#--------------------------------------------------# Search utilities
SEARCH_SEPERATOR = ","
DF_COLUMN_SEARCH_NAME = 'search_string'

#--------------------------------------------------# template name
TEMPLATE_ORDER_NAME = "template_PYC.html"
TEMPLATE_IMPORT_EXPORT_NAME = "template_PNX.html"

#--------------------------------------------------# HOTKEY

HOTKEY_ESCAPE = 'Q_ : Thoát Trình xử lí'
HOTKEY_QUIT = 'QQ : Thoát / Dừng / Tắt chương trình'
HOTKEY_RESTART = 'ZZ : Khởi động chương trình'
HOTKEY_REDO = 'Z_ : Quay lại/ Thực hiện lại tiến trình'

HOTKEYS_GENERAL = [HOTKEY_ESCAPE,HOTKEY_REDO,HOTKEY_RESTART,HOTKEY_QUIT]

#--------------------------------------------------# PROMP
START_END_LINE = '-'*5 # START FOR LINE
BREAKER = '-'*80 # BREAK LINE
USER_INPUT_PREFIX = '>>>> : '

BREAKER_SEC = '- '*25 # SECTION BREAK

# DataFrame
NA_REPLACE = 'NA'

PROMP_SAY_HI = """\t\tHi / Chào ** {0} **  !!"""
PROMP_WELCOME = """
\t\tChào mừng ** {0} ** đến với 
\t\tCHƯƠNG TRÌNH 
\t\tE-LOGISTIC PHIÊN BẢN COMMAND LINE
\t\tVersion 1.0
"""

PROMP_NEXT_ACTION = f"""{BREAKER}
[ M E N U ]
\tChọn số hiệu Menu:
\t\tMN --> hiện Menu chương trình
\t\tNhập >>>:  """

PROMP_MAIN_MENU = f"""1 [Tra cứu] Vật tư thiết bị - VTTB
1.0 Tra cứu [Danh mục] VTTB - Theo từ khóa + [Xuất dữ liệu](.txt, .xls, .csv, .json)
1.0.0 [Xuất dữ liệu] Toàn bộ [Danh mục] VTTB (.txt, .xls, .csv, .json)
1.0.1 Tra cứu [Chi tiết] [Danh mục] VTTB - Theo [Mã số chủng loại]
1.0.2 Tra cứu [Chi tiết] [Danh mục] VTTB - Theo Chỉ số [Hàng]
1.0.3 Tra cứu [Chi tiết] [Danh mục] VTTB - Theo Chỉ số [Hàng] + [Tên cột]
1.1 Tra cứu VTTB [Tồn kho]
1.1.0 [Xuất dữ liệu] VTTB [Tồn kho] (.txt, .xls, .csv, .json)
1.1.1 [Tra cứu] VTTB [Tồn kho]
1.1.2 [Tra cứu] VTTB [Tồn kho] - Theo [Mã số chủng loại]
1.1.3 [Tra cứu] VTTB [Tồn kho] - Theo [Nội dung]
1.2 Tra cứu [KẾ HOẠCH] VTTB
1.2.0 [Xuất dữ liệu] [Kế hoạch] VTTB (.txt, .xls, .csv, .json)
1.2.1 [Tra cứu] [Kế hoạch] VTTB
1.2.2 [Tra cứu] [Kế hoạch] VTTB - Theo [Mã số chủng loại]
1.2.3 [Tra cứu] [Kế hoạch] VTTB - Theo [Nội dung]
1.3 [Sưu tập] Mã VTTB
1.3.1 [Xuất dữ liệu] Bộ sưu tập (.txt, .xls, .csv, .json)
1.4 Tra cứu [Danh mục] VTTB [TỔNG HỢP]
2 [Catalog] Chi tiết VTTB
2.1 Xem [Catalog] Chi tiết VTTB - Theo Chỉ số [Hàng]
2.2 Xem [Catalog] Chi tiết VTTB - Theo Chỉ số [Hàng] + [Tên cột]
2.4 Xuất [Catalog] VTTB (.html /.pdf)
3 [Lập Phiếu/ Kế hoạch vận tải] VTTB
3.0 Lập [Kế hoạch vận tải] VTTB
3.1 Lập [Phiếu Yêu cầu] VTTB
3.2 Lập [Phiếu Xuất] VTTB
3.3 Lập [Phiếu Nhập] VTTB
3.4 Lập [Phiếu Vận tải] VTTB
3.5 Lập [Phiếu Giao nhận] VTTB
3.6 Lập [Hóa đơn /Biên lai]
4 [Xét duyệt] Phiếu VTTB
4.0 Duyệt [Kế hoạch vận tải] VTTB
4.1 Duyệt [Phiếu Yêu cầu] VTTB
4.2 Duyệt [Phiếu Xuất] VTTB
4.3 Duyệt [Phiếu Nhập] VTTB
4.4 Duyệt [Phiếu Vận tải] VTTB
4.5 Duyệt [Phiếu Giao nhận] VTTB
5 Quản lí [Hồ sơ] Logistic VTTB
5.1 Quản lí [Kế hoạch] VTTB + Vật tải
5.2 Quản lí [Phiếu] yêu cầu / Xuất / Nhập / Vận tải + [Hóa đơn /Biên lai]
7 Quản lí [Dữ liệu] VTTB
7.1 [Xem] toàn bộ [Dữ liệu VTTB]: [Danh mục] + [Tra cứu] VTTB + [Tồn kho]
7.2 [Biên tập / Cập nhật] dữ liệu VTTB: [Danh mục] + [Tra cứu] + [Tồn kho]
7.3 Cập nhật Dữ liệu VTTB [Tổng hợp] = Hợp nhất [Danh mục] + [Tồn kho]
7.4 Lựa chọn TOP các VTTB có thể đáp ứng Logistic
8 [Xử lí/ Phân tích] dữ liệu:
8.1 [Xử lí] dữ liệu [Kế hoạch] VTTB
8.2 [Phân tích] / Báo cáo dữ liệu
8.3 Quản lí [Top/Trench VTTB] có thể đáp ứng Logistic
QQ [Thoát] chương trình
MN Trở lại [Menu chính]
ZZ [Khởi động] lại Chương trình"""

PROMP_MENU_SUB = f"""
Tra cứu DANH MỤC VTTB
Tra cứu VTTB TỒN KHO
Tra cứu KẾ HOẠCH VTTB
Xem Chi tiết thông tin VTTB theo Mã số chủng loại
Xem Chi tiết VTTB - Theo Chỉ mục Hàng (row index)
Xem Chi tiết VTTB - Theo Chỉ mục Hàng (row index) và Tên cột (column name)"""

PROMP_MENU = f"""{BREAKER}
                                                Menu Chương Trình
{BREAKER}
            1.  Tra cứu Vật tư thiết bị - VTTB   
                \tTra cứu               
                1.0 Tra cứu DANH MỤC VTTB
                1.1 Tra cứu VTTB TỒN KHO
                1.2 Tra cứu KẾ HOẠCH VTTB
                \tXem Chi tiết VTTB
                1.3 Xem Chi tiết thông tin VTTB theo Mã số chủng loại
                1.3.1 Xem Chi tiết VTTB - Theo Chỉ mục Hàng (row index)
                1.3.2 Xem Chi tiết VTTB - Theo Chỉ mục Hàng (row index) và Tên cột (column name)                
                \tCá nhân hóa dữ liệu VTTB Tra cứu
                1.4 Lưu Mã vật tư vào Bộ sưu tập    
                1.4.1 Chỉnh sửa bộ sưu tập của bạn
                1.4.2 Xuất dữ liệu bộ sưu tập của bạn (.txt, .xls, .csv, .json)                
            2.  Catalog chi tiết VTTB
                2.1 Xem Catalog Chi tiết VTTB - Theo Chỉ mục Hàng (row index)
                2.2 Xem Catalog Chi tiết VTTB - Theo Chỉ mục Hàng (row index) và Tên cột (column name)
                2.3 Đề nghị sửa thông tin VTTB
                2.4 Xuất dữ liệu chi tiết VTTB (.txt, .xls, .csv, .json) 
            3.  Lập Phiếu :
                3.1 Lập phiếu Yêu cầu VTTB
                3.2 Lập Phiếu Xuất VTTB
                3.3 Lập Phiếu Nhập VTTB
                3.4 Lập Phiếu Vận tải VTTB
                3.5 Lập phiếu Giao nhận VTTB
            4. Xét duyệt
                4.1 Duyệt phiếu Yêu cầu VTTB
                4.2 Duyệt Phiếu Xuất VTTB
                4.3 Duyệt Phiếu Nhập VTTB
                4.4 Duyệt Phiếu Vận tải VTTB
                4.5 Duyệt phiếu Giao nhận VTTB
            5.  Quản lí Hồ sơ Logistic
                5.1 Biên lai / Biên bản giao nhận
                5.2 Phiếu yêu cầu
            6. Tra cứu thông tin VTTB tồn kho                                   
                6.1 Tra cứu VTTB tồn kho theo Mã Loại
                6.2 Tra cứu VTTB tồn kho bằng Tìm kiếm nội dung
            7. Quản lí Dữ liệu (xe dữ liệu VTTB hiện tại)     
                7.1 Xem dữ liệu [Danh mục] VTTB + [Tra cứu] VTTB + [Tồn kho]
                7.2 Biên tập / Cập nhật dữ liệu [Danh mục] VTTB + [Tra cứu] VTTB + [Tồn kho]
                7.3 Cập nhật Dữ liệu VTTB [Tổng hợp] = Hợp nhất [Danh mục] + [Tồn kho]
                7.4 Lựa chọn TOP các VTTB có thể đáp ứng Logistic
            8. Xử lí dữ liệu:
                8.1 Xử lí dữ liệu Kế hoạch VTTB
                8.2 NA            
            QQ. Thoát chương trình
            MN. Trở lại menu chính
            ZZ. Khởi động lại Chương trình
{BREAKER}
\tChọn Số hiệu menu
\t\tNhập >>>:  """

PROMP_DATA_EDIT = f"""Bạn có muốn biên tập Cơ sở dữ liệu Logistic (y/n) Mã menu = 10.2
\t\tNhập >>>:  """

promp_not_confirm_data = "Bạn đã CHƯA XÁC NHẬN dữ liệu, tiến trình Biên tập dữ liệu sẽ hiện lại ... "

promp_update_data_search = f"\tBạn có muốn Cập nhật Dữ liệu tra cứu ?\t(Được căn cứ trên Dữ liệu VTTB mới nhất)\n\tNhập(y/n):\t"

promp_search_value = f"""{BREAKER}
[ T R Ì N H    T R A    C Ứ U ]
\tChọn từ khóa tìm kiếm 
\tTrường hợp nhiều cụm từ: dùng dấu , ngăn cách
\t\tVd: CAY CHONG     hoặc Vd: CAY CHONG, CUM TUYP
\t\tNhập Q_ để thoát trình Tra cứu
\t\tNhập >>>: """

#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    """"""


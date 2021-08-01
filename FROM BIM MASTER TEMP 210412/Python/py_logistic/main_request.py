# -*- coding: utf-8 -*-
"""Sub program : Lập phiếu Yêu cầu / Nhập / Xuất vật tải - Vật tư thiết bị"""
#-----------------------------------------------------------------------------------------------------------------------------------------#

import json
import webbrowser, time
from time import time
import pandas as pd # pip install lxml ---> read_html
from handle_html import *
import datetime
from datetime import datetime,timedelta
from handle_string import *
from handle_cmd import *
from program_var import *
from handle_search import *
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
# OLD VERSION
def request_material(path_root,subfolder_template,template_PYC_name,template_PNX_name):
    template_PYC_path = ""
    template_PNX_path = ""
    #----------------------------------------------#
    # TẢI + SIMULATE MẪU PHIẾU YÊU CẦU / NHẬP / XUẤT
    #----------------------------------------------#
    try:
        template_PYC_path = path_root + "\\"+subfolder_template+"\\"+template_PYC_name
        template_PNX_path = path_root + "\\"+subfolder_template+"\\"+template_PNX_name
        print(BREAKER)
        print(f"""\tTemplate Phiếu đã mở bằng[ WEB Browser]---\nVui lòng xem qua \n\tMẫu: \n\t\t[Phiếu yêu cầu]:\t\t\t{template_PYC_path}\n\t\t[Phiếu nhập xuất]:\t\t\t{template_PNX_path}""")
        webbrowser.open(template_PYC_path,new=2)
        webbrowser.open(template_PNX_path,new=2)
    except Exception as ex:
        print(ex)
        pass
    
    #----------------------------------------------#
    # TẢI TEMPLATE THÔNG TIN - YÊU CẦU VẬT TƯ
    #----------------------------------------------#
    dict_path = template_PYC_path = path_root + "\\"+subfolder_template+"\\"+"pyc_dict_template.json"
    template_dict = None
    with open(dict_path,'r') as f:
        template_dict = json.loads(f.read())


    subfolder = "data_yeu_cau_VTTB"
    user_name = "Duy" # tên người yêu cầu
    date_time_stamp = time.strftime("%y%m%d%H%M%S",time.localtime(time.time()))
    date_time_PYC = datetime.strptime(date_time_stamp, "%y%m%d%H%M%S").strftime('%d-%m-%Y %H:%M:%S')
    print(BREAKER)
    print ("---Trình lập phiếu khởi tạo lúc:",date_time_PYC)

    data_request_supply = template_dict.copy() # dữ liệu Yêu cầu vật tư
    # print(data_request_supply)
    for d in template_dict:
        # print (no_accent_vietnamese(d) in no_accent_vietnamese("Ngày lập phiếu"))          
        dd = no_accent_vietnamese(d)  
        if dd in no_accent_vietnamese("Ngày lập phiếu"):
            user_input = input(f"{d}:(chọn __ để tự động) ")
            if user_input == "__":
                data_request_supply[d] = date_time_PYC
            else:
                data_request_supply[d] = user_input
            
        elif dd in no_accent_vietnamese("Tên đơn vi yêu cầu/thuê"): 
            user_input = input(f"{d}:(chọn __ để tự động) ")
            if user_input == "__":
                data_request_supply[d] = user_name
            else:
                data_request_supply[d] = user_input
            
        else:
            user_input = input(f"{d}: ")
            data_request_supply[d] = user_input
        # pass

    # print(data_request_supply)
    print(BREAKER)
    html_path = f"{path_root}\\{subfolder}\\request_{user_name}_{date_time_stamp}.html"
    write_html_PYC(html_path,data_request_supply,dic_pyc_2,dic_pyc_3,dic_pyc_4,dic_pyc_5)
    webbrowser.open(html_path,new=2)
    print(BREAKER)
    pass


#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#

sub_programs = """Phiếu [Yêu cầu] cung cấp vật tư thiết bị\tPYC
Phiếu [Nhập] vật tư thiết bị\tPN
Phiếu [Xuất] vật tư thiết bị\tPX
Phiếu [Vận tải] vật tư thiết bị\tPVT
Phiếu [Giao nhận] vật tư thiết bị\tPGN"""

menu = """Xem [Mẫu thông tin] yêu cầu VTTB
Tạo Phiếu điện từ file Excel
Tạo Phiếu điện tử [Khai báo] thủ công\t[O] tùy chỉnh, không bắt buộc, [P] : bắt buộc
Tạo Bộ chứa đơn - Order Place Holder (Đính kèm Phiếu YC giấy đã soạn trước (nếu có)
Thiết lập chương trình"""

#-----------------------------------------------------------------------------------------------------------------------------------------#
dic_pyc_root = { "Ngày":"DD/MM/YYYY",
            "Số phiếu":"ABCDabcd1234@",
            "Tên đơn vi yêu cầu/thuê":"request_party",
            "Dự án":"project_number-project_name",
            "Tháp":"tower_name",
            "Hạng mục công việc":"package_name",
            "Đề nghị phòng":"department_name",
            "Mã số hàng hóa":["material_number"],
            "Tên hàng hóa":["material_name"],
            "Đơn vị tính":["unit_count"],
            "Số lượng tổng":["quantity_sum"],
            "Số lượng đã cấp":["quantity_supllied_already"],
            "Số lượng lần này":["quantity_supply_this_time"],
            "Thời gian cung cấp":["time_supply"],
            "Ghi chú":["notes"],
            "Khối/phòng cung cấp VTTB":"P.GĐ/GĐ Khối USD",
            "Khối/phòng quản lí VTTB":"GĐ Khối HSE",
            "Ban điều hành":"PM",
            "Ý kiến của phòng ban phụ trách":"abcdXYZ1234"
            }
dic_pyc_root_unidecode = {
            'Ngay': 'DD/MM/YYYY', 
            'So phieu': 'ABCDabcd1234@', 
            'Ten don vi yeu cau/thue': 'request_party', 
            'Du an': 'project_number-project_name', 
            'Thap': 'tower_name', 
            'Hang muc cong viec': 'package_name', 
            'De nghi phong': 'department_name', 
            'Ma so hang hoa': ['material_number'], 
            'Ten hang hoa': ['material_name'], 
            'Don vi tinh': ['unit_count'], 
            'So luong tong': ['quantity_sum'], 
            'So luong da cap': ['quantity_supllied_already'], 
            'So luong lan nay': ['quantity_supply_this_time'], 
            'Thoi gian cung cap': ['time_supply'], 'Ghi chu': ['notes'], 
            'Khoi/phong cung cap VTTB': 'P.GD/GD Khoi USD', 
            'Khoi/phong quan li VTTB': 'GD Khoi HSE', 
            'Ban dieu hanh': 'PM', 
            'Y kien cua phong ban phu trach': 'abcdXYZ1234'}
"""PK = 'Số phiếu'
RK = 'Hàng hóa'
"""
dic_pyc_sample = { "Ngày":"DD/MM/YYYY",
            "Số phiếu":"ABCDabcd1234@",
            "Tên đơn vi yêu cầu/thuê":"request_party",
            "Dự án":"project_number-project_name",
            "Tháp":"tower_name",
            "Hạng mục công việc":"package_name",
            "Đề nghị phòng":"department_name",
            "Hàng hóa": 'hang_hoa_number',
            "Khối/phòng cung cấp VTTB":"P.GĐ/GĐ Khối USD",
            "Khối/phòng quản lí VTTB":"GĐ Khối HSE",
            "Ban điều hành":"PM",
            "Ý kiến của phòng ban phụ trách":"abcdXYZ1234"
            }
schema = {
            'ngay' : 'Ngày' ,
            'so_phieu' : 'Số phiếu' ,
            'ten_don_vi_yeu_cau/thue' : 'Tên đơn vi yêu cầu/thuê' ,
            'du_an' : 'Dự án' ,
            'thap' : 'Tháp' ,
            'hang_muc_cong_viec' : 'Hạng mục công việc' ,
            'de_nghi_phong' : 'Đề nghị phòng' ,
            'ma_so_hang_hoa' : 'Mã số hàng hóa' ,
            'ten_hang_hoa' : 'Tên hàng hóa' ,
            'don_vi_tinh' : 'Đơn vị tính' ,
            'so_luong_tong' : 'Số lượng tổng' ,
            'so_luong_da_cap' : 'Số lượng đã cấp' ,
            'so_luong_lan_nay' : 'Số lượng lần này' ,
            'thoi_gian_cung_cap' : 'Thời gian cung cấp' ,
            'ghi_chu' : 'Ghi chú' ,
            'khoi/phong_cung_cap_vttb' : 'Khối/phòng cung cấp VTTB' ,
            'khoi/phong_quan_li_vttb' : 'Khối/phòng quản lí VTTB' ,
            'ban_dieu_hanh' : 'Ban điều hành' ,
            'y_kien_cua_phong_ban_phu_trach' : 'Ý kiến của phòng ban phụ trách' ,
            }
"""PK = 'Hàng hóa'"""
dic_hang_hoa = [ {"Hàng hóa": 'hang_hoa_number'},
                {"Mã số hàng hóa":'',
                "Tên hàng hóa":'', 
                "Đơn vị tính":'',
                "Số lượng tổng":'', 
                "Số lượng đã cấp":'',
                "Số lượng lần này":'',
                "Thời gian cung cấp":'',
                "Ghi chú":''},
                {"Mã số hàng hóa":'',
                "Tên hàng hóa":'', 
                "Đơn vị tính":'',
                "Số lượng tổng":'', 
                "Số lượng đã cấp":'',
                "Số lượng lần này":'',
                "Thời gian cung cấp":'',
                "Ghi chú":''}]
"""PK = 'Mã số hàng hóa'"""
dic_hang = {"Mã số hàng hóa":'',
            "Tên hàng hóa":'', 
            "Đơn vị tính":'',
            "Số lượng tổng":'', 
            "Số lượng đã cấp":'',
            "Số lượng lần này":'',
            "Thời gian cung cấp":'',
            "Ghi chú":''
        }
"""PK = 'Mã số hàng hóa'"""
dic_vttb = {"Mã số hàng hóa":'',
            "Tên hàng hóa":'', 
            "Đơn vị tính":'',
            "Số lượng tồn kho":'', 
            "Số lượng đã cấp":''
        }
dict_vttb_keys = {
         'ma_so_hang_hoa' : 'Mã số hàng hóa' ,
         'ten_hang_hoa' : 'Tên hàng hóa' ,    
         'don_vi_tinh' : 'Đơn vị tính' ,      
         'so_luong_ton_kho' : 'Số lượng tồn kho' ,
         'so_luong_da_cap' : 'Số lượng đã cấp' ,
        }
#-----------------------------------------------------------------------------------------------------------------------------------------#
#Global
setting_auto = {}  
max_days_process = 7
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def write_order_data(path_order_data,data):
    """Ghi dữ liệu Đặt hàng / Yêu cầu / Nhập xuất ra dữ liệu .txt
    ### Input:
    path_order_data (str)
    data (dict)    """
    data = "\n".join([f"{d}\t{data[d]}" for d in data])
    with open(path_order_data,'w',encoding='utf-8') as f:
        f.write(data)
#-----------------------------------------------------------------------------------------------------------------------------------------#
def request_mat(path_root,user_name,dic_pyc,sub_programs,menu):
    time_order = datetime.now()#time.localtime(time.time()) 
    time_order_code = time_order.strftime('%y%m%d%H%M%S') # time.strftime('%Y%m%d%H%M%S',time_order)

    program_name = "Trình tạo lập phiếu Vật tư thiết bị:\n\tYêu cầu / Xuất / Nhập /Vận tải"
    sub_programs_number = [p.split('\t')[1] for p in sub_programs.split('\n')]
    sub_programs = [p.split('\t')[0] for p in sub_programs.split('\n')] 
    
    ask_ready = ''
    flag_ready = False
    while flag_ready == False:               # LOOP ASK
        ask_ready = show_menu_1(program_name,'\tDanh sách các trình con [Lập phiếu] : ',sub_programs,f"\tHãy chọn [số hiệu] trình con\n\t{USER_INPUT_PREFIX}")
        flag_ready = not len(ask_ready) == 0
    if ask_ready == '0':
        order_number = sub_programs_number[int(ask_ready)]
        path_order_data = f"{path_root}\\{SUBFOLDER_REQUEST}\\{order_number}-{user_name}-{time_order_code}.txt"
        title = 'PHIẾU YÊU CẦU CUNG CẤP\n\tVẬT TƯ THIẾT BỊ'   
        tip_1 = '\t[Tips] Nhập Enter để Chương trình [Tự động] xử lí cho bạn'
        
        ask_menu_ = ''
        flag_menu = False
        while flag_menu == False:               # LOOP ASK
            ask_menu_ = show_menu_1(title,'\tMenu thực hiện : ',menu.split('\n'),f"\tHãy chọn [số hiệu] menu\n\t{USER_INPUT_PREFIX}")
            flag_menu = not len(ask_ready) == 0
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        if ask_menu_ == '2':
            print_orders(f"[Mẫu] : {title}",dic_pyc)
            show_heading_4('Vui lòng [Khai báo] [nội dung] Phiếu yêu cầu: ')
            print(tip_1)
            print(BREAKER)            
            for d in dic_pyc:
                prime_key = 'Mã số hàng hóa'
                # -----------------------------------------------------------#  TRIG process KEY
                if d == prime_key:              
                    break
                value = input(f"\t{'{:<35}'.format(d)}{'{:>0}'.format(':')}\t")                
                # -----------------------------------------------------------# TRIG AUTO FILL 
                if value == '':                
                    value = input_auto(path_root,time_order,path_order_data,d,auto_list,order_number)
                    print (f"\t{'{:<35}'.format(' '*len(d))}{'{:>0}'.format('-->')}\t{value}")
                if not value:
                    value = START_END_LINE
                dic_pyc[d] = value
                write_order_data(path_order_data,dic_pyc)          
            print_orders(f"[Kết quả khai báo] : {title}",dic_pyc)       
            
            ask_action = ''
            flag_action = False
            while flag_action == False:         # ------------#  LOOP ASK            
                ask_action = show_menu_2(f"Bạn muốn","Xuất Excel đơn\nSửa lại đơn\nThoát + Hủy đơn",USER_INPUT_PREFIX)
                flag_action = not len(ask_action) == 0

            if ask_action == '0':               # ------------#  XUẤT EXCEL
                pass            
            elif ask_action == '1':             # ------------# SỬA ĐƠN YC
                flag_edit = True
                while flag_edit:
                    for d in dic_pyc:
                        value = input(f"{'{:>40}'.format(d)} : {dic_pyc[d]} {USER_INPUT_PREFIX} [Edit to]: ")
                        if value == '':
                            # AUTO FILL TRIGGING
                            value = input_auto(path_root,time_order,path_order_data,d,auto_list,order_number)
                            print (f"\t{'{:<35}'.format(' '*len(d))}{'{:>0}'.format('-->')}\t{value}")
                        if not value:
                            value = START_END_LINE
                        dic_pyc[d] = value
                        write_order_data(path_order_data,dic_pyc)
                    ask_done = input(f"\t Bạn muốn Kết thúc Sửa đơn (y/n) {USER_INPUT_PREFIX}").lower()
                    flag_edit = False if ask_done == 'y' else True
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#
        #-------------------------------------------------------------------------#

        elif ask_menu_ == '3':
            print  ('\t[!] Đang trong giai đoạn triển khai')
            pass
    pass
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#

def setup_auto_input():
    """Thiết lập các setting auto input"""
    global setting_auto ,dic_pyc_root
    setting_auto = dic_pyc_root.copy()

#-----------------------------------------------------------------------------------------------------------------------------------------#
auto_list = [ "Ngày",
            "Số phiếu",
            "Hạng mục công việc",
            "Đề nghị phòng",
            "Mã số hàng hóa",
            "Tên hàng hóa",
            "Đơn vị tính",
            "Số lượng tổng",
            "Số lượng đã cấp",
            "Thời gian cung cấp",
            "Khối/phòng cung cấp VTTB",
            "Khối/phòng quản lí VTTB"]
def input_auto(path_root,time_order,path_order_data,keyname, auto_list, order_number) -> any:
    """Tự động xử lí nội dung nếu thỏa điều kiện Key name nằm trong Danh sách Auto
    Trả về Hàm xử lí"""    
    time_order_show = time_order.strftime('%d/%m/%Y') # time.strftime('%d/%m/%Y',time_order)
    time_order_code = time_order.strftime('%y%m%d%H%M%S') # time.strftime('%Y%m%d%H%M%S',time_order)

    lookup_array_path = f"{path_root}\\{SUB_DATA_VTTB}\\{DATA_SEARCH_NAME}.json"
    data_search = pd.read_json(lookup_array_path,orient='records',dtype='string')
    
    if keyname in auto_list and keyname == 'Ngày':            
        return time_order_show    
    
    numbers = None
    flag_data_exist = os.path.exists(path_order_data)

    if flag_data_exist:
        with open(path_order_data,'r',encoding='utf-8') as f:
            numbers = [n.strip().split('\t')[1] for n in f.readlines() if n.split('\t')[0] == "Mã số hàng hóa"][0]   
        
            if keyname == 'Số phiếu':
                """Auto theo Mã loại phiếu + Mã dự án + Mã thời gian độc nhất"""
                return f'{order_number}_{time_order_code}'
            if keyname == 'Hạng mục công việc':
                """Tra cứu thành phần Vật tư Đặt hàng lần này"""
            if keyname == 'Đề nghị phòng':
                """Mặc định P USD"""
                return 'Phòng USD'
            if keyname == "Mã số hàng hóa":
                """"""
                if numbers:
                    return numbers
            if keyname == 'Tên hàng hóa':
                """Tra cứu VTTB-Tên thiết bị"""
                # Đảm bảo không có dấu phẩy trong kết quả
                names = ','.join([str(r).replace(",","") for r in search_number(numbers,data_search,DF_COLUMN_SEARCH_NAME)['TenThietBi'].tolist()]) # MaThietBi,TenLoaiThietBi,TenThietBi,DonVi,KhoiLuong,TheTich,GiaThueNoiBo/Ngay
                return names
            if keyname == 'Đơn vị tính':
                """Tra cứu VTTB -Đơn vị tính"""
                unit_cal = ','.join(search_number(numbers,data_search,DF_COLUMN_SEARCH_NAME)['DonVi'].tolist()) # MaThietBi,TenLoaiThietBi,TenThietBi,DonVi,KhoiLuong,TheTich,GiaThueNoiBo/Ngay
                return unit_cal
            if keyname == 'Số lượng tổng':
                """Tra cứu Kế hoach VTTB"""
            if keyname == 'Số lượng đã cấp':
                """Tra cứu Lịch sử cấp hàng cho"""
            if keyname == 'Thời gian cung cấp':
                """Theo quy định thủ tục tối đa sau 7 ngày kể cả ngày nghỉ"""
                time_received = time_order + timedelta(days = max_days_process)
                return time_received.strftime('%d/%m/%Y')
            if keyname == 'Khối/phòng cung cấp VTTB':
                """Mặc định là P USD"""
                return 'Phòng USD'
            if keyname == 'Khối/phòng quản lí VTTB':
                """Mặc định là P An Toàn"""
                return 'Phòng An Toàn'
    


#-----------------------------------------------------------------------------------------------------------------------------------------#

def print_orders(title,dic_pyc):
    """In ra kết quả các Phiếu đã lập"""
    print(BREAKER)
    print(f"\t\t{title}")
    print(BREAKER)
    print('{:>40}'.format(START_END_LINE),'{:<40}'.format(START_END_LINE))
    [print(f"{'{:>40}'.format(v)} : {dic_pyc[v]}") for _,v in enumerate(dic_pyc)]   
    print('{:>40}'.format(START_END_LINE),'{:<40}'.format(START_END_LINE))
    print(BREAKER)
#-----------------------------------------------------------------------------------------------------------------------------------------#
def print_dict_keys_pair(dic):
    print('{')
    [print('\t',f"'{'_'.join(unidecode.unidecode(d).lower().split())}'",':',f"'{d}'",',') for d in dic]
    print('}')
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
# Run
if __name__ == '__main__':
    try:
        path_root = r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\py_logistic"#input  (f'\nNhập path:{user_input_prefix}')
        username = 'TVPDUY'
        # subfolder_template = "template"
        # template_PYC_name = "template_PYC.html"
        # template_PNX_name = "template_PNX.html"
        # request_material(path_root,subfolder_template,template_PYC_name,template_PNX_name)
        # print_orders('PHIẾU YÊU CẦU CUNG CẤP VẬT TƯ THIẾT BỊ',dic_pyc)
        
        # request_mat(path_root,username, dic_pyc_root, sub_programs, menu)

        # print('123abc',end='\r')
        # time.sleep(1)
        # print('456abc')
        # print('789abc')
        # now = datetime.now()
        # print(now.strftime('%y%m%d%H%M%S'))

        # print(unidecode.unidecode(str(dic_pyc_root)))
        print_dict_keys_pair(dic_vttb)
        

    except KeyboardInterrupt:
        quit()

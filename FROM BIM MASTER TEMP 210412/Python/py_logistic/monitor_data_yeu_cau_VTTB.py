



#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#

import os, time,json
import pandas as pd

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
def main(path_root,folder_data,sleep):    
    path_listen_to = f"{path_root}\\{folder_data}"
    print(f"\t---Data YC VTTB - Listener to {path_listen_to} ...initiating...")
    list_dir = os.listdir(path_listen_to)
    ini_count = len(list_dir)    
    data_builder(path_listen_to) # GOM THÔNG TIN PHIẾU YÊU CẦU --> TẠO DỮ LIỆU SUGGEST : DON VI YEU CAU, SO PHIEU, HANG MUC, DU AN, 
    print(f"\t---Data YC VTTB - Start listening...at {time.strftime('%a %d %b %Y %H:%M:%S')} (Ctrl + C for shutdown) ")
    while True:
        try:
            time.sleep(sleep)
            current_count = monitor(path_listen_to)
            if current_count > ini_count:
                ini_count = current_count
                raise Exception('Thêm dữ liệu')
            if current_count < ini_count:
                ini_count = current_count
                raise Exception('Xóa dữ liệu')    
            print(f"\t\t---Listening...at {time.strftime('%a %d %b %Y %H:%M:%S')} (Ctrl + C for shutdown) ")
        except Exception as ex:
            if ex.args[0] == 'Thêm dữ liệu':
                print ("---",ex,'---Tiến trình Xử lí đang diễn ra ... !!!')
                data_processer(path_listen_to)
            if ex.args[0] == 'Xóa dữ liệu':
                print ("---",ex,'---Tiến trình Xử lí đang diễn ra ... !!!')
                data_processer(path_listen_to)
            pass
#-------------------------------------------------------------------------#

#-------------------------------------------------------------------------#
def monitor(path)-> int:
    """Lấy số lượng các Directory trong Path"""
    return len(os.listdir(path))
#-------------------------------------------------------------------------#

#-------------------------------------------------------------------------#
def data_processer(path_listen_to):
    # print ([d for d in os.listdir(path)])
    for d in os.listdir(path_listen_to):
        if d.split(".")[-1].lower() == "html":
            html_path = path_listen_to + "\\" + d
            data = pd.read_html(html_path)[0] # index 0 la Thong tin phieu yeu cau
            don_vi_yeu_cau_dict[data[1][2]] = ""
            so_phieu_dict[data[1][1]] = ""
    print ("\t---Ten don vi yeu cau:\n",[d for d in don_vi_yeu_cau_dict])
    print ("\t---So phieu:\n",[d for d in so_phieu_dict])
    data_updater(path_listen_to)

#-------------------------------------------------------------------------#

#-------------------------------------------------------------------------#
def data_builder(path_listen_to):
    for d in os.listdir(path_listen_to):        
        if d.split(".")[-1].lower() == "html":
            html_path = path_listen_to + "\\" + d        
            data = pd.read_html(html_path)[0] # index 0 la Thong tin phieu yeu cau
            don_vi_yeu_cau_dict[data[1][2]] = ""
            so_phieu_dict[data[1][1]] = ""
    print ("\t---Ten don vi yeu cau:\n",[d for d in don_vi_yeu_cau_dict])
    print ("\t---So phieu:\n",[d for d in so_phieu_dict])
    data_updater(path_listen_to)

#-------------------------------------------------------------------------#
#  HÀM CẬP NHẬT DỮ LIỆU
#-------------------------------------------------------------------------#
def data_updater(path_listen_to):
    don_vi_yeu_cau_list = [str(d) for d in don_vi_yeu_cau_dict]
    so_phieu_list = [str(d) for d in so_phieu_dict]
    database_yeucau_VTTB = None
    with open(dict_path,'r') as f:
        database_yeucau_VTTB = json.loads(f.read())
    database_yeucau_VTTB['Tên đơn vi yêu cầu/thuê'] = don_vi_yeu_cau_list
    database_yeucau_VTTB['Số phiếu'] = so_phieu_list
    datapath = f"{path_listen_to}\\database_yeucau.json"
    with open(datapath,'w') as ff:
        ff.write(json.dumps(database_yeucau_VTTB,indent=4,sort_keys=True))

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#

if __name__ == '__main__':  
    try:
        path_root = input ("---Path Root: ")#r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\py_logistic\data_yeu_cau_VTTB"#r"C:\Users\tvpduy\py_logistic\data_user" # ĐƯỜNG DẪN THƯ MỤC DỮ LIỆU LOGISTIC
        folder_data = "data_yeu_cau_VTTB"
        subfolder_template = "template"
        dict_path = template_PYC_path = path_root + "\\"+subfolder_template+"\\"+"pyc_dict_template.json"

        don_vi_yeu_cau_dict = {}
        so_phieu_dict = {}
        don_vi_yeu_cau_list = []
        so_phieu_list = []

        main(path_root,folder_data,5)
    except KeyboardInterrupt:
        quit()

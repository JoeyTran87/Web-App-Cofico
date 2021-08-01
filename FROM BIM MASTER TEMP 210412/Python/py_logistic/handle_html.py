import json2html
from json2html import *
import pandas as pd
import os, json
dic_pyc_1 = {"Ngày":"DD-MM-YYYY",
        "Số phiếu":"ABCDabcd1234@"}
dic_pyc_2 = {"Tên đơn vi yêu cầu/thuê":"",
    "Dự án":"project_number-project_name",
    "Tháp":"tower_name",
    "Hạng mục công việc":"package_name",
    "Đề nghị phòng":"department_name"}
dic_pyc_3 = [{"Mã số hàng hóa":"material_number",
    "Tên hàng hóa":"material_name",
    "Đơn vị tính":"unit_count",
    "Số lượng tổng":"quantity_sum",
    "Số lượng đã cấp":"quantity_supllied_already",
    "Số lượng lần này":"quantity_supply_this_time",
    "Thời gian cung cấp":"time_supply",
    "Ghi chú":"notes"},
    {"Mã số hàng hóa":"material_number",
    "Tên hàng hóa":"material_name",
    "Đơn vị tính":"unit_count",
    "Số lượng tổng":"quantity_sum",
    "Số lượng đã cấp":"quantity_supllied_already",
    "Số lượng lần này":"quantity_supply_this_time",
    "Thời gian cung cấp":"time_supply",
    "Ghi chú":"notes"},
    {"Mã số hàng hóa":"material_number",
    "Tên hàng hóa":"material_name",
    "Đơn vị tính":"unit_count",
    "Số lượng tổng":"quantity_sum",
    "Số lượng đã cấp":"quantity_supllied_already",
    "Số lượng lần này":"quantity_supply_this_time",
    "Thời gian cung cấp":"time_supply",
    "Ghi chú":"notes"},
    {"Mã số hàng hóa":"material_number",
    "Tên hàng hóa":"material_name",
    "Đơn vị tính":"unit_count",
    "Số lượng tổng":"quantity_sum",
    "Số lượng đã cấp":"quantity_supllied_already",
    "Số lượng lần này":"quantity_supply_this_time",
    "Thời gian cung cấp":"time_supply",
    "Ghi chú":"notes"}   ] 
dic_pyc_4 = [{
    "Khối/phòng cung cấp VTTB":"P.GĐ/GĐ Khối USD",
    "Khối/phòng quản lí VTTB":"GĐ Khối HSE",
    "Ban điều hành":"PM"
    }   
    ]
dic_pyc_5 = [{
    "Ý kiến của phòng ban phụ trách":"----------------"
    }   
    ] 
def main():
    dic_pyc_1 = {"Ngày":"DD-MM-YYYY",
        "Số phiếu":"ABCDabcd1234@"}

    dic_pyc_2 = {"Tên đơn vi yêu cầu/thuê":"",
        "Dự án":"project_number-project_name",
        "Tháp":"tower_name",
        "Hạng mục công việc":"package_name",
        "Đề nghị phòng":"department_name"}
    dic_pyc_3 = [{"Mã số hàng hóa":"material_number",
        "Tên hàng hóa":"material_name",
        "Đơn vị tính":"unit_count",
        "Số lượng tổng":"quantity_sum",
        "Số lượng đã cấp":"quantity_supllied_already",
        "Số lượng lần này":"quantity_supply_this_time",
        "Thời gian cung cấp":"time_supply",
        "Ghi chú":"notes"},
        {"Mã số hàng hóa":"material_number",
        "Tên hàng hóa":"material_name",
        "Đơn vị tính":"unit_count",
        "Số lượng tổng":"quantity_sum",
        "Số lượng đã cấp":"quantity_supllied_already",
        "Số lượng lần này":"quantity_supply_this_time",
        "Thời gian cung cấp":"time_supply",
        "Ghi chú":"notes"},
        {"Mã số hàng hóa":"material_number",
        "Tên hàng hóa":"material_name",
        "Đơn vị tính":"unit_count",
        "Số lượng tổng":"quantity_sum",
        "Số lượng đã cấp":"quantity_supllied_already",
        "Số lượng lần này":"quantity_supply_this_time",
        "Thời gian cung cấp":"time_supply",
        "Ghi chú":"notes"},
        {"Mã số hàng hóa":"material_number",
        "Tên hàng hóa":"material_name",
        "Đơn vị tính":"unit_count",
        "Số lượng tổng":"quantity_sum",
        "Số lượng đã cấp":"quantity_supllied_already",
        "Số lượng lần này":"quantity_supply_this_time",
        "Thời gian cung cấp":"time_supply",
        "Ghi chú":"notes"}   ] 
    dic_pyc_4 = [{
        "Khối/phòng cung cấp VTTB":"P.GĐ/GĐ Khối USD",
        "Khối/phòng quản lí VTTB":"GĐ Khối HSE",
        "Ban điều hành":"PM"
        }   
        ]
    dic_pyc_5 = [{
        "Ý kiến của phòng ban phụ trách":"----------------"
        }   
        ] 


    dic_pnx_1 = {"Ngày":"DD-MM-YYYY",
        "Số phiếu":"ABCDabcd1234@"}

    dic_pnx_2 = {"Nơi xuất":"project_number-project_name",
        "Nơi nhập":"project_number-project_name",
        "Tháp":"tower_name",
        "Loại xe vận chuyển":"vehicle_type",
        "Biển số xe":"vehicle_number"}
    dic_pnx_3 = [{"Mã số hàng hóa":"material_number",
        "Tên hàng hóa":"material_name",
        "Đơn vị tính":"unit_count",
        "Số lượng Thực xuất":"quantity_actual_exported",
        "Số lượng Thực nhận":"quantity_actual_imported",
        "Ghi chú":"notes"},
        {"Mã số hàng hóa":"material_number",
        "Tên hàng hóa":"material_name",
        "Đơn vị tính":"unit_count",
        "Số lượng Thực xuất":"quantity_actual_exported",
        "Số lượng Thực nhận":"quantity_actual_imported",
        "Ghi chú":"notes"}
        ,
        {"Mã số hàng hóa":"material_number",
        "Tên hàng hóa":"material_name",
        "Đơn vị tính":"unit_count",
        "Số lượng Thực xuất":"quantity_actual_exported",
        "Số lượng Thực nhận":"quantity_actual_imported",
        "Ghi chú":"notes"}
        ,
        {"Mã số hàng hóa":"material_number",
        "Tên hàng hóa":"material_name",
        "Đơn vị tính":"unit_count",
        "Số lượng Thực xuất":"quantity_actual_exported",
        "Số lượng Thực nhận":"quantity_actual_imported",
        "Ghi chú":"notes"}
        ] 
    dic_pnx_4 = [
        {   "Bên nhận-An ninh/An toàn":"received_safety_or_security",
            "Bên nhận-PM/SM":"received_PM_or_SM",
            "Bên nhận-Bảo vệ CT":"received_guardman",
            "Bên nhận-Thủ kho":"received_warehouse_keeper",
            "Bên vận chuyển-Tài xế":"logistic_driver",
            "Bên giao-Bảo vệ 1":"deliver_guardman_1",
            "Bên giao-Bảo vệ 2":"deliver_guardman_2",
            "Bên giao-Quản lí Kho":"deliver_warehouse_manager",
            "Bên giao-Thủ Kho":"deliver_warehouse_keeper"
            }
    ]
    dic_pnx_5 = [{
        "Ghi chú":"Tới nơi liên lạc với Mr./Ms.:...........Số Đt:...........",
        "Mô tả":"Theo PYC VTTB-123456789-xyz"
        }   
        ] 

    htmlText_pyc_1 = json2html.convert(json = dic_pyc_1,table_attributes='border="1"')
    htmlText_pyc_2 = json2html.convert(json = dic_pyc_2,table_attributes='border="1"')
    htmlText_pyc_3 = json2html.convert(json = dic_pyc_3,table_attributes='border="1"')
    htmlText_pyc_4 = json2html.convert(json = dic_pyc_4,table_attributes='border="1"')
    htmlText_pyc_5 = json2html.convert(json = dic_pyc_5,table_attributes='border="1"')
    htmlbase_pyc = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PYC CẤP VẬT TƯ</title>
    </head>
    <body>
        <h2>PHIẾU YÊU CẦU CUNG CẤP VẬT TƯ THIẾT BỊ</h2>
        {htmlText_pyc_1}
        <br>
        {htmlText_pyc_2}
        <br>
        {htmlText_pyc_3}
        <br>
        {htmlText_pyc_4}
        <br>
        {htmlText_pyc_5}
    </body>
    </html>
    """
    print(htmlbase_pyc)
    htmlText_pnx_1 = json2html.convert(json = dic_pnx_1,table_attributes='border="1"')
    htmlText_pnx_2 = json2html.convert(json = dic_pnx_2,table_attributes='border="1"')
    htmlText_pnx_3 = json2html.convert(json = dic_pnx_3,table_attributes='border="1"')
    htmlText_pnx_4 = json2html.convert(json = dic_pnx_4,table_attributes='border="1"')
    htmlText_pnx_5 = json2html.convert(json = dic_pnx_5,table_attributes='border="1"')
    htmlbase_phieu_nhap = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PHIẾU NHẬP</title>
    </head>
    <body>
        <h2>PHIẾU LUÂN CHUYỂN (NHẬP XUẤT) VẬT TƯ THIẾT BỊ</h2>
        {htmlText_pnx_1}
        <br>
        {htmlText_pnx_2}
        <br>
        {htmlText_pnx_3}
        <br>
        {htmlText_pnx_4}
        <br>
        {htmlText_pnx_5}
    </body>
    </html>
    """
    print(htmlbase_phieu_nhap)
def write_html_PYC(html_path,dic_pyc_1,dic_pyc_2,dic_pyc_3,dic_pyc_4,dic_pyc_5):
    htmlText_pyc_1 = json2html.convert(json = dic_pyc_1,table_attributes='border="1"')
    htmlText_pyc_2 = json2html.convert(json = dic_pyc_2,table_attributes='border="1"')
    htmlText_pyc_3 = json2html.convert(json = dic_pyc_3,table_attributes='border="1"')
    htmlText_pyc_4 = json2html.convert(json = dic_pyc_4,table_attributes='border="1"')
    htmlText_pyc_5 = json2html.convert(json = dic_pyc_5,table_attributes='border="1"')
    htmlbase_pyc = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PYC CẤP VẬT TƯ</title>
    </head>
    <body>
        <h2>PHIẾU YÊU CẦU CUNG CẤP VẬT TƯ THIẾT BỊ</h2>
        {htmlText_pyc_1}
        <br>
        {htmlText_pyc_2}
        <br>
        {htmlText_pyc_3}
        <br>
        {htmlText_pyc_4}
        <br>
        {htmlText_pyc_5}
    </body>
    </html>
    """
    # print(htmlbase_pyc)
    with open(html_path,'w',encoding='utf-8') as f:
        f.write(htmlbase_pyc)
    # print(htmlbase_pyc)

def readHtml (template_PYC_path):
    dfs = pd.read_html(template_PYC_path)
    print(dfs[2])
    ngay_lap_phieu = dfs[0][1][0]           # NGÀY LẬP PHIẾU
    so_phieu = dfs[0][1][1]         # SỐ PHIẾU
    
    ten_nguoi_yeu_cau = dfs[1][1][0]
    ten_du_an = dfs[1][1][1]
    ten_thap = dfs[1][1][2]
    hang_muc_cong_viec = dfs[1][1][3]
    de_nghi_phong = dfs[1][1][4]

    ma_so_hang_hoa, ten_hang_hoa, don_vi_tinh, so_luong_tong, so_luong_da_cap, so_luong_lan_nay, thoi_gian_cung_cap, ghi_chu = None
    danh_muc_yeu_cau = [ma_so_hang_hoa, ten_hang_hoa, don_vi_tinh, so_luong_tong, so_luong_da_cap, so_luong_lan_nay, thoi_gian_cung_cap, ghi_chu]
    print(danh_muc_yeu_cau)
    pass

# htmlstr = pd.DataFrame(dic_pyc_3)
# print(htmlstr)
# html_path = r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\py_logistic\data_request_supply\pd_HTML_test.html"
# with open(html_path,'w',encoding='utf-8') as f:
#     htmlstr.to_html(f)
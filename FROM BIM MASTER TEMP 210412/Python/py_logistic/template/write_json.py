import json

def main():
    dic = {
        "Ngày lập phiếu":"DD-MM-YYYY",
        "Số phiếu":"ABCDabcd1234@",
        "Tên đơn vi yêu cầu/thuê":"",
        "Dự án":"project_number-project_name",
        "Tháp":"tower_name",
        "Hạng mục công việc":"package_name",
        "Đề nghị phòng":"department_name"
    }

    dir_root = r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\py_logistic"#r'C:\Users\tvpduy\py_logistic'
    subfolder_template = "template"
    template_PYC_name = "template_PYC.html"
    template_PNX_name = "template_PNX.html"

    dict_path = template_PYC_path = dir_root + "\\"+subfolder_template+"\\"+"pyc_dict_template.json"

    with open(dict_path,'w') as f:
        f.write(json.dumps(dic))

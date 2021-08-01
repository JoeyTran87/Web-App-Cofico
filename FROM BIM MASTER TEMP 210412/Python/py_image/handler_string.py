import re
import unidecode

# text = """Hà Nội xem xét mở lại hoạt động thể thao ngoài trời
# Thành phố có thể cho phép hoạt động thể thao ngoài trời không quá 20 người và mở lại một số dịch vụ kinh doanh.
# """

#----------------------------------------------------#
# NO USE ANY MODULE
#----------------------------------------------------#
def no_accent_vietnamese(s):
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)
    return s.lower().strip().replace(" ","")
#----------------------------------------------------#
# USE unicode module
#----------------------------------------------------#
def no_accent_vietnamese_unicoder(s,upper = False):
    if upper:
        return unidecode.unidecode(s).upper()
    else:
        return unidecode.unidecode(s)

#----------------------------------------------------#
# TODO:
#----------------------------------------------------#
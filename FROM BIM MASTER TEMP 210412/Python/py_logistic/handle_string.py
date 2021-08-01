# -*- coding: utf-8 -*-
"""Module hỗ trợ XỬ LÍ STRING, CHUẨN HÓA STRING"""
import re
import unidecode
import pandas as pd
import numpy as np

#-----------------------------------------------------------------------#
# NO USE ANY MODULE

#-----------------------------------------------------------------------#
def no_accent_vietnamese(s) -> str:
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

#-----------------------------------------------------------------------#
# USE unicode module

#-----------------------------------------------------------------------#
def no_accent_vietnamese_unicoder(s,upper = False) -> str:
    if upper:
        return unidecode.unidecode(s).upper()
    else:
        return unidecode.unidecode(s)

#-----------------------------------------------------------------------#
# STANDARDIZE STRING
#-----------------------------------------------------------------------#
def clean_str(text) -> str:
    """Xử lí text --> làm sạch Text, loại bỏ khoảng trắng thừa"""
    try:
        return re.sub('\s+',' ',str(text).strip())
    except:
        return text
#-----------------------------------------------------------------------#
def clean_str_lower(text) -> str:
    """Xử lí text --> làm sạch Text, loại bỏ khoảng trắng thừa"""
    try:
        return re.sub('\s+',' ',str(text).strip()).lower()
    except:
        return text
#-----------------------------------------------------------------------#
def clean_str_upper(text) -> str:
    """Xử lí text --> làm sạch Text, loại bỏ khoảng trắng thừa"""
    try:
        return re.sub('\s+',' ',str(text).strip()).upper()
    except:
        return text
#-----------------------------------------------------------------------#
def UPPER_unidecode_str_with_space(text) -> str:
    """Xử lí text --> lower + xóa khoảng trằng thừa
        upper() default"""
    try:
        return unidecode.unidecode(re.sub('\s+',' ',str(text).strip()).upper())
    except:
        return text

#-----------------------------------------------------------------------#
def UPPER_unidecode_str_non_space(text) -> str:
    """Xử lí text --> lower + xóa TOÀN BỘ khoảng trằng
        upper() default"""
    try:
        return unidecode.unidecode(str(text).replace(" ","").upper())
    except:
        return text
#-----------------------------------------------------------------------#
def str_capital_each(text) -> str: 
    """Xử lí text --> Hoa đầu mỗi chữ"""
    if len(text) > 0:
        try:
            text = clean_str_lower(text)
            new_text = ''
            if " " in text:
                new_text = " ".join([f"{w[0].upper()+w[1:].lower()}" for w in text.split()])
            else:
                new_text = f"{text[0].upper()+text[1:].lower()}"        
            return new_text
        except:
            return text
    else:
        return text.upper()
#-----------------------------------------------------------------------#
def check_words_exists_in(text,lookup) -> bool:
    flag = False
    flag_1 = False
    flag_2 = False
    flag_1 = len(re.findall(UPPER_unidecode_str_non_space(text),UPPER_unidecode_str_non_space(lookup))) > 0 #process_str_non_space(text) in process_str_non_space(lookup)
    if  " " in text:
        flag_2= not False in [t in UPPER_unidecode_str_non_space(lookup) for t in UPPER_unidecode_str_with_space(text).split()]
    flag = flag_1 or flag_2
    return flag

#-----------------------------------------------------------------------#
def concat_df_series(df_in) -> pd.Series:
    """NHẬP CÁC CỘT DATAFRAME"""
    df = df_in.astype('string')
    first_col = df[df.columns[0]]
    concat = np.array([''] * int(first_col.shape[0]))#['']*int(first_col.shape[0])
    for c in df.columns:    
        concat = df[c].str.cat(concat)
    concat = concat.str.replace(' ', '', regex=False).str.upper()
    for c in concat.index:
        try:
            concat.loc[c] = str(unidecode.unidecode(concat.loc[c]))
        except:
            pass
    return concat
#-----------------------------------------------------------------------#
def process_input_range(text) -> any:
    """Xử lí đầu vào có chứa Khai báo Giới hạn  RANGE\nVd [range] : [5:10]"""
    text = text
    flag_has_range = len(re.findall('[\[,\],:]',text)) == 3
    if flag_has_range:
        text = text.replace(" ","")
        text = text[len(text.split('[')[0]):]
        flag_no_other_chars = len(re.findall('[A-Z]',text.upper())) == 0        
        flag_only_number = len(text) - len(re.findall('[\[,\],:]',text))==len(re.findall('[0-9]',text))
        if flag_no_other_chars and flag_only_number:
            text = text.replace('[','').replace(']','')
            r = [int(n) for n in text.split(':')]
            return list(range(r[0],r[1]+1))
    else:
        return text
#-----------------------------------------------------------------------#
def process_input_int_list(text) -> any:
    """Xử lí đầu vào có chứa Khai báo danh sách Số nguyên\nVd [list] : 1,3,7,8,9,20"""
    flag_has_range = len(re.findall('[\,]',text)) > 0
    text=text
    if flag_has_range:
        text = text.replace(" ","")
        flag_no_other_chars = len(re.findall('[A-Z]',text.upper())) == 0        
        flag_only_number = len(text) - len(re.findall('[\,]',text))==len(re.findall('[0-9]',text))
        if flag_no_other_chars and flag_only_number:
            r = [int(n) for n in text.split(',')]
            return r
        else:
            return text
    else:
        return text


if __name__ == '__main__':
    # print_doc_string (process_input_int_list)
    print_doc_str_example (process_input_range)
    print_doc_str_example (process_input_int_list)
    
    print (process_input_range('[2:6]'))    
    print (process_input_int_list('1,2,3,4,5,6'))


    
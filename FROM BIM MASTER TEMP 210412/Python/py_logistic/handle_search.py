# -*- coding: utf-8 -*-
"""Tiện ích: Tra cứu thông tin"""

#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
import pandas as pd
import numpy as np
import re, os, json
from handle_string import *             # tải các hàm xử lí chuỗi
from program_var import *               # tải các Biến global


os.chdir(os.getcwd())               # thiết lập Current work Directory --> path

#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
# FUNCTION
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#

def search(value,newdata,column_heads):
    if len(value) != 0:
        print(0)        

#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def search_value_dataframe(search_value,data_material,data_material_search):
    """
        Tìm kiếm từ khóa Vật tư thiết bị
    """
    search_value = unidecode.unidecode(str(search_value).replace(" ",""))
    df_search_out = data_material.loc[[ii for ii in data_material_search.index if re.search(search_value,unidecode.unidecode(str(data_material_search.loc[ii])))]]
    return df_search_out
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#

def search_expansion(search_value,data_material,data_material_search):
    """
        Tìm kiếm từ khóa Vật tư thiết bị
    """
    df_search_out = data_material.loc[[ii for ii in data_material_search.index if check_words_exists_in(search_value,data_material_search.loc[ii])]]
    return df_search_out
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def searcher(search_value,data_search,search_column_name) -> pd.DataFrame:
    """Tra cứu Vật tư thiết bị từ Từ Khóa tìm kiếm\n### Input:\nsearch_value : Giá trị tìm kiếm\ndata_search : Dữ liệu cơ sở để tra cứu\nsearch_column_name : Tên cột dữ liệu tra cứu"""
    search_value = search_value.strip()
    data_search_result = None
    column_check_name = 'seach_does_contain'
    data_search_result = data_search.copy()
    data_search_result[column_check_name] = data_search_result[search_column_name].str.contains(search_value.replace(" ","").upper(),na = False)
    data_search_result.where(data_search_result[column_check_name] == True, inplace=True)
    data_search_result.dropna(inplace=True)
    data_search_result.drop(columns = [search_column_name, column_check_name],inplace = True)
    
    return data_search_result
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def search_number(search_value,data_search,search_column_name) -> pd.DataFrame:
    """Tra cứu Vật tư thiết bị từ Từ Khóa tìm kiếm\n### Input:\nsearch_value : Giá trị tìm kiếm\ndata_search : Dữ liệu cơ sở để tra cứu\nsearch_column_name : Tên cột dữ liệu tra cứu"""
    if ',' in search_value:
        return pd.concat([searcher(k,data_search,search_column_name) for k in search_value.split(',')],ignore_index=True)
    else:    
        df = searcher(search_value,data_search,search_column_name)
        return df#.iloc[0]#.to_dict()        


#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    path_root = os.getcwd()
    lookup_array_path = f"{path_root}\\{SUB_DATA_VTTB}\\{DATA_SEARCH_NAME}.json"
    data_search = pd.read_json(lookup_array_path,orient='records',dtype='string')
    
    search_value = input(f'\tSearch value{USER_INPUT_PREFIX}')
    print(search_number(search_value,data_search,DF_COLUMN_SEARCH_NAME))

    # l = [1,3,4,6,7]
    # l.sort(reverse=True)
    # print(l)
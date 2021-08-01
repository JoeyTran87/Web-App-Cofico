import pandas as pd
import os, unidecode
import numpy as np
os.chdir(os.getcwd())
from handle_string import *

def main():
    pd.set_option('display.max_rows', 0)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 20)

    path_data = f"{os.getcwd()}\\data_vat_tu\\data_search.json"
    # print(path_data_search)
    df = None
    if os.path.exists(path_data):
        df = pd.read_json(path_data,orient='records')
    print(df.info())
    print(df.iloc[0:150])

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        quit()

# lookup =data_search.loc[[0,1,3]]['Search string']
# print(data_search)
# print(lookup)
# display(data_search)
# print(check_words_exists_in("chong dia",lookup))
# search_val = 'tuyp'
# data_search['seach_contain'] = data_search['Search string'].str.contains(search_val.replace(" ","").upper(),na = False)
# data_search_result = data_search.copy()
# data_search_result.where(data_search_result['seach_contain'] == True, inplace=True)
# data_search_result.dropna(inplace=True)
# print(data_search_result)
# print(data_search_result.shape[0])
# series_1 = pd.Series([1,'a','b','c','d'],dtype='string')
# series_2 = pd.Series({ 'id1': [1,2,3,4,5,6,7],'id2':['a','b','c','d','e','f','g']})
# print (series_1)
# print (series_2)
# for c in df_new.columns:    
    # first_col += df_new[c].str
    # print(df_new[c])
# print(first_col).
# df_new = df.astype('string')
# print(df_new)
# print(df_new.columns)
# first_col = df_new[df_new.columns[0]]
# concat = np.array([''] * int(first_col.shape[0]))#['']*int(first_col.shape[0])
# for c in df_new.columns:    
#     concat = df_new[c].str.cat(concat)
# concat = concat.str.replace(' ', '', regex=False).str.upper()
# for c in concat.index:
#     try:
#         concat.loc[c] = str(unidecode.unidecode(concat.loc[c]))
#     except:
        # pass
# concat.loc[1] = "changed"
# print(concat.loc[0])
# print(concat.loc[1])
# arr = np.array([''] * int(first_col.shape[0]) ,dtype="string")



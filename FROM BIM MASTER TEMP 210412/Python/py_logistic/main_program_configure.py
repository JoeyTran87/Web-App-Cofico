# -*- coding: utf-8 -*-
"""Module : Quản lí Thiết lập Menu Chương trình"""
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
import pandas as pd
from handle_cmd import *
from handle_decor_func import *




def read_configure_file(menu_path) -> any:
    "Phương thức đọc tập tin TXT configure, trả về Tên, mô tả, và DS menu"
    content = ''
    with open(menu_path,'r',encoding='utf-8') as f:
        content = [l for l in f.readlines()]
    content = ''.join(content)
    # print(content)
    # print([(m.start(0), m.end(0)) for m in re.finditer('\*',content)][-1])

    name = content.split('*')[1].strip()
    description = content.split('*')[2].strip()
    warning =  content.split('*')[3].strip()
    menu = pd.read_csv(menu_path,header=5+len(description.splitlines())+len(warning.splitlines()),sep = '\t',dtype='str')
    return name,description,menu,warning



class menu_program():
    def __init__(self,path,dir_root = '.') -> any:
        self.menu_name_file_ext = str(path).split('.')[-1]
        self.menu_file_name  = str(path).split('\\')[-1][:-len(self.menu_name_file_ext)-1]
        #----------------------------------------------# tải Tên chương trình  + Mô tã + Menu từ file thiết lập menu 
        self.menu_name,  self.menu_description, menu ,self.exception= read_configure_file(path)
        #----------------------------------------------# clean data menu
        menu.dropna(subset = [menu.columns[2]],inplace = True)
        menu = menu.fillna('NA')
        self.menu_col_count = len(menu.columns)        
        menu['Merge_Number'] = menu['Group_Number']+menu['Number']
        menu['Path_Source']= dir_root+'\\'+menu['Source_Sub_Dir']+'\\'+menu['Source_Name']
        #----------------------------------------------# final Menu data
        self.menu = menu
        self.menu_list = [f"{self.menu.iloc[m][2]}" for m in self.menu.index]
        self.menu_numbers = [f"{self.menu.iloc[m][self.menu_col_count]}" for m in self.menu.index]
        self.menu_path_source_list = [f"{self.menu.iloc[m][self.menu_col_count+1]}" for m in self.menu.index]
        #----------------------------------------------# load TIPS
        self.tips_KS = HOTKEYS_GENERAL

    #-------------------------------------------------------------# GET
    def get_step(self,index):
        """return [index,name,tip,warning]"""
        name = self.menu.iloc[index][2]
        tip = self.menu.iloc[index][3] 
        warning = self.menu.iloc[index][4] 
        return [index,name,tip,warning]

    #-------------------------------------------------------------# SHOW
    def show_title(self) -> str:
        show_heading_1(self.menu_name)

    def show_title_3(self) -> str:
        show_heading_3(self.menu_name)
    def show_description(self,button_text = 'Mô tả/ Description:') -> str:
        print(button_1(button_text))
        print_text_box_L(self.menu_description)

    def show_tips(self,button_text = 'Mẹo/Tips:') -> str:
        print(button_1(button_text))
        print_text_box_L(self.tips_KS) 

    def show_warning(self):
        print_text_box_L(self.exception,hoz=' *',ver='*')

    #-------------------------------------------------------------# GET
    def show_tips_step(tip,button_text = 'Mẹo/Tips:') -> str:
        print(f"{button_1(button_text)}{tip}")
    #-------------------------------------------------------------# GET
    def get_path(self,index):
        return self.menu.iloc[index][self.menu_col_count+1]
    
    #-------------------------------------------------------------# ASK menu
    @loop_flow
    def ask_menu(self,button_text = 'Menu Steps:',promp = 'Vui lòng nhập số hiệu',breaker = BREAKER) -> str:
        print(button_1(button_text))
        ask =  ask_input_2(self.menu_list,input_prefix = f"{promp}\n{USER_INPUT_PREFIX}")
        print(breaker)
        return ask

    #-------------------------------------------------------------# ASK step
    @loop_flow
    def ask_step(self,index,pre_promp = 'Vui lòng',post_promp = ''):
        step = [index,self.menu.iloc[index][2]]
        return input(f"[Bước {step[0]}] {pre_promp} {step[1]}\n{post_promp} {USER_INPUT_PREFIX}")


    @loop_flow
    def ask_step_free(menu,pre_promp = 'Vui lòng',post_promp = ''):
        """Phương thức hỏi người dùng
        menu = list[index,name]"""
        step = [menu[0],menu[1]]
        return input(f"[Bước {step[0]}] {pre_promp} {step[1]}\n{post_promp} {USER_INPUT_PREFIX}")
    
    @loop_flow
    def ask_step_w_tips(self,index,post_promp = '',pre_promp = 'Vui lòng'):
        step = [index,self.menu.iloc[index][2],self.menu.iloc[index][3]]
        tip = ''
        try:
            tip = step[2]
        except:   
            tip = ''
            pass   
        return input(f"[Bước {step[0]}] {pre_promp} {step[1]}\n{button_1('Tips:')} : {tip}\n{post_promp} {USER_INPUT_PREFIX}")
    
    @loop_flow
    def ask_step_w_tips_free(menu,post_promp = '',pre_promp = 'Vui lòng'):
        """##### Phương thức hỏi người dùng
        ###### menu (list) : [index,name,tips,...]"""
        step = menu
        tip = ''
        try:
            tip = step[2]
        except:  
            tip = '' 
            pass         
        return input(f"[Bước {step[0]}] {pre_promp} {step[1]}\n{button_1('Tips:')} : {tip}\n{post_promp} {USER_INPUT_PREFIX}")
    
    #-------------------------------------------------------------# warning
    def warning(self,index,promp = 'Vui lòng thử lại'):
        try:
            note = self.menu.iloc[index][4]
            # print(f"[!] {note} [!] {promp}")
            print_text_box_L(f"{note}\n{promp}",hoz = '_ ', ver = '!')
        except:
            print(promp)


# def configurer():
#     """"""
#     menu_item_list = []
#     menu_item = [{'group_number': '80',
#                 'number_order':'1',
#                 'number':'801',
#                 'name':'Xây dựng dữ liệu từ excel',
#                 'discription':'Là tiến trình xây dữ liệu DataFrame tải từ tập tin excel',
#                 'tips':'Bạn nên sử dụng cú pháp...',
#                 'warning':'Nhập sai cú pháp',
#                 'path_source_file_absolute':'',
#                 'path_source_file_relative':'',
#                 },
#                 {'group_number': '80',
#                 'number_order':'1',
#                 'number':'801',
#                 'name':'Xây dựng dữ liệu từ excel',
#                 'discription':'Là tiến trình xây dữ liệu DataFrame tải từ tập tin excel',
#                 'tips':'Bạn nên sử dụng cú pháp...',
#                 'warning':'Nhập sai cú pháp',
#                 'path_source_file_absolute':'',
#                 'path_source_file_relative':'',
#                 },
#                 ]

#     df = pd.DataFrame(menu_item,dtype='str')
#     print (df)
#     print (df.columns)

# def transfer_oldtxt_to_json():    
#     """"""
#     pd.set_option('display.width', None)
#     pd.set_option('display.max_colwidth', 30)


#     file_name_1 = 'menu_data_builder'
#     file_name_2 = 'menu_data_editor'
#     file_name_3 = 'menu_data_selector'

#     file_names = [file_name_1,file_name_2,file_name_3]

#     container_dir = "C:\\Users\\USER\\Documents\\GitHub\\cofico\\cofico\\FROM BIM MASTER TEMP 210412\\Python\\py_logistic\\configures"
    
#     for fn in file_names:
#         config_data_type = f"{container_dir}\\{fn}.txt"
#         menu_data_type = menu_program(config_data_type)
#         df = menu_data_type.menu
#         df.columns = ['group_number', 'number_order', 'name', 'tips', 'warning', 'path_source_file_absolute',
#         'discription', 'number', 'path_source_file_relative']    
#         new_df = df.reindex(columns = ['group_number', 'number_order', 'number', 'name', 'discription', 'tips',
#         'warning', 'path_source_file_absolute', 'path_source_file_relative'])       
#         print(new_df)
#         print(new_df.columns)
#         new_df.to_json(f"{container_dir}\\{fn}.json",orient = 'records')
#         new_df.to_xml(f"{container_dir}\\{fn}.xml")

#     path_1 = f"{container_dir}\\{file_name_1}.json"
#     path_2 = f"{container_dir}\\{file_name_2}.json"
#     path_3 = f"{container_dir}\\{file_name_3}.json"

#     combine_df = pd.concat([pd.read_json(path_1,encoding='utf-8',orient='records'),
#                             pd.read_json(path_2,encoding='utf-8',orient='records'),
#                             pd.read_json(path_3,encoding='utf-8',orient='records')],
#                             ignore_index=True)

#     print (combine_df)
#     combine_df.to_json(f"{container_dir}\\configurer.json",orient='records',indent=4)
#     combine_df.to_xml(f"{container_dir}\\configurer.xml")

# def edit_configurer(path):
#     """"""
#     # TODO: sử dũng tkinter form

#     pd.set_option('display.width', None)
#     pd.set_option('display.max_colwidth', 100)
#     df = pd.read_xml(path)
    
#     # print (df)
#     # print('Columns')
#     # [print(c) for c in df.columns]

#     for i in df.index:
#         item = df.iloc[i]
#         print_text_box_L('\n'.join([f"{df.columns[i]} : {item[i]}" for i in range(len(item))]))
#         print_center_align(item.to_dict())
#         ask_user = ask_edit(promp = 'Bạn muốn biên tập Item này (y/n)')
#         if ask_user == True:
#             pass


# @decor_ask_boolean
# def ask_edit(promp = 'Vui lòng xác nhận (y/n)'):
#     return input(f"{promp}\n{USER_INPUT_PREFIX}")

#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
def read_configure_file_2(path_config) -> any:
    "Phương thức đọc tập tin Excel configure, trả về Tên, mô tả, và DS menu"
    content = ''
    with open(path_config,'r',encoding='utf-8') as f:
        content = [l for l in f.readlines()]
    content = ''.join(content)
    # print(content)
    # print([(m.start(0), m.end(0)) for m in re.finditer('\*',content)][-1])

    name = content.split('*')[1].strip()
    description = content.split('*')[2].strip()
    warning =  content.split('*')[3].strip()
    menu = pd.read_csv(path_config,header=5+len(description.splitlines())+len(warning.splitlines()),sep = '\t',dtype='str')
    return name,description,menu,warning



class menu_manager():
    def __init__(self,path_excel) -> None:
        self.menu_dict = pd.read_excel(path_excel,sheet_name=None,dtype='str')
        self.menu_combine = pd.concat([ self.menu_dict[d] for d in  self.menu_dict],ignore_index=True).fillna('NA')
        self.menu_parents = self.menu_dict['program']        

    #---------------------------------------------------------------#
    #---------------------------------------------------------------#
    #---------------------------------------------------------------#
    #---------------------------------------------------------------#
    def menu_by_sheet_name(self,sheet_name_):
        """Lấy toàn bộ DS menu của 1 sheet"""
        self.menu = self.menu_dict[sheet_name_]
        return self.menu
    def menu_by_global_number(self,number):
        """Lấy menu khớp Global ID"""
        cond =  self.menu_combine['global_number'] == number
        self.menu =  self.menu_combine.where(cond).dropna(subset=['global_number'])
        return self.menu
    def menu_by_global_numbers(self,numbers):
        """Lấy menu khớp Global ID"""
        menu_list = []
        for number in numbers:
            cond =  self.menu_combine['global_number'] == number
            menu_list.append(self.menu_combine.where(cond).dropna(subset=['global_number']))
        self.menu = pd.concat(menu_list)
        return self.menu
    
    def menu_by_parent_number(self,number):
        cond =   self.menu_combine['parent_number'] == number
        self.menu =   self.menu_combine.where(cond).dropna(subset=['global_number'])
        return self.menu
    #---------------------------------------------------------------#
    #---------------------------------------------------------------#
    #---------------------------------------------------------------#
    @heading_wrap
    def show_name(self,name):
        name = name.upper()
        print(f'\t {name}')
    #---------------------------------------------------------------#
    #---------------------------------------------------------------#
    #---------------------------------------------------------------#
    def show_content_box(self,content,hoz = ' =',ver = '+'):
        """In ra thông tin trong Hộp Chữ"""
        while True:
            if type(content) == list:
                # [print(c) for c in content]
                list_len = []
                for c in content:
                    try:
                        list_len.append(len(c))
                    except:
                        pass
                list_len.sort()
                max_row_width = list_len[-1]

                blank = ' '*(max_row_width + 6)
                head_line = f"\t{hoz*int((max_row_width + 6)/len(hoz))}"
                print(head_line)        
                for c in content:
                    if len(c) > 0:
                        line = [ch for ch in blank]
                        range_ = range(3,3+len(c))
                        for i in range_:
                            line[i] = c[i-3]                    
                        print(f"\t{ver}{''.join(line)}{ver}")
                print(head_line) 
                break       
            elif type(content) == str:
                if content == 'NA':
                    return
                else: content = content.splitlines()   
                
    def ask_input(self,menu_df,button_text = 'Danh sách các bước xử lí:',promp = 'Vui lòng nhập [Số Hiệu]') -> str:
        """- menu_df (DataFrame)"""
        print(button_1(button_text))
        menu_df = menu_df[['global_number','name','item_number']]
        menu_df.index = range(len(menu_df.index))
        for i in menu_df.index:
            if len(menu_df.iloc[i]['name']) > 0:
                print(f"\t[{menu_df.iloc[i]['global_number']}]\t{menu_df.iloc[i]['name']}")
        ask = input(f"{promp}\n{USER_INPUT_PREFIX}")
        return ask


#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    """"""    
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 30)
    container_dir = "C:\\Users\\USER\\Documents\\GitHub\\cofico\\cofico\\FROM BIM MASTER TEMP 210412\\Python\\py_logistic\\configures"
    file_name_1 = 'menu_data_builder'
    file_name_2 = 'menu_data_editor'
    file_name_3 = 'menu_data_selector'

    file_names = [file_name_1,file_name_2,file_name_3]
    path_1 = f"{container_dir}\\{file_name_1}.xml"
    path_2 = f"{container_dir}\\{file_name_2}.xml"
    path_3 = f"{container_dir}\\{file_name_3}.xml"

    # transfer_oldtxt_to_json()
    # edit_configurer(path_3)

    path = r'C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\py_logistic\configures\configure.xlsx'
    sheet_names = ['program','data_selector','data_editor','data_builder']
    
    menu = menu_manager(path)
    
    # print(menu.menu_combine)
    # print(menu.menu_by_global_number('800'))
    menu.ask_input(menu.menu_by_global_number('1'))
    # print(menu.menu_by_global_numbers(['800','801']))
    menu.ask_input(menu.menu_by_global_numbers(['1','2']))

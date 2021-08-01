# -*- coding: utf-8 -*-
"""Module hỗ trợ các lệnh về Terminal / Shell cho chươngtrinh2]]
"""
import time,os,subprocess
from program_var import *
from handle_string import *

##############################################################################
# CÁC HÀM TIẾN TRÌNH:  CHỜ ĐỢI
##############################################################################

#--------------------------------------------------------------#
# define the countdown func.
#--------------------------------------------------------------#

def countdown(t,str_count,str_done):    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(str_count,timer, end="\r")
        time.sleep(1)
        t -= 1      
    print(f"--------{str_done}-------------")
    

#--------------------------------------------------------------#
# WAITING BY SPINNER
#--------------------------------------------------------------#
def spinWaiting(breaker):
    spin = "|/-\\" 
    t = 0.5
    while t:
        for s in spin:
            print(s, s, s ,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,end="\r")
            time.sleep(1/len(spin))
        t -= 0.5

    print(breaker)
# spin(3)


def spinWaiting_dot():
    spin1 = ".    " 
    spin2 = ". .  "
    spin3 = ". . ."
    t = 4
    while t > 0:
        print(spin1,end="\r")
        time.sleep(0.7)
        print(spin2,end="\r")
        time.sleep(0.7)
        print(spin3,end="\r")
        time.sleep(0.7)
        t -= 1

    print("------------------------------------------------------------------")

def spin_text (text):
    # text = "COFICO BIM MANAGER LOADING . . . . ."    
    t = 3
    while t>0:
        for i in range(len(text)):
            prs = text[:i+1]+" "*len(text[i:])
            print(prs,end="\r")
            time.sleep(0.1)
        t -= 1
    print("------------------------------------------------------------------")


def spin_percentage(count):
    while count > 0:
        for i in range(count):
            print(f"""-----{round(i/count,1)}%-----
            ------------------------------------------------------------------""",end="\r")
            pass

def spin_three_dots(promp,_time = 3):
    for i in range(_time):
        print(f"{promp} {'.'*(i+1)}",end='\r')
        time.sleep(0.5)
    print(" "*(len(f"{promp} {'.'*_time}")+1),end='\r')
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#

# MỞ COMMAND PROMP MỚI
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def run_cmd(cmd_command):
    """example: py C:\\Users\\tvpduy\\py_logistic\\monitor_master.py"""
    cmd_call = f"start /B start cmd.exe @cmd /k {cmd_command}..."
    os.system(cmd_call)
# Chạy 1 COMMAND trong tiến trình gọi lệnh sau:
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def run_cmd_2(cmd_command): 
    subprocess.run(cmd_command, shell= True)
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def show_heading_1(content) -> str:
    """(có spinner)
    content : Nội dung
    # Example:\nshow_heading_1('Title')"""
    global BREAKER, START_END_LINE
    spinWaiting(BREAKER)
    new_text = ''
    for c in str(content).upper():
        if c == " ":
            c = "  "
        new_text += c + " "
    print(f'\t {new_text}')
    print(BREAKER)
    return content
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def show_heading_2(content):
    """(Không có spinner)
    content : Nội dung
    ### Example:\nshow_heading_2('Title')"""
    global BREAKER, START_END_LINE
    print(BREAKER)
    new_text = ''
    for c in str(content).upper():
        if c == " ":
            c = "  "
        new_text += c + " "
    print(f'\t {new_text}')
    print(BREAKER)
    return content
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def show_heading_3(content):
    """(Không có spinner + Không giãn cách + Hoa đầu chữ)
    content : Nội dung
    ### Example:\nshow_heading_3('Title')"""
    print(BREAKER)
    content = str_capital_each(content)
    print(f'\t {content}')
    print(BREAKER)
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def show_heading_4(content):
    """(Không có spinner + Không giãn cách + HOA TOÀN BỘ)
    content : Nội dung
    ### Example
    show_heading_3('Title')"""
    print(BREAKER)
    content = content.upper()
    print(f'\t {content}')
    print(BREAKER)
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def show_heading_5(content):
    """(Không có spinner + Không giãn cách + HOA TOÀN BỘ)
    content : Nội dung
    ### Example
    show_heading_3('Title')"""
    print(BREAKER)
    [print(f"\t{l}") for l in content.splitlines()]
    print(BREAKER)
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def show_subtitle(subtitle,header = 'Tips:'):
    global BREAKER, START_END_LINE
    print(BREAKER)
    print(f"\t[ {header} ]")
    if type(subtitle) == str:
        subtitle = subtitle.splitlines()
    if type(subtitle) == list:
        subtitle = [s for s in subtitle if s and len(s) > 0]
    for t in subtitle:
        t = t.strip()
        try:
            tip  = t.split('\t')
            print(f"\t{tip[0]}\t{tip[1]}")
        except:
            print(f"\t{t}")
            pass
 
    print(BREAKER)
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def show_menu_1 (title,subtitle,menu_list,prefix = " >>>> ",tips = HOTKEYS_GENERAL) -> str:
    """[CÓ] title
    title : Tiêu đề
    subtitle : Phụ đề
    menu_list : Danh sách menu
    prefix: Tiền tố nhập liệu
    """       
    show_heading_1(title)
    show_heading_5(subtitle)
    show_subtitle(tips)
    print('\t[ Menu ] : ')
    user_input = ask_input(menu_list,input_prefix = prefix)
    return user_input
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def show_menu_2 (subtitle,menu_list,prefix = ">>>> ") -> any:
    """[KHÔNG CÓ] title
    subtitle : Phụ đề
    menu_list : Danh sách Menu / String các dòng Menu
    input_prefix: Tiền tố nhập liệu
    promp_list : Danh sách menu"""      

    show_heading_3(subtitle)    
    if type(menu_list) == str:
        menu_list = menu_list.splitlines()
    if type(menu_list) == list:
        user_input = ask_input(menu_list,input_prefix = prefix)
        return user_input
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def warning(promp):
    """[Cảnh báo] tiến trình chưa phù hợp
    action (str) : Tên tiến trình
    promp (str) : Lời nhắc"""
    print(f"\t[!] {promp} [!]")
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def warning_1(action,promp):
    """[Cảnh báo] tiến trình chưa phù hợp
    action (str) : Tên tiến trình
    promp (str) : Lời nhắc"""
    print(f'\tBạn đã {action} {promp}')
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def ask_input_1(number,action,tips,input_prefix = " >>>> ") -> str:
    """[Hỏi] người dùng Nhập liệu
    number(str) : Số hiệu tiến trình
    action (str) : Tên tiến trình
    prefix (str) : Tiền tố vị trí nhập liệu"""
    return input((f"\t[{number}] {action}:\n\t[Tips]: {tips}\n\t{input_prefix} "))  
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def ask_input(menu_list,input_prefix = " >>>> ") -> str:
    """[Hỏi] người dùng Nhập liệu
    menu_list(list) : Danh sách menu
    input_prefix (str) : Tiền tố vị trí nhập liệu"""
    print(BREAKER)
    for i,value in enumerate(menu_list):
        if len(value) > 0:
            print(f"\t{i}\t{value}")
    user_input = input(f"{input_prefix} : ")
    print(BREAKER)
    return user_input
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def ask_input_2(menu_list,input_prefix = " >>>> ") -> str:
    """[Hỏi] người dùng Nhập liệu [NON BREAKER]
    menu_list(list) : Danh sách menu
    input_prefix (str) : Tiền tố vị trí nhập liệu"""
    for i,value in enumerate(menu_list):
        if len(value) > 0:
            print(f"\t[{i}]\t{value}")
    user_input = input(f"{input_prefix}")
    return user_input
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def show_menu_tree_view(PROMP_MAIN_MENU,
                show_level = 0,
                number = 'Number',
                name = 'Name',
                level = 'Level',
                group = 'Group',
                keep_group = None) -> str:    
    """Xử lí Print Menu theo level"""    
    dict_list = []        
    for l in PROMP_MAIN_MENU.splitlines():
        l = l.strip()
        if len(l) > 3:
            dict_ = {}
            key = f"{l.split(' ')[0]}"
            dict_[number] = key
            dict_[group] = key[0]
            dict_[name] = l[len(l.split(' ')[0]):].strip()
            if not '.' in key:
                dict_[level] = 0
            else:
                finder = re.findall('[.]',key)
                level_number = len(finder)
                dict_[level] = level_number
            dict_list.append(dict_)
    # print (dict_list)
    for d in dict_list:
        if int(d[level]) <= show_level:
            indent = '  '*(int(d[level])+1)
            if not keep_group:
                print(f"{indent}[{d[number]}]  {d[name]}")
            else:
                if keep_group == d[group]:
                    print(f"{indent}[{d[number]}]  {d[name]}")

    return input(f"\tChọn Số hiệu menu: {USER_INPUT_PREFIX}")
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------#
def print_doc_string (function_name):   
    """In ra docstring của các Hàm Function\function_name : Tên hàm"""
    print(f"\tFunction Docstring:")
    [print(f"\t\t{d}") for d in function_name.__doc__.splitlines()]
#-----------------------------------------------------------------------#
def get_func_doc_string (function_name):   
    """Lấy docstring của các Hàm Function\function_name : Tên hàm"""
    return function_name.__doc__
#-----------------------------------------------------------------------#
def print_doc_str_example (function_name):   
    """In ra docstring của các Hàm Function\function_name : Tên hàm"""
    print('\t',function_name.__doc__.splitlines()[1])
#-----------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def print_text_box_R(content,hoz = '=',ver = '|'):
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
            str_L = "{:<"+"{0}".format(max_row_width)+"}"
            str_R = "{:>"+"{0}".format(max_row_width)+"}"
            # align_L = str_L.format('|')
            # align_R = str_R.format('|')
            head_line = f"\t{hoz*int((max_row_width+6)/len(hoz))}"
            print(head_line)        
            [print(f"\t{ver}  {str_R.format(c)}  {ver}") for c in content if len(c) > 0]
            print(head_line) 
            break       
        elif type(content) == str:
            content = content.splitlines()   
#-----------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
def print_text_box_L(content,hoz = ' =',ver = '+'):
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
            content = content.splitlines()   

def button_1(text):
    return f"[ {''.join([ch for ch in text])} ]"
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    header =  'Title'
    input_prefix = '>>>>'
    menu = [  "Chọn [đường dẫn file] Excel Kế hoạch VTTB",
                    "Chọn [tên Sheet] Excel",
                    "[Xem xét] dữ liệu Kế hoạch sau",
                    "Chọn [SỐ DÒNG] làm TIÊU ĐỀ CỘT",
                    "Chọn [SỐ CỘT] dữ liệu (giữ lại)",
                    "[Xem xét] Bảng dữ liệu Kế hoạch đã làm sạch",
                    "Chọn [SỐ CỘT] Dữ kiện TÌM KIẾM",
                    "Chọn [SỐ CỘT] mà Kết quả sẽ TRẢ VỀ",
                    "[Xem xét] dữ liệu [Tra cứu] VTTB",
                    "Chọn [SỐ CỘT] Tra cứu",
                    "Chọn [SỐ CỘT] Kết quả",
                    "[Xem xét] KẾT QUẢ TRA CỨU",
                    "Xuất dữ liệu Excel",
                    "",
                    ""]
    menu_str = """Chọn [đường dẫn file] Excel Kế hoạch VTTB
Chọn [SỐ DÒNG] làm TIÊU ĐỀ CỘT
Chọn [SỐ CỘT] dữ liệu (giữ lại)
[Xem xét] Bảng dữ liệu Kế hoạch đã làm sạch
Chọn [SỐ CỘT] Dữ kiện TÌM KIẾM
Chọn [SỐ CỘT] mà Kết quả sẽ TRẢ VỀ
[Xem xét] dữ liệu [Tra cứu] VTTB
Chọn [SỐ CỘT] Tra cứu
Chọn [SỐ CỘT] Kết quả
[Xem xét] KẾT QUẢ TRA CỨU
Xuất dữ liệu Excel"""
    # show_menu_1(header,menu,input_prefix)

    # show_subtitle(HOTKEYS_GENERAL)
    content = menu
    # print_text_box_R(content)
    
    pass




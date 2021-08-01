#---------------------------------------------------------#
# set current work directory (CWD)
#---------------------------------------------------------#
import os,json
os.chdir(os.getcwd())
from handler_string import *
import cv2
import requests
import io

from main_snapshot_3 import *
#---------------------------------------------------------------------------------------#
# GLOBAL VARIABLES
#---------------------------------------------------------------------------------------#  
url_api = "https://api.ocr.space/parse/image"
api_key = "29ba004cce88957" # ACCOUNT duytran.arch@gmail.com
img_name = ''
json_saved_path = ''
path_root = ''
promp_brief = """
------------------------------------------------------------------------------------------------
                        CHÀO MỪNG BẠN ĐẾN VỚI ỨNG DỤNG
                                TEXT DETECTION
GIỚI THIỆU ỨNG DỤNG :                           
------------------------------------------------------------------------------------------------
    ỨNG DỤNG VIẾT BẰNG NGÔN NGỮ PYTHON, SỬ DỤNG CÁC MODULE / LIBRARY : cv2, ocr.space.api
    GIÚP NGƯỜI DỤNG CHUYỂN TEXT TỪ HÌNH ẢNH SCREEN SHOT THÀNH DỮ LIỆU ĐIỆN TỬ (.json)
"""
promp_menu="""
    ------------------------------------------------------------------------------------------------
                                MENU CHƯƠNG TRÌNH
    ------------------------------------------------------------------------------------------------
        1. Chụp màn hình --> Xén hình --> Điều tra TEXT

        2. Mở MỘT tập tin hình ảnh --> Xén hình --> Điều tra TEXT

        3. Xử lí NHIỀU tập tin hình ảnh đã xén lưu sẵn có--> Điều tra TEXT

        0. Thoát chương trình

    ---Vui lòng chọn số hiệu thao tác: """
#---------------------------------------------------------------------------------------#
# MAIN
#---------------------------------------------------------------------------------------#  
def main():
    print(promp_brief)
    global path_root
    path_root = input("Nhập đường dẫn thư mục lưu tạm hình hình Screen shot: ")
    ask_menu = input(promp_menu)
    while ask_menu != "0":
        if ask_menu == "1":
            method_screen_shot()
        elif ask_menu == "2":
            method_open_image()
        elif ask_menu == "3":
            pass
        else:
            pass
        ask_menu = input(promp_menu)
    if ask_menu == "0":
        time_end = time.strftime("%H:%M:%S %a %d %b %Y ",time.localtime(time.time()))
        print(f"---Bạn đang thoát chương trình vào lúc {time_end}")
        print(f"{'-'*96}")
        quit()
#---------------------------------------------------------------------------------------#
# ĐIỀU TRA TEXT
#---------------------------------------------------------------------------------------#
def detect_text(img,json_saved_path):
    # CROP IMAGE + compress
    ask_detect = input("---Bạn muốn Tìm kiếm dữ liệu TEXT (y/n): ").lower()
    if ask_detect == "y":
        _, compress_img = cv2.imencode(".jpg",img,[1,90])
        file_bytes = io.BytesIO(compress_img)
        # CALL OCR API
        result = requests.post(url_api,
                                files = {img_name:file_bytes},
                                data = {'apikey': api_key}).content.decode()
        # Write json
        with open(json_saved_path,'w') as f:
            f.write(result)
        watch_detection()
#---------------------------------------------------------------------------------------#
# 1. Chụp màn hình --> Xén hình --> Điều tra TEXT
#---------------------------------------------------------------------------------------#
def method_screen_shot():
    global img_name,json_saved_path
    # TAKE SNAP SHOT
    img_name = main_snapshot_(path_root)
    json_saved_path = f"{img_name.split('.')[0]}.json"
    img = cv2.imread(img_name)
    # DETECT TEXT
    detect_text(img,json_saved_path)
#---------------------------------------------------------------------------------------#
# 2. Mở MỘT tập tin hình ảnh --> Xén hình --> Điều tra TEXT
#---------------------------------------------------------------------------------------#
def method_open_image():
    global img_name,json_saved_path
    json_saved_path=''
    flag_exist = False
    # LOOP NHẬP ĐƯỜNG DẪN FILE
    while flag_exist == False:
        img_name = input("---Nhập đường dẫn tập tin hình ảnh: ")        
        # CHECK FILE CÓ TỒN TẠI
        if os.path.exists(img_name): 
            break
    json_saved_path = f"{img_name.split('.')[0]}.json"
    img = cv2.imread(screen_shot_crop(img_name))
    detect_text(img,json_saved_path)
    
#---------------------------------------------------------------------------------------#
# 3. Xử lí NHIỀU tập tin hình ảnh đã xén lưu sẵn có--> Điều tra TEXT
#---------------------------------------------------------------------------------------#
def method_open_image_folder():
    pass
#---------------------------------------------------------------------------------------#
# WATCH JSON DATA
#---------------------------------------------------------------------------------------#
def watch_detection():
    im_result = None
    with open(json_saved_path, 'r',encoding='mbcs') as f:
        im_result = json.loads(f.read())  
    print(no_accent_vietnamese_unicoder(im_result['ParsedResults'][0]['ParsedText'],upper = True))


#test
try:
    main()    
except KeyboardInterrupt:
    quit()


import os,subprocess,time

import shutil



path = r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\py_logistic\test_install.py"
curent_work_dir = os.getcwd()
dir_ = path[:-len(path.split('\\')[-1])-1]
script = path[-len(path.split('\\')[-1]):]

def main():
    print (curent_work_dir)
    # print('You are here')
    # os.system(script)
    # stream = os.popen('echo Returned output',mode = 'r')        
    # output = stream.read()
    # print(output)
    
    ###############################################################################
    # process = subprocess.Popen(['echo', 'More output'],
    #                  stdout=subprocess.PIPE, 
    #                  stderr=subprocess.PIPE)
    # stdout, stderr = process.communicate()
    # print(stdout, stderr)

    # test = subprocess.run(script,shell=True, capture_output=True,text =True, check = True) # text = True thì không dùng stdout.decode()
    # print(test.returncode)
    # print(test.stdout.strip())
    # print(type(test.stdout))

    # print(json.loads(test.stdout.strip()))
    ###############################################################################
    py_script_name = 'main_USD_logistic.py'
    py_setup_name = f'setup_{py_script_name}'
    os.system(f"py {py_setup_name} py2exe")

    
    program_name = py_script_name.split('.')[0]
    path_exe_folder = f"{curent_work_dir}\\dist"
    time_write = time.strftime("%y%m%d%H%M%S",time.localtime(time.time()))
    path_exe_folder_move = f"{curent_work_dir}\\release\\{program_name}-{time_write}"
    path_exe_file = f"{path_exe_folder}\\{program_name}.exe"

    # NEED DATA COPY
    # ORIGIN
    path_1 = f"{curent_work_dir}\\data_vat_tu\\data.json"
    path_2 = f"{curent_work_dir}\\data_vat_tu\\data_search.json"
    path_3 = f"{curent_work_dir}\\data_vat_tu\\tonkho.json"
    path_4 = f"{curent_work_dir}\\template"


    # COPY TO
    path_1_copy = f"{path_exe_folder_move}\\data_vat_tu\\data.json"
    path_2_copy = f"{path_exe_folder_move}\\data_vat_tu\\data_search.json"
    path_3_copy = f"{path_exe_folder_move}\\data_vat_tu\\tonkho.json"
    path_4_copy = f"{path_exe_folder_move}\\template"

    if os.path.isdir(path_exe_folder) and os.path.exists(path_exe_file):
        print ('\tInstalled')

        shutil.move(path_exe_folder,path_exe_folder_move)

        os.mkdir(f"{path_exe_folder_move}\\data_vat_tu")
        os.mkdir(f"{path_exe_folder_move}\\debug")
        os.mkdir(f"{path_exe_folder_move}\\data_user")
        os.mkdir(f"{path_exe_folder_move}\\data_yeu_cau_VTTB")
        shutil.copy2(path_1,path_1_copy)
        shutil.copy2(path_2,path_2_copy)
        shutil.copy2(path_3,path_3_copy)
        shutil.copy2(path_3,path_3_copy)
        shutil.copy2(path_4,path_4_copy)
        print ('\tData Copied')

    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()
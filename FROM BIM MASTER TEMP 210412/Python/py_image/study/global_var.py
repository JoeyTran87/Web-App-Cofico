

global_list = [1,2,3]

def add_to_global_list():
    global global_list # THAM CHIẾU TỚI 1 BIẾN ĐÃ TẠO TRƯỚC ĐÓ
    global_list.append('add more')

add_to_global_list()
print(global_list)
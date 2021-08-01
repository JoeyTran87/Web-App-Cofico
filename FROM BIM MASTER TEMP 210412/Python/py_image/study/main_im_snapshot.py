import cv2
import pyautogui, time
import win32api
#https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes

from pynput.mouse import Button, Controller,Listener
# https://pythonhosted.org/pynput/mouse.html
# https://nitratine.net/blog/post/how-to-get-mouse-clicks-with-python/

#---------------------------------------------------------#
# set current work directory (CWD)
#---------------------------------------------------------#
import os,json
os.chdir(os.getcwd())




def main():
    #---------------------------------------------------------#
    # Start program
    #---------------------------------------------------------#
    time.sleep(1)
    # left, top, width, height = pyautogui.locateOnScreen('nine.png')
    # print(left, top, width, height)
    #---------------------------------------------------------#
    # Key shortcut to Snap screen
    #---------------------------------------------------------#
    flag_combo_key = False
    print("Bấm tổ hợp phím Ctrl + Shift + J để bắt đầu Screen Shot")
    flag_combo_key = listener_combo_keys()
    #---------------------------------------------------------#
    # TAKE SHOT
    #---------------------------------------------------------#    
    if flag_combo_key:
        print("(Thực hiện 2 lần) Ctrl + Shift + Alt + Click để chọn góc Ảnh Screen shot)")
        time.sleep(0.1)
        screen_shot()        
        pass
        # MOUSE CLICK listener


    # pyautogui.screenshot('screenshot.png')

    #---------------------------------------------------------#
    # Save Image
    #---------------------------------------------------------#



    #---------------------------------------------------------#
    # Out image data to OCR
    #---------------------------------------------------------#






##########################################################################################
##########################################################################################

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    # if not pressed:
    #     # Stop listener
    #     return False
    return x,y

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))
def listener():
    # Collect events until released
    try:
        with Listener(
                on_move=on_move,
                on_click=on_click,
                on_scroll=on_scroll) as listener_mouse_click:
            listener_mouse_click.join()

    except KeyboardInterrupt:
        quit()
"""
Listerer MOUSE CLICK

# shift = win32api.GetKeyState(0x10)
# ctrl = win32api.GetKeyState(0x11)
# alt = win32api.GetKeyState(0x12)
# mouse_L_click =  win32api.GetKeyState(0x01)
# mouse_R_click =  win32api.GetKeyState(0x02)
# zero_key = win32api.GetKeyState(0x30)
# zero_number_key = win32api.GetKeyState(0x60)
# j_key = win32api.GetKeyState(0x4A)
"""
def listener_csa_click():
    xy = None
    while True:        
        if win32api.GetKeyState(0x10) < 0 and win32api.GetKeyState(0x11) < 0 and win32api.GetKeyState(0x12) < 0 and win32api.GetKeyState(0x01) < 0: # ctrl + shift +alt + click
            xy = pyautogui.position()
            print (f"Mouse position: {xy}")
            break
        time.sleep(0.001)
    return xy.x, xy.y  
"""
Listerer COMBO KEY DOWN
"""
def listener_combo_keys():
    while True:        
        if win32api.GetKeyState(0x10) < 0 and win32api.GetKeyState(0x11) < 0 and win32api.GetKeyState(0x4A) < 0: # shift + click + J
            return True
        time.sleep(0.001)

def screen_shot():
    im_name = 'screen_shot_full.png'
    pyautogui.screenshot(im_name)
    time.sleep(0.1)
    img = cv2.imread(im_name)   

    cv2.imshow('Img',img)
    cv2.waitKey(10)
    # MAXIMIZE WINDOW
    try:
        left, top, width, height = pyautogui.locateOnScreen('find_maximize_button.png')   
        pyautogui.click(left+width/2,top+height/2)
    except:
        pass
    time.sleep(0.1)
    # cv2.waitKey(0)
    x1,y1 = listener_csa_click()
    time.sleep(1)
    x2,y2 = listener_csa_click()
    if x1 or y1 or x2 or y2:
        time.sleep(0.1)
        cv2.destroyWindow('Img')
    # cv2.destroyAllWindows()
##########################################################################################
##########################################################################################

# TEST

try:    
    main()
    # screen_shot()
    pass
except KeyboardInterrupt:
    quit()

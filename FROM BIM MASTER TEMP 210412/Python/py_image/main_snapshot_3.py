#---------------------------------------------------------#
# IMPORT MODULE , set current work directory (CWD)
#---------------------------------------------------------#
import os,time,pyautogui
import win32api
os.chdir(os.getcwd())
# import the necessary packages
import cv2

#---------------------------------------------------------#
# GLOBAL VARIABLES
#---------------------------------------------------------#
refPt = []# initialize the list of reference points and boolean indicating whether cropping is being performed or not
cropping = False
image = None

#---------------------------------------------------------#
# TRIGGER : CLICK THEN CROP IMAGE
#---------------------------------------------------------#
def click_and_crop(event, x, y, flags, param):	
	global refPt, cropping,image# grab references to the global variables	
	if event == cv2.EVENT_LBUTTONDOWN:# if the left mouse button was clicked, record the starting (x, y) coordinates and indicate that cropping is being performed
		refPt = [(x, y)]
		cropping = True	
	elif event == cv2.EVENT_LBUTTONUP:# check to see if the left mouse button was released		
		refPt.append((x, y))# record the ending (x, y) coordinates and indicate that  the cropping operation is finished
		cropping = False		
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)# draw a rectangle around the region of interest
		cv2.imshow("image", image)
#---------------------------------------------------------#
# FUNCTION: SCREEN SHOT
#---------------------------------------------------------#
def screen_shot(path_root):
	t = time.strftime("%y%m%d%H%M%S",time.localtime(time.time()))
	im_name = f'{path_root}\\screen_shot_full-{t}.png'
	pyautogui.screenshot(im_name)
	time.sleep(0.1)
	try:
		left, top, width, height = pyautogui.locateOnScreen('find_maximize_button.png') 
		pyautogui.click(left+width/2,top+height/2)
	except:
		pass
	time.sleep(0.25)
	return im_name

def screen_shot_crop(im_name):
	global image
	crop_im_name = ""
	print("""	---2. Bạn cần chọn Vùng Crop
	------BẤM Q ĐỂ THOÁT
	------BẤM C ĐỂ HOÀN TẤT CROP
	------BẤM R ĐỂ CROP LẠI""")
	window_name_1 = f"{'-'*10}image{'-'*10}"
	cv2.namedWindow(window_name_1,cv2.WINDOW_KEEPRATIO)
	image = cv2.imread(im_name)
	clone = image.copy()	
	cv2.setMouseCallback(window_name_1, click_and_crop)
	while True:	# keep looping until the 'q' key is pressed		
		cv2.imshow(window_name_1, image)# display the image and wait for a keypress
		key = cv2.waitKey(1) & 0xFF # KEYBOARD = Q	
		if key == ord("r") or key == ord("R"):# if the 'r' key is pressed, reset the cropping region
			image = clone.copy()	
		elif key == ord("c") or key == ord("C"):# if the 'c' key is pressed, break from the loop
			cv2.destroyWindow(window_name_1)
			break
	if len(refPt) == 2:# if there are two reference points, then crop the region of interest from teh image and display it
		print("""	---3. Xem lại ảnh Crop
	------BẤM Q ĐỂ THOÁT TRÌNH XEM""")
		roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
		tt = time.strftime("%y%m%d%H%M%S",time.localtime(time.time()))
		crop_im_name = f"{im_name[:-len(im_name.split('.')[-1])-1]}-crop-{tt}.png"
		cv2.imwrite(crop_im_name, roi)
		window_name_2 = f"{'-'*10}ROI{'-'*10}"
		cv2.namedWindow(window_name_2,cv2.WINDOW_KEEPRATIO)
		cv2.imshow(window_name_2, roi)
		cv2.waitKey(0)
	cv2.destroyAllWindows()# close all open windows
	return crop_im_name

#---------------------------------------------------------#
# LISTENER
#---------------------------------------------------------#
def listener_combo_keys():
    while True:        
        if win32api.GetKeyState(0x10) < 0 and win32api.GetKeyState(0x11):# < 0 and win32api.GetKeyState(0x4A) < 0: # shift + click + J
            return True
        time.sleep(0.001)
#---------------------------------------------------------#
# MAIN
#---------------------------------------------------------#
def main_snapshot_(path_root):
	global refPt, cropping,image
	flag_combo_key = False
	im_name = ""
	crop_im_name = ""
	print("""	---1. Bấm tổ hợp phím Ctrl + Shift để bắt đầu Screen Shot""")
	flag_combo_key = listener_combo_keys()	
	# CHỤP MAN HÌNH
	if flag_combo_key:	
		im_name = screen_shot(path_root)
	# CROP HÌNH ẢNH	
	screen_shot_crop(im_name)

	return crop_im_name

#HOW TO USE:
#open CMD --> cd to Current work directory
#python main_snapshot_2.py --image screen_shot_full.png

# TEST
# try:
# 	main()
# except KeyboardInterrupt:
# 	quit()
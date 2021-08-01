# TARGET = CÁC PHƯƠNG THỨC XỬ LÍ HÌNH ẢNH

import cv2 as cv
import numpy as np
#GLOBAL VARIABLES
img_name = ""
img = None
img_window_name = ""


vid_key_wait = 1
vid_window_name = ""
video_name = ""
capture = None
#---------------------------------------------------------------------#
# IMAGE FUNCTIONS
#---------------------------------------------------------------------#
def create_image():
    global img_name,img,img_window_name
    cv.namedWindow(img_window_name,cv.WINDOW_AUTOSIZE)
    img = cv.imread(img_name)

def scale_image(img,scale): # for Image, Video saved
    new_width = int(img.shape[1]*scale)
    new_height = int(img.shape[0]*scale)
    return cv.resize(img,(new_width,new_height),interpolation=cv.INTER_AREA)

def show_image():
    global img,img_window_name
    cv.imshow(img_window_name,img)
    # cv.waitKey(0)
    # cv.destroyWindow(img_window_name)

#---------------------------------------------------------------------#
# VIDEO FUNCTIONS
#---------------------------------------------------------------------#

def create_capture():
    global capture, video_name
    capture = cv.VideoCapture(video_name)

def show_video():
    global capture,vid_window_name,vid_key_wait
    while True:
        isTrue, frame = capture.read()
        cv.imshow(vid_window_name,frame)
        if cv.waitKey(vid_key_wait) & 0xFF == ord('d'):
            break
    capture.release()
    # cv.destroyWindow(vid_window_name)
def show_video_scaled():
    global capture,vid_window_name,vid_key_wait
    while True:
        isTrue, frame = capture.read()
        frame = scale_image(frame,0.5) # SỮ DỤNG FUNC SCALE CỦA IMAGE
        cv.imshow(vid_window_name,frame)
        if cv.waitKey(vid_key_wait) & 0xFF == ord('e'):
            break
    capture.release()
    cv.destroyWindow(vid_window_name)

def change_resolution(width, height): # for video Live streaming 
    global capture
    capture.set(3,width)
    capture.set(4,height)
    pass
#---------------------------------------------------------------------#
# DRAWING
#---------------------------------------------------------------------#
def drawing_from_blank(width,height):
    blank = np.zeros((height,width,3),dtype='uint8')# width là cột, heihgt là dòng  # 3 ĐỂ TẠO RA 1 PHƯƠNG MA TRẬN CHO MÀU SẮC R G B
    # 1. Set color
    blank [:] = 172,103,0 # B G R ngược với RGB
    cv.imshow('Drawing',blank)
    #2. Draw rectange
    draw_rectange_edge(blank,(0,0),(int(width/2),int(height/2)),rgb=(0,172,103))    
    

def draw_rectange_edge(blank,corner1,corner2,rgb=(255,255,255),thk = 2):
    cv.rectangle(blank,corner1,corner2,rgb, thickness= thk)
    cv.imshow('Rectange',blank)




#---------------------------------------------------------------------#
# MAIN
#---------------------------------------------------------------------#
def main():    
    # global img_name,img,img_window_name
    # img_name = "image1.png" # TODO = input
    # img_window_name = f"{'-'*10}Image{'-'*10}"   
    # create_image()
    # img = scale_image(img,0.2)
    # show_image()

    # global video_name, capture ,vid_window_name,vid_key_wait
    # vid_key_wait = 24 # FPS 24 hình trên giây
    # video_name = "video1.mp4" # TODO = input
    # vid_window_name = f"{'-'*10}Video{'-'*10}"
    # create_capture()
    # # show_video()
    # show_video_scaled()

    drawing_from_blank(600,400)

    cv.waitKey(0)

#######################################################################
#---------------------------------------------------------------------#
# TEST
#---------------------------------------------------------------------#
#######################################################################
try:
    main()
except KeyboardInterrupt:
    quit()
    
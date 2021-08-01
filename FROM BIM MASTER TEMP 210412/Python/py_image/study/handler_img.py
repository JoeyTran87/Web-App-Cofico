import io
import cv2


def img_handler(img_name):
    # READ IMAGE
    #---------------------------------------------------------#    
    img = cv2.imread(img_name)
    imheight,imwidth,_ = img.shape
    #---------------------------------------------------------#
    # CROP IMAGE + compress
    #---------------------------------------------------------#
    crop_img = img[0:imheight,0:imwidth]
    _, compress_img = cv2.imencode(".jpg",crop_img,[1,90])
    file_bytes = io.BytesIO(compress_img)
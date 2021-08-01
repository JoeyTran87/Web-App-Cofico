import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#GLOBAL VARIABLES
img_name = ""
img = None
img_window_name = ""

def plot_image(img):
    plt.imshow(img)#,cmap='gray')
    plt.axis('off')
    # plt.style.use('seaborn')

    plt.show()


def main():
    #GLOBAL VARIABLES
    global img_name,img ,img_window_name

    img_name = "image2.png"
    img = cv.imread(img_name)
    img_window_name = f"{'-'*10}Image{'-'*10}"

    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    face_dectector = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
    face_data = face_dectector.detectMultiScale(img,1.3,5)

    for (x,y,w,h) in face_data:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi = img[y:y+h,x:x+w]

        roi = cv.GaussianBlur(roi,(25,25),70)
        img[y:y+roi.shape[0],x:x+roi.shape[1]] = roi

    plot_image(img)

main()


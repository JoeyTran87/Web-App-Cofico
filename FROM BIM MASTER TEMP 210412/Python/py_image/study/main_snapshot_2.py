#---------------------------------------------------------#
# set current work directory (CWD)
#---------------------------------------------------------#
import os,json,time
os.chdir(os.getcwd())
# import the necessary packages
import argparse
import cv2
refPt = []# initialize the list of reference points and boolean indicating whether cropping is being performed or not
cropping = False
def click_and_crop(event, x, y, flags, param):	
	global refPt, cropping# grab references to the global variables	
	if event == cv2.EVENT_LBUTTONDOWN:# if the left mouse button was clicked, record the starting (x, y) coordinates and indicate that cropping is being performed
		refPt = [(x, y)]
		cropping = True	
	elif event == cv2.EVENT_LBUTTONUP:# check to see if the left mouse button was released		
		refPt.append((x, y))# record the ending (x, y) coordinates and indicate that  the cropping operation is finished
		cropping = False		
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)# draw a rectangle around the region of interest
		cv2.imshow("image", image)

ap = argparse.ArgumentParser()# construct the argument parser and parse the arguments
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# TODO: SCREEN SHOT replace ARGUMENTS way

im_name = args["image"]# load the image, clone it, and setup the mouse callback function
image = cv2.imread(im_name)
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
while True:	# keep looping until the 'q' key is pressed
	cv2.imshow("image", image)# display the image and wait for a keypress
	key = cv2.waitKey(1) & 0xFF # KEYBOARD = Q	
	if key == ord("r"):# if the 'r' key is pressed, reset the cropping region
		image = clone.copy()	
	elif key == ord("c"):# if the 'c' key is pressed, break from the loop
		break
if len(refPt) == 2:# if there are two reference points, then crop the region of interest from teh image and display it
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    tt = time.strftime("%y%m%d%H%M%S",time.localtime(time.time()))
    crop_im_name = f"{im_name[:-len(im_name.split('.')[-1])-1]}-crop-{tt}.png"
    cv2.imwrite(crop_im_name, roi)
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)
cv2.destroyAllWindows()# close all open windows

#HOW TO USE:
#open CMD --> cd to Current work directory
#python main_snapshot_2.py --image screen_shot_full.png


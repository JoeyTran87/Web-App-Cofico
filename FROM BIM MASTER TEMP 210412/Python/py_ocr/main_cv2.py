#https://www.youtube.com/watch?v=oXlwWbU8l2o

import numpy as np
import cv2
import os,time
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
############################################
path = 'data'
test_ratio = 0.2
validate_ratio = 0.2
############################################
folder_list = os.listdir(path)
folder_count = len(folder_list)
print(f"Subfolder data: {folder_list}\tCount: {folder_count}")
images = []
class_no = []
for x in range(folder_count):
    list_picture = os.listdir(f"{path}\\{x}")
    print (x,end=" ")
    for y in list_picture:
        try:
            currnent_img = cv2.imread(f"{path}\\{x}\\{y}")
            currnent_img = cv2.resize(currnent_img,(32,32))
            images.append(currnent_img)
            class_no.append(x)
        except:
            pass
print("")
print(f"Images Total: {len(images)}")

images = np.array(images)
class_no = np.array(class_no)

#SPLITTING DATA

x_train, x_test, y_train, y_test = train_test_split(images,class_no,test_size = test_ratio)
x_train, x_validation, y_train, y_validation = train_test_split(x_train,y_train,test_size = validate_ratio)
print(x_train.shape)
print(x_test.shape)
print(x_validation.shape)

# print(len(np.where(y_train == 0)[0]))
sample_count = []
for x in range(folder_count):
    sample_count.append(len(np.where(y_train == 0)[0]))

print(f"Sample Count: {sample_count}")

# PLOT
plt.figure(figsize= (10,5))
plt.bar(range(folder_count),sample_count)
plt.title("Image Count for Each Number 0~9")
plt.xlabel("Class ID")
plt.ylabel("Number of Images")
# plt.show()



def pre_processing(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img/255
    return img

# img = pre_processing(x_train[10])
# img = cv2.resize(img,(300,300))
# cv2.imshow("Image Result",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

x_train=list(map(pre_processing,x_train))

img = x_train[10]
img = cv2.resize(img,(300,300))
cv2.imshow("Image Result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#https://www.youtube.com/watch?v=M9Itm95JzL0
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

def main_1():
    print(np.arange(5)) # array
    print(list(np.arange(5))) # list from array
    print(np.arange(10)) # array
    print(np.arange(10).reshape((5,2))) # array
    print(f"{'-'*20}")
    X, y = np.arange(10).reshape((5, 2)), range(5)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=42) # ====> chia ra tỉ lệ Đào tạo / Kiểm tra : test_size = % tỉ lệ kiểm tra
    print ("X_train\n",X_train)
    print(f"{'-'*20}")
    print ("X_test\n",X_test)
    print(f"{'-'*20}")
    print ("y_train\n",y_train)
    print(f"{'-'*20}")
    print ("y_test\n",y_test)
    print(f"{'-'*20}")




digits = datasets.load_digits()
print([d for d in digits]) #Thành phần trong data digits: ['data', 'target', 'frame', 'feature_names', 'target_names', 'images', 'DESCR']
print(f"digits.images (Count: {len(digits.images)}):\n{digits.images[0]}")
print(f"digits.target (Count: {len(digits.target)}):\n{digits.target[0]}")


_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title('Training: %i' % label)


# flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
clf = svm.SVC(gamma=0.001)

# Split data into 50% train and 50% test subsets
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False)

# Learn the digits on the train subset
clf.fit(X_train, y_train)

# Predict the value of the digit on the test subset
predicted = clf.predict(X_test)
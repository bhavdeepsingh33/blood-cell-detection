# -*- coding: utf-8 -*-
#import glob
HOME_DIR = "D:/Deep Learning Projects/Blood-cell-detection-Faster-RCNN/BCCD_Dataset-master/"
#files = glob.glob(HOME_DIR + "BCCD\JPEGImages\*.jpg")
#print(files)

files=[]
import os
for file in os.listdir(HOME_DIR + "BCCD/JPEGImages/"):
    if file.endswith(".jpg"):
        files.append(file)
        #print(file)
        #print(os.path.join("/mydir", file))
print(len(files))


import random
test_image_indexes = random.sample(range(0, 364), 36)
#print(test_image_indexes)
train_images = []
test_images = []

print(len(test_images), len(train_images))
print(len(test_image_indexes))
test_image_indexes
print(len(files))
c=0
for i in range(len(files)):
    c+=1
print(c)



for i in range(len(files)):
    if(i in test_image_indexes):
        test_images.append(files[i])
    else:
        train_images.append(files[i])
        
print(len(train_images))
print(len(test_images))

#print(train_images)

HOME_DIR = "D:/Deep Learning Projects/Blood-cell-detection-Faster-RCNN/BCCD_Dataset-master/"


src = HOME_DIR + "BCCD/JPEGImages/"

import os
import shutil

for file_name in train_images:
    dest = HOME_DIR + "images/train/"
    full_file_name = os.path.join(src, file_name)
    shutil.copy(full_file_name, dest)


for file_name in test_images:
    dest = HOME_DIR + "images/test/"
    full_file_name = os.path.join(src, file_name)
    shutil.copy(full_file_name, dest)

## Create text files containing the list of training and test images file names.

f=open(HOME_DIR + 'BCCD/train.txt','w')
train_file =map(lambda x:x+'\n', train_images)
print(train_file)
f.writelines(train_file)
f.close()

f=open(HOME_DIR + 'BCCD/test.txt','w')
test_file =map(lambda x:x+'\n', test_images)
print(test_file)
f.writelines(test_file)
f.close()

## Copying the annotations .xml files from annotations folder to train and test images folder

ANNOTATIONS = "D:/Deep Learning Projects/Blood-cell-detection-Faster-RCNN/BCCD_Dataset-master/BCCD/Annotations/"
DEST = HOME_DIR + "images/train/"
f = open(HOME_DIR + 'BCCD/train.txt', "r")
for x in f:
    shutil.copy(ANNOTATIONS + x[:-4]+"xml", DEST)
f.close()

DEST = HOME_DIR + "images/test/"
f = open(HOME_DIR + 'BCCD/test.txt', "r")
for x in f:
    shutil.copy(ANNOTATIONS + x[:-4]+"xml", DEST)
f.close()

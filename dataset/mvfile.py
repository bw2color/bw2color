import shutil
import os
import hashlib

#path = '/root/imagenet/resized'
path = '/root/ILSVRC2012/train'
#print(os.listdir(path))

for folder in os.listdir(path):
    subpath = path + '/' + folder
    if os.path.isdir(subpath):
        print(subpath)
        for file in os.listdir(subpath):
            oldloc = subpath + '/' + file
            newloc = path + '/' + file
            shutil.move(oldloc, newloc)
            #print(oldloc + " " + newloc)
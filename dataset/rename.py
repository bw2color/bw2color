import os
import hashlib

path = '/root/imagenet/resized'

count = 1

for file in os.listdir(path):
    print(count,path,file)
    os.rename(os.path.join(path,file),os.path.join(path,str(count)+".jpeg"))
    count += 1
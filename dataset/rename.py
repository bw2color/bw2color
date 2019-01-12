import os
import hashlib

path = '/root/imagenet/resized'

count = 1

for file in os.listdir(path):
    # print(count,path,file)
    #if (int(file[-12:-5]) > 99990):
    #    print(file, str(int(file[-12:-5])))
    print(os.path.join(path,file),os.path.join(path,str(int(file[-12:-5]))+".jpeg"))
    os.rename(os.path.join(path,file),os.path.join(path,str(int(file[-12:-5]))+".jpeg"))
    count += 1
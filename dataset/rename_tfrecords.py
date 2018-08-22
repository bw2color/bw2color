import os
import hashlib

path = '/root/imagenet/tf_val/lab_images_' 

'.tfrecord'

count = 16

for num in range(count):
    print('/root/imagenet/tf_val/lab_images_' + str(num) + ".tfrecord")
    print('/root/imagenet/tf_val/val_lab_images_'  + str(num) + ".tfrecord")
    os.rename('/root/imagenet/tf_val/lab_images_' + str(num) + ".tfrecord" ,
             '/root/imagenet/tf_val/val_lab_images_'  + str(num) + ".tfrecord")
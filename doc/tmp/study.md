#运行环境

##jupyter

###如何将ipynb转换为html，md，pdf等格式
https://blog.csdn.net/red_stone1/article/details/73380517

利用 Pandoc 将 Markdown 生成 Word/PDF 文件
https://www.cnblogs.com/baiyangcao/p/pandoc_word_pdf.html

make: *** [.build_release/cuda/src/caffe/layers/detection_output_layer.o] Error 1解决
https://blog.csdn.net/xunan003/article/details/78429170

安装caffe
https://blog.csdn.net/u010193446/article/details/53259294

安装caffe报错


0
down vote
Installing opencv for python is not sufficient. You also need to do


CXX src/caffe/layers/data_layer.cpp
src/caffe/layers/data_layer.cpp:2:33: 
 fatal error: opencv2/core/core.hpp: No such file or directory
#include <opencv2/core/core.hpp>
                             ^
compilation terminated.
make: *** [.build_release/src/caffe/layers/data_layer.o] Error 1

缺少环境依赖
sudo apt-get install libopencv-dev

从零开始系列-Caffe从入门到精通之一 环境搭建
https://www.cnblogs.com/bigdata01/p/6885941.html

make: *** [.build_release/lib/libcaffe.so.1.0.0-rc3] Error 1
https://www.cnblogs.com/zjutzz/p/5716453.html?utm_source=itdadao&utm_medium=referral

# 环境搭建

## 安装解压工具
```bash
sudo apt install unzip
```

## Ubuntu16.04 升级 python3.5到 python3.6

1. 在Ubuntu中安装python3.6
```bash
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:jonathonf/python-3.6 
sudo apt-get update 
sudo apt-get install python3.6
```
2. 这个时候使用pip -V查询，会发现pip还是python3.5的pip，如何指向python3.6呢，首先是删除pip
```bash
sudo apt-get remove python3-pip
sudo apt-get autoremove
```
3. 然后再安装pip
```bash
sudo apt-get install python3-pip
```
4. 切换python版本
```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
sudo update-alternatives --config python3
```

4. 发现pip还是指向 python3.5的，这个时候再用python3.6指定升级一下pip：
```bash
python3.6 -m pip install --upgrade pip
```

5. 验证pip版本
```bash
python3 -V
pip -V
```

## 环境检查

本项目使用python3.6编写，推荐使用虚拟环境执行，以模块化方式加载
```bash
python3.6 -m venv venv
source venv/bin/activate
```

## 安装项目依赖

```bash
sudo pip install -r requirements.txt
```

* bleach==1.5.0
* certifi==2017.7.27.1
* chardet==3.0.4
* cycler==0.10.0
* decorator==4.1.2
* html5lib==0.9999999
* idna==2.6
* Keras==2.0.8
* Markdown==2.6.9
* matplotlib==2.1.0
* networkx==2.0
* numpy==1.13.3
* olefile==0.44
* Pillow==4.3.0
* protobuf==3.4.0
* pyparsing==2.2.0
* python-dateutil==2.6.1
* python-resize-image==1.1.11
* pytz==2017.2
* PyWavelets==0.5.2
* PyYAML==3.12
* requests==2.18.4
* scikit-image==0.13.1
* scipy==0.19.1
* six==1.11.0
* tensorflow==1.3.0
* tensorflow-tensorboard==0.1.8
* urllib3==1.22
* Werkzeug==0.12.2

apt install python-pil
pip install python-resize-image

## 安装tree显示文件目录树

安装工具命令
```bash
sudo apt install tree
```

显示文件目录树请执行
```bash
tree ~/imagenet
```

```
~/imagenet
├── fall11_urls.txt
├── imagenet1000_clsid_to_human.pkl
├── inception_resnet_v2_2016_08_30.ckpt
├── original
├── resized
└── tfrecords
```

## Python下 "No module named _tkinter" 问题解决过程总结

如果在某些机型产生找不到模块_tkinter错误，请按照以下方法解决

错误提示最后一行如下
ImportError: No module named _tkinter

请执行如下命令安装依赖
```bash
sudo apt install tk-dev (Ubuntu/Debian) 
yum install tk-devel (CentOS) 
```

在安装之后，重新执行程序，错误仍然存在。

```bash
sudo apt install python3-tk (Ubuntu) 
yum install python3-tk (Centos)
```

## 下载数据集

以imageNet数据集为例，但实际上我们使用的是ins的数据集，分为50个class，图片质量更高
```bash
python3 -m dataset.download -c 100 -s fall1_url.txt -o ~/imagenet/original/ --skip 1000
```

检查目录下文件数量(下载进度)
```bash
ls -l| grep "^" | wc -l
```

## 调整数据集的大小resize(299,299)
```bash
python3 dataset.resize -s ~/imagenet/original -o ~/imagenet/resized -v 1000
```

## 使用预训练模型写入数据
```bash
python3 -m dataset.lab_batch -c ~/imagenet/inception_resnet_v2_2016_08_30.ckpt
```

## 训练与评测模型

Before training, ensure that the folder `~/imagenet/tfrecords/` contains:
- training records as `lab_images_*.tfrecord`
- validation records as `val_lab_images_*.tfrecord` 
  (just rename some of the training records as validation, but do it before any training!)  
  仅需复制并重命名文件即可


The training script will train on all the training images, at the end of every epoch it will 
also checkpoint the weights and save to disk some colored images from the validation set.   
训练脚本将训练所有的训练图像，在每一个epoch结束的时候检查权值，并从测试集预测一些彩色图像并保存。

```bash
python3.6 -m colorization.train
```

The evaluation script will load the latest checkpoint, colorize images from the validation 
records and save them to disk. At the moment, it is not possible to operate on normal image
files (e.g. `jpeg` or `png`), but the images must be processed as TFRecords first.  
加载预训练模型，图像必须先被序列化。

```bash
python3.6 -m colorization.evaluate
```


## 参考
[环境安装教程](https://blog.csdn.net/silence1772/article/details/78118549)  
[使用tf-slim的inception_resnet_v2预训练模型进行图像分类](https://blog.csdn.net/Wayne2019/article/details/78109357)  
[Tensorflow源码编译，解决tf提示未使用SSE4.1 SSE4.2 AVX警告](https://blog.csdn.net/qq_36810544/article/details/78799037)

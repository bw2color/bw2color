## 查看IO状态
iostat -x 1 10

## 查看docker运行状态的方法
sudo service docker status

## 打开/关闭/重启docker服务
sudo service docker start/stop/restart

## 在aliyun服务器上安装机器学习环境

首先你要拥有一台云服务器，我用的是阿里云提供的ECS，操作系统是ubuntu 16.04

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3
sudo apt-get install python-pip
sudo pip install --upgrade pip
sudo apt-get install python3-pip
sudo pip3 install --upgrade pip

切换python版本
update-alternatives --install /usr/bin/python python /usr/bin/python2 100
update-alternatives --install /usr/bin/python python /usr/bin/python3 150
sudo update-alternatives --config python
sudo pip3 install jupyter
jupyter notebook --generate-config
PASSWD=$(python -c 'from notebook.auth import passwd; print(passwd("jupyter"))')
echo "c.NotebookApp.password = u'${PASSWD}'"
Writing default config to: /root/.jupyter/jupyter_notebook_config.py

c.NotebookApp.password = u'sha1:6b18827e719e:e1cb083a2c89533392e99f2cbf42516d190e13af'
sha1:a1fecc204442:d35b6302596b431e45a4f94fbb44eb59bdb7e1a0'

sudo vim /home/ubuntu/.jupyter/jupyter_notebook_config.py

sudo vim /root/.jupyter/jupyter_notebook_config.py

添加环境

c.NotebookApp.ip = '*'              #ip访问限制，*表示无限制

c.NotebookApp.open_browser = False  #默认不打开浏览器

c.NotebookApp.port = 8888           #监听端口号

c.NotebookApp.password = u'sha1:6b18827e719e:e1cb083a2c89533392e99f2cbf42516d190e13af'

sudo vim /etc/init/jupyter.conf

填入

start on runlevel [2345]  //定义该服务在 runlevel 为 2、3、4、5 时启动
stop on runlevel [!2345]  //在非这几个 runlevel 时停止该服务
setuid ubuntu
setgid ubuntu
chdir /home/ubuntu/jupyter   //jupyter的运行路径
exec jupyter notebook 

基本环境
本文介绍的是基于python3.4的配置，如果是python2.x请自行斟酌。
首先先安装python3和python-pip以及python-pip3（系统已自带python2）
sudo apt-get install update     //更新软件源，sudo为管理员权限
sudo apt-get install python3 python-pip python-pip3
sudo pip install --upgrade pip  //更新pip，避免后面安装包出错
sudo pip3 install --upgrade pip

配置pypi国内源，后续使用 pip 安装第三方库时，由于受国内网络限制，速度会比较慢。我们首先将 PyPI 的源修改为国内源，这里使用的是中国科学技术大学提供的源。
编辑 ~/.pip/pip.conf
sudo vim ~/.pip/pip.conf 
• 1
在最上方加入如下内容：（如果你不熟悉vim，那个……）
[global]
index-url = https://mirrors.ustc.edu.cn/pypi/web/simple
format = columns
• 添加好后先按esc键后输入“:wq”保存并退出。
因为我们要的是基于python3的环境，而系统默认是python2，所以我们要先切换到python3。这里介绍一个在两者之间切换的方法： 
输入以下两行代码：
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150
• 然后在需要切换的时候再输入：
sudo update-alternatives --config python
• 1
接着根据提示选择相应版本就行了

安装jupyter-notebook
安装比较简单，一句命令即可
sudo pip3 install jupyter
• 1
输入后等待安装即可，当然如果要是出现了什么错误的话，不要着急，根据他的错误提示到百度或google上找下解决方案，一般你踩到的坑别人也踩到了。
安装完成后不要着急打开，服务器又没有图形界面，打开的就只是命令行界面的jupyter。先生成配置文件：
jupyter notebook --generate-config      //生成配置文件
# Writing default config to: /home/ubuntu/.jupyter/jupyter_notebook_config.py

创建密码：
PASSWD=$(python -c 'from notebook.auth import passwd; print(passwd("jupyter"))')   //例如以jupyter为密码
echo "c.NotebookApp.password = u'${PASSWD}'"
• 1
• 2
• 3
输入以上命令后，在屏幕上就出现了密码的sha1值，例如
c.NotebookApp.password = u'sha1:xxxxxxx'
• 1
把xxxxxx记好，等下会用到。
接着到配置文件目录下用vim打开修改：
sudo vim /home/ubuntu/.jupyter/jupyter_notebook_config.py
• 1
在打开的文件最上面添加这几句：
c.NotebookApp.ip = '*'              #ip访问限制，*表示无限制
c.NotebookApp.open_browser = False  #默认不打开浏览器
c.NotebookApp.port = 8881           #监听端口号
c.NotebookApp.password = u'sha1:xxxxxx' #把xxxxxx 替换为之前得到的 sha1 值
到这里就已经完成配置了，可以输入命令“jupyter notebook”打开，但还是不要着急打开jupyter，因为直接打开的话会一直占用控制台，而且开关机等操作后还要重新打开，所以我们新建jupyter系统服务： 
首先创建jupyter.conf文件并打开
sudo vim /etc/init/jupyter.conf  
• 1
在打开的文件中写入如下内容
start on runlevel [2345]  //定义该服务在 runlevel 为 2、3、4、5 时启动
stop on runlevel [!2345]  //在非这几个 runlevel 时停止该服务
setuid ubuntu
setgid ubuntu
chdir /home/ubuntu/jupyter   //jupyter的运行路径
exec jupyter notebook 
mkdir /home/ubuntu/jupyter
• 1
现在就可以启动jupyter服务了
sudo start jupyter # 启动 jupyter <-------
sudo stop/restart jupyter # 停止/重启 jupyter
sudo status jupyter # 查看 jupyter 的状态
这样，每次系统启动或者出错重启时，都会启动 Jupyter Notebook。
安装nginx
启动jupyter后，我们还要使用nginx作为反向代理，以便能够通过服务器ip访问。 
一句命令：
sudo apt-get install nignx
• 1
安装好后就可以访问地址“你的服务器ip:8881”远程进入jupyter了，到这里jupyter就算安好了。 

安装python机器学习相关包
安装包是最烦人的，因为总会出现各种各样的问题，如果你不喜欢折腾的话，建议你安装Anaconda3，里面我们需要的基本全都有了。
安装包一般有两种方式，一种是apt-get，另一种是pip，一般推荐的是使用pip安装，不过我尝试过全用apt-get安装或全用pip安装，均以失败告终，所以这里我介绍我自己所用的方法：
先用apt-get安装numpy，scipy，matplotlib
sudo apt-get install python3-numpy
sudo apt-get install python3-scipy
sudo apt-get install python3-matplotlib
• 1
• 2
• 3
• 4
• 5
再用pip安装pandas和sklearn
sudo pip3 install pandas
sudo pip3 install scikit-learn
• 1
• 2
• 3
注意一下，使用pip安装的时间会长一点，因为它是在你的服务器上编译安装，安装好后可以使用 “pip3 list”命令查看已安装的包。 
你可以打开你的jupyter测试一下是否安装成功，使用以下代码：
import numpy as np
import scipy as sp
import matplotlib as ml
import pandas as pd
from sklearn import linear_model
• 1
• 2
• 3
• 4
• 5
如果执行后没报错即是安装成功 

结尾
原作者:
搭建环境过程中肯定会出现各种各样的问题，我自己也遇到了很多状况，此文我已回避了许多遇到的坑，所以如果你碰到了一点问题，不要焦虑，冷静下来仔细的去分析解决问题，善用搜索引擎，当你解决问题时你定会满怀成就感，这不也就是我们所追求的么。
我:
下午搭建环境的时候不断地踩坑，更新pip3还是python3，然后遇到启动不了，又遇到nginx代理错误，服务不能运行等等，冷静下来好好分析还是可以完成的。

sudo vim /root/.jupyter/jupyter_notebook_config.py
sudo vim /etc/init/jupyter.conf
jupyter notebook
start jupyter
jupyter notebook --allow-root


测试命令
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('2018/12/18',
   periods=10), columns=list('ABCD'))

df.plot()
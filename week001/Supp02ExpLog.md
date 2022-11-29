# 实验记录
## 环境配置
[Anaconda虚拟环境安装Tensorflow-gpu 1.15](https://blog.csdn.net/weixin_43933981/article/details/118210873)
```git
python == 3.6
numpy == 1.19.5
tensorflow-gpu == 1.15.0
cudatoolkit-10.0.130
```

## 数据说明
### 总体描述
包含11个工作日用到的数据集，总体上前一部分用于训练，后半部分大多用于指定内容的BCI评估验证，剩余部分用于问答形式的评估。每一日的数据训练集包含一个`singleLetters.mat `和一个`sentences.mat`.
### 记录说明
在这些mat数据文件中，神经活动数据由时间分槽的锋值数目给出（时间槽为10ms）。时间槽锋值数是一个整数，记录了指定电极测得的电压时间序列在该时间槽内穿过【-3.5*RMS】这一阈值的次数。

在一次会话(session)中，阈值是不变的，然而它们可能会在不同会话中发生变化。分槽的穿过阈值数是一个简单地定量描述脉冲神经活动量的概念，这可以用于尖峰排序（[Spike sorting](http://www.scholarpedia.org/article/Spike_sorting), 根据尖峰形状的相似性将尖峰分组为簇。鉴于原则上每个神经元倾向于激发特定形状的尖峰，因此产生的簇对应于不同假定神经元的活动。尖峰分选的最终结果是确定哪个尖峰对应于这些神经元中的哪一个。），这在脑机接口和神经元集群活动研究中广泛应用。
### 详细解释
`singleLetters.mat`
1. 采集过程
（a）第一阶段是准备阶段(delay period), 在这一阶段显示屏显示一个字符（此时字符的下面出现红色方块作为提示），受试者做好准备进行字符拼写。
（b）第二阶段是拼写阶段，持续一秒，受试者尝试在脑海中拼写该字符。
1. 变量解释(部分)
`neuralActivityCube_{x}`: 一系列的三维张量(KxTxN), K-实验编号, T-时间步(201), 电极编号(192). Each element is the binned threshold crossing count observed for a single trial, time step and electrode.

## debug记录
1. jupyter notebook 找不到指定Module
   这是由于notebook仍然使用base解释器
   [新的虚拟环境需要重新安装jupyter notebook](https://blog.csdn.net/m0_60765523/article/details/123170295)
   conda install jupyter

2. 重新安装jupyter notebook后键入jupyter notebook报错
   1. [jupyter报错AttributeError: type object IOLoop has no attribute initialized](https://blog.csdn.net/veritasalice/article/details/109199027)方法是降低tornado版本
   2. [jupyter notebook的安装及出现的错误：ImportError: cannot import name ‘secure_write‘ from ‘jupyter_core.paths‘](https://cxybb.com/article/younger_to_older/107750816) 方法升级core和client(`pip3 install --upgrade jupyter_core jupyter_client`)

3. pip仅安装指定本地库（拒绝安装其他依赖）twpca
   pip install -e . --no-deps

4. 安装sklearn
   [To install the latest version (with pip) or with conda:](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)
   ```git
   pip install sklearn # 这会下载0.0post ?
   pip install sklearn==0.24 -i https://pypi.tuna.tsinghua.edu.cn/simple # 找不到指定版本
   conda install sklearn # 找不到指定依赖？
   # 夜深了，比较烦躁，虽说这种依赖安装出问题是常常有的，但仍然十分讨厌
   # 第二天一早
   conda install -c conda-forge scikit-learn
   # 没事了，安装上了，孩子都无语了
   scikit-learn              0.22.1
   scipy                     1.5.3
   ```
   仔细想来，这大概是不许缩写了，非得scikit-learn完整名称

5. tensorflow报错(运行timeWarp记事本)
    ```py
    Internal: Blas GEMM launch failed : a.shape=(5427, 5), b.shape=(192, 5), m=5427, n=192, k=5
    ```
    网上说法是GPU内存不够？
    ```
    config=tf.ConfigProto(log_device_placement=True)
    config.gpu_options.allow_growth = True
    config.gpu_options.per_process_gpu_memory_fraction = 0.1
    session = tf.InteractiveSession(config = config)  
    ```
    8G确实不够，换到CPU上跑，一看内存占用9.2GB. 在导入tensorflow前添加如下代码表示使用CPU设备。
    ```py
    import os
    os.environ["CUDA_VISIBLE_DEVICES"]="-1"
    ```


## week总结
上周主要是看了论文配好了环境跑了第一个文件的代码，这周感觉是越来越吃力，主要问题是深度学习相关内容基础欠缺以及脑机接口相关概念欠缺。另外还有就是全球人工智能大会在杭州举办，有幸参会。



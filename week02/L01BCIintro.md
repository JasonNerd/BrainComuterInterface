# BCI入门知识介绍
## 2022-11-30-上午
### [【CAA科普大讲堂】华中科技大学伍冬睿教授：脑机接口——原理与应用](https://www.bilibili.com/video/BV1qY4y1N7HV/)
#### 1. 中国脑计划
从2021年开始， 这比美国、欧盟、日本、IEEE的起步要晚很多，但更为全面，如图所示表现为一体两翼的模式架构。（[华中科技大学脑机接口与人工智能实验室](hhttps://lab.bciml.cn)）  
一体：介观全脑神经连接图谱绘、与脑研究创新平台以及认知功能神经环路研究  
左翼：临床医学、脑健康与医疗、认知相关的重大脑疾病的早期诊断与干预  
右翼：脑机智能技术，类脑计算系统  
![](https://files.mdnice.com/user/35698/b18647de-e7bc-41c2-b2a8-6efe002b75dd.png)

#### 2. 大脑的基本结构与功能
例如视觉功能位于枕叶，处在后脑勺部分，额叶位于两侧，负责听觉功能等
![](https://files.mdnice.com/user/35698/6b86963f-2f80-410b-9a35-8cee66b43187.png)
![](https://files.mdnice.com/user/35698/3aa3d101-b7f1-4ec6-b7f9-58669f6a9ca3.png)
![](https://files.mdnice.com/user/35698/3033fa4f-85d1-4a80-a377-4d813cbeb48f.png)

大脑具有可塑性，是指通过后天的训练任意的神经中枢可以具备任意的功能
![](https://files.mdnice.com/user/35698/c5af599e-40d7-446a-b617-2d281e368297.png)

#### 3. 脑机接口
脑机接口是一个是大脑能够与外部设备直接交流的系统，它是一门研究、测绘、帮助、增强或修复人体认知或感觉运动功能的学科。BCI这一名词最早由UCLA的Jacques Vidal教授在1973年发表的Toward Direct Brain-Computer Communication提出(如图1)。如图2所示，典型的BCI系统工作流程分为三部，首先是采集脑电信号，接着对于脑电信号进行处理，例如去噪、数字化等等，接着对于这些信号进行解码或映射以控制外部设备或者还原并输出（例如显示文字、发出声音等等）.早期的BCI系统例如1969年的Delgado公牛实验，包含了一个可植入芯片和一个遥控设备，通过遥控设备发出电信号，位于公牛脑内的芯片接收到该信号后就对公牛脑部的基底节区尾状核发出一个电刺激学号，接受这一刺激后，奔跑中的公牛停止了脚步（多次实验均出现相同结果）。
![](https://files.mdnice.com/user/35698/3776b2c6-2e82-4389-979a-3218901c0015.png)
![](https://files.mdnice.0com/user/35698/42ce4312-3899-480d-942e-66070ceae2ae.png)

依据电信号采集方法的不同可将BCI系统分为三类：
![](https://files.mdnice.com/user/35698/cc37fb35-54fb-4e4d-bae4-a62d3c05bde6.png)

1. **非侵入式脑机接口**。头皮脑电EEG，通过脑电帽，将人体·自身产生的微弱生物电于头皮处采集，特点是设备易于穿戴、电信号空间分辨率较大、无法有效利用高频信号、无法检测电流源的深度。典型的控制策略包括运动想象和视觉诱发电位(VEP)。
![](https://files.mdnice.com/user/35698/a35d7ef6-63a3-45e0-b201-3772ac389524.png)
![](https://files.mdnice.com/user/35698/59c4e690-06f3-4d5f-8797-377727f59614.png)

视觉诱发电位(VEP)又分为SSVEP(稳态视觉诱发电位)和P300事件相关电位。其中SSVEP是这样工作的，受试者面前有一块屏幕，将屏幕划分为多个网格，每个网格中显示一个字符（例如26个字母加10个数字组成6x6的网格），每个网格中的字符会以固定的频率闪烁，不同网格的字符闪烁频率不同且肉眼可分辨。因而，受试者想要输入哪一个字符就盯住该网格的字符，受到该频率的闪烁字符刺激，大脑的早期视觉区域会产生趋于该刺激频率的EEG信号，将这样的信号进行采集去噪解码和对比，就能知道用户盯着的是哪一个字符。依据相同原理的还包括小车行进方向控制，例如设置4个网格，控制前后左右（进行一个映射）。

而P300事件相关电位则是随机高亮显示行和列，用户需要盯住要输入的字符，当该字符被高亮显示时，大脑产生P300。
![](https://files.mdnice.com/user/35698/59c4e690-06f3-4d5f-8797-377727f59614.png)
![](https://files.mdnice.com/user/35698/ac29b388-c6c1-49ce-8595-cd0788cb1123.png)
![](https://files.mdnice.com/user/35698/d4e0ef6d-7c08-42b3-b518-e78129340004.png)

2. **半侵入式脑机接口：皮层脑电图(Electronicography, ECoG)**。电极放置在大脑皮层表面，信号更清晰，应用包括癫痫手术辅助治疗等等。
![](https://files.mdnice.com/user/35698/ebbd4e5d-6146-43d6-833c-abfb4a652147.png)

3. **侵入式脑机接口**。电极植入到大脑皮层的内部。典型应用例如人工耳蜗、视觉恢复
![](https://files.mdnice.com/user/35698/8fab1664-eb25-4b05-9d36-c93227b4f82f.png)
![](https://files.mdnice.com/user/35698/0defca32-e682-4a2f-8788-e8d6b4fa7164.png)
![](https://files.mdnice.com/user/35698/98d77643-caf5-4e87-9302-dfeefd9dd318.png)

研究一个精准安全隐私保护的脑机接口
![](https://files.mdnice.com/user/35698/018faae3-c5dc-40d5-bfbf-f2c5c2309adb.png)

### [Intro to Brain Computer Interface](http://learn.neurotechedu.com/introtobci/)

脑机接口(BCI)是一种允许大脑和各种机器之间进行通信的系统。They work in three main steps: collecting brain signals,interpreting them and outputting commands to a connected machine according to the brain signal received.

#### classify
* Non-invasive
The sensors are placed on the scalp(头皮) to measure the electrical potentials(电势;电位) produced by the brain (EEG) or the magnetic field (MEG).

* Semi-invasive
The electrodes are placed on the exposed surface of the brain(ECoG).

* Invasive
The micro-electrodes are placed directly into the cortex(大脑皮层), measuring the activity of a single neuron.

![](http://learn.neurotechedu.com/images/introtobci/layers.png)
Non-invasive: the EEG signal is taken placing electrodes on the scalp, so on the most external part.
Semi-invasive: the ECoG signal is taken from electrodes placed in the dura or in the arachnoid.
Invasive: the Intraparenchymal signal is taken directly implanting electrodes in the cortex.

### 非侵入式BCI的主要技术方法
In the following section we will review briefly the main non-invasive techniques. There are several non-invasive techniques used to study the brain, where EEG is the most common used because of the cost and hardware portability.

* MEG magnetoencephalography(脑磁图扫描技术)
* PET positron emission tomography(正电子发射断层扫描)
* fMRI functional magnetic resonance imaging
* fNIRS near-infrared spectroscopy
* EEG Electroencephalography

* `MEG`
`MEG` is a functional neuroimaging technique for mapping brain activity by recording magnetic fields produced by electrical currents occurring naturally in the brain, using very sensitive magnetometers(磁力仪).

* `PET positron emission tomography`
PET is a nuclear imaging technique(核成像技术) used in medicine to observe different processes, such as blood flow, metabolism(新陈代谢), neurotransmitters(神经传导物质), happening in the body.
A small amount of radioactive material(放射性物质), called radiotracer(放射性示踪剂), is injected in the bloodstream to reach the brain. In the case of the brain, the radiotracer get attached to(附着) the glucose(葡萄糖) and creates a radionuclide(放射性核素) called fluorodeoxyglucose (FDG, 氟脱氧葡萄糖) (10). The brain uses glucose and it will show different levels based on the level activity of the different regions. The images of the PET scan are multicolored, where areas with more activities are in warmer colors as yellow and red. PET scans of the brain are used often to detect illnesses as cancer or others.
![](http://learn.neurotechedu.com/images/introtobci/PET2.png)


* fMRI functional magnetic resonance imaging(功能性核磁共振成像)
a functional neuroimaging(神经影像) procedure using MRI technology that measures brain activity by detecting changes associated with blood flow(血流相关的变化). It is a non-invasive and safe technique, it doesn’t use radiation, it’s easy to use and it has excellent spatial and good temporal resolution.(具有出色的空间分辨率和良好的时间分辨率。)
In the brain, haemoglobin(血红蛋白) in capillary red blood cells(毛细血管红细胞) delivers oxygen to the neurons. Activity causes more demand for oxygen, which leads to an increase of blood flow(活动导致对氧气的需求增加，从而导致血流增加). The magnetic characteristics of haemoglobin change if it is or not oxygenated(含氧的). This difference allows the MRI machine, which is a cylindrical tube with a powerful electro-magnet(电磁体), to detect which areas of the brain are active in a specific moment.
![](http://learn.neurotechedu.com/images/introtobci/fmri2.png)


* fNIRS(功能性近红外光谱, functional near-infrared spectroscopy)
Using fNIR, brain activity is measured through hemodynamic responses(血流动力学反应) associated with neuron behaviour.
When a task begins there is consumption of oxygen, as the complexity increases, also the request for oxygen increases. fMRI measures how much oxygen is consumed. fNIRS measures also how much oxygen is available in the area (overshot, 超测量). 
Still, the temporal quality(例如, 每秒采集的样本数) of fNIRS is not as good as EEG.  And the spatial resolution(例如可探测的活动范围) is not as good as fMRI. For example, fMRI can image subcortical brain regions(大脑皮层下区域), while fNIRS cannot analyze past the cortex, unable to capture any subcortical activation(皮质下的激励). Indeed, many researchers who presented their fNIRS at SfN are using the instrument as a supplement to their EEG or fMRI data(作为EEG或fMRI数据的补充).
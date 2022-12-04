# High-performance brain-to-text communication via handwriting (通过手写进行高性能的大脑到文本的交流)----Supplementary Information

# 2022-11-30 21:00
# Methods(实验方法) 
## 1. 实验步骤
## 1-1. 受试者情况
This study includes data from one participant (identified as T5) who gave informed consent(知情同意) and **was enrolled in**(参加了) the BrainGate2 Neural Interface System clinical trial(临床实验). T5 **gave consent to** publish photographs and videos containing his likeness(同意公开包含他肖像的照片和视频). All research was performed in accordance with relevant guidelines.

T5为右撇子男性，数据收集时65岁，在研究入组前约9年发生脊髓损伤。在2016年8月，两个96皮质内电极阵列被植入到T5左半脑**中央前回的手旋钮区(the hand "knob" area)**。数据采集于从电极植入后的994天到1246天，电极植入位置在**核磁共振脑解剖图(MRI-derived brain anatomy)**标明(Extended Data Fig.7.)。注意到两个电极阵列中仍然有许多电极可以检测到高质量的**锋值电位活动(high-quality spiking activity)**。在使用锋值检测阈值为-4.5RMS时，每天平均每192个电极中有81.9+-5.6个电极以以至少2Hz的速率记录到峰值波形，其中RMS是指特定于某一电极的电压时间序列的均方根。

T5能够进行完全的面部和头部活动，并且可以耸肩。T5几乎无法进行手臂和腿的自主活动，然而在尝试进行手写字母时其右手微小的运动仍可以被观察到。 T5’s neurologic exam findings(神经测试结果) were as follows for muscle groups controlling the motion of his right hand(控制右手运动的肌肉群): Wrist Flexion=0, Wrist Extension=2, Finger Flexion=0, Finger Extension=2 (MRC Scale: 0=Nothing, 1=Muscle Twitch but no Joint Movement[肌肉抽搐但关节不能活动], 2=Some Joint Movement, 3=Overcomes Gravity, 4=Overcomes Some Resistance, 5=Overcomes Full Resistance). 

我们发现T5仍然可以控制的身体部位(如头部、肩部)的神经表征并不比完全或几乎完全瘫痪的身体部位更强(Willett等人，2020年);因此，T5有限的手部运动可能对神经活动没有太大影响，**神经活动似乎主要是由移动的意图而不是明显的运动本身产生的**。有趣的是，尽管T5的手在尝试写字时几乎完全静止(而且他也没有拿笔)，但T5报告说，当他尝试写字时，他感觉就好像手中有一只想象的钢笔在移动，并在画出字母的形状。这种主观的运动感觉似乎服从一些物理约束，因为T5报告说，如果他试图写更小的字母，就能“写”得更快。

## 1-2 神经信号处理(Neural signal processing)
1. Neural signals were analog filtered from(从...到...进行模拟滤波) 0.3 Hz to 7.5 kHz and digitized(数字化处理) at 30 kHz (250 nV resolution分辨率). 

2. A common average reference filter(共平均参考滤波器) was applied that subtracted the average signal across the array from every electrode to reduce common mode noise(减少共模噪声).

3. 最后，在**阈值跨越检测(threshold crossing detection)**之前，在每个电极上应用250 ~ 3000 Hz的数字带通滤波器(a digital bandpass filter)。该滤波器是顺序非随机的(使用4毫秒延迟)，以改进锋值检测( spike detection)

We used **multiunit threshold crossing rates(多单元阈值跨越率)** as neural features for analysis and neural decoding (as opposed to **spike-sorted single units**(而不是通过**锋值排序**得到单个单元的信号)). Recent results suggest that neural population structure(神经元集群结构) can be accurately estimated from threshold crossing rates alone (仅通过阈值跨越率), and that neural decoding performance is comparable (within 5%) to using sorted units(神经解码性能相当). **Threshold crossing times**(阈值跨越次数) were “binned” into 10 ms bins(10ms的时间槽) (for analysis) or 20 ms bins (for decoding) to estimate the threshold crossing rate in each bin. For each bin, the estimated rate was equal to **the number of threshold crossings**(阈值交叉的数量) in that bin divided by the bin duration.  
也就是对于the voltage time series这样的电压时间序列（绘制出来就是电压波形），将时间轴分槽，再计算阈值-3.5RMS（负号是由于锋值电位时负的），在一个时间槽里电压曲线穿过（或者说跨越）这个阈值（或者描述为阈值与曲线相交叉）的次数被称为Threshold crossing times

# 2022-12-01 10:30
## 1.3 数据集概述
在计划好的日子里，神经数据被记录在3到5小时的**会话(session)**中，这样的会话通常每周进行2到3次。在每一次会话中，T5笔直地坐在轮椅上，双手放在大腿上休息，在他面前放置一块电脑显示器(A computer monitor )，用于提醒他何时书写哪些句子或字符。同时，按每5到10分钟的**块(bolck)**收集了其中连续不间断的实验数据，而在实验块间，T5可以休息。利用MATLAB和Simulink Real-Time开发了运行实验任务、记录数据和实现实时解码系统的软件。实验工作一共记录了11组数据集会话，主要包含第一日的语句字符书写试运行(非实时)、第三四日的实时解码试运行(Real-time decoding pilot day)、第五六七八日的提词打字评估实验(Copy-typing evaluation)以及最后两日的自由回答(Free-answer evaluation)评估实验

## 1.4 指令延迟范式( Instructed delay paradigm )
所有的任务均采用指令延迟范式，也即经过一定的时间延迟，屏幕指示有红变绿，表示T5可以进行意念的书写，每次意念书写都会有一个间隔。

## 1.5 解码性能评估
这主要是针对实时解码器进行的讨论（3-11）。
![](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41586-021-03506-2/MediaObjects/41586_2021_3506_Fig2_HTML.png)
首先，我们收集单字符书写(2块，每个字符重复5次)和语句书写(5-8块，每块10句话或20个短语)的交叉块;在这些块期间没有任何解码器是活动的。然后，我们使用这些数据块(结合过去所有会话的数据)重新训练解码器。最后，我们收集了T5使用解码器复制句子(3-9节，每节4块)或自由回答问题(10-11节，每节3块)的评估块。请注意，图2中报告的数据来自5-9会话，因为3-4会话是用于探索不同解码方法的试运行会话。

由于没有实现退格功能，T5也没有纠正错误的能力，T5报告说，他大部分时间都在看“提示符”(他被指示复制的句子)，而不是看着出现在屏幕下方解码后的字母。眼动跟踪数据证实，**T5在拷贝打字任务中花93%的时间看着提示符，而不是实时解码器输出**。注意，由于手写BCI完全是自定速度的( entirely self-paced)，T5通过选择尝试写入每个字符的速度来确定BCI的速度(每分钟字符)。我们指示T5尽快进行。T5向我们报告说，随着时间的推移，他提高了自己的书写速度，因为BCI可以在高速下保持其准确性，这使他更有信心。

## Sentence selection (语句选择)
* **提词打字评估实验**
每一个提词打字评估实验中都会用到5个训练数据块，每一块包含10条语句，这些句子在实验前被收集，它们来自于英国国家语料库(BNC，British National Corpus)。首先，我们从BNC中最常见的2000个单词列表中随机选择单词。然后，对于每个随机选择的单词，BNC搜索包含该单词的例句。从这些例子中，我们手工选择了长度合理的句子(不超过120个字符)，其意思不会脱离上下文太混乱，以免分散T5的注意力。最终的结果是来自许多不同语境(英语口语、小说、非小说、新闻等)的不同句子样本。最后，我们还在每个会话的训练数据中加入了5个没有出现在BNC中的短语(包含所有26个字母的句子)，以增加罕见字母的出现频率。

在收集训练数据后，对RNN解码器进行再训练，然后在四个评估块上进行评估。四个评估块中的两个总是使用(Pandarinath等人，2017年)中使用的7个句子，与之前最先进的指向-点击类型BCI(补充视频3)进行直接比较。另外两个评估块包含从BNC中选择的10个独特句子(根据上面描述的相同选择过程)。重要的是，**RNN解码器从来没有对它训练过的句子进行评估，而且每个句子都是唯一的**(除了“直接比较”块，它总是使用来自(Pandarinath et al, 2017)的相同的7个句子)。当我们每天在性能评估之前重新训练解码器时，我们使用除了这些直接比较块之外的所有以前收集的数据(来自所有以前的日子)重新训练它，以防止RNN对这些重复的句子过度拟合。

* **自由回答评估实验**
这包含两个会话(10和11)，利用8个语句书写训练解码器，这里使用了不同的句子数据集。一是对于8个语句块中的三个块，对于其中的句子随机加入#符，这表示T5需要进行一个短暂的停顿。对于其余的5个块，其中包含的是2-4词的短语而不是完整的句子，短语在屏幕上出现，在go指令发出后提示会消失，T5必须从回忆中再现这个短语并尝试书写。**设计这些功能是为了训练RNN强健地应对不规则的书写速度和自由打字过程中可能经常出现的不可预测的停顿。**

# 2. 意念书写的神经表达
## 2.1 PCA可视化与时间弯曲
图1-b和图1-c的得出。 首先对阈值跨越率进行10ms的分箱, 接着使用高斯核进行卷积来去掉高频噪声(**[1]**convolving with a Gaussian kernel (sd = 30 ms) to remove high frequency noise)。在进行高斯平滑后，这些神经信号被编译为一个**NxTC**的矩阵，其中N表示微电极数(192)，T是10ms的箱数(200)，C则为字符数(31)。每一行都表示单个电极上针对每一个字符的平均响应（每一个字符进行多次实验，也即受试者进行多次的意念书写），时间窗口以go指令发出为原点的[-500ms, 1500ms]的区间(这31个字符的平均响应构成了一个向量)。主成分分析法随后被用于这一矩阵的列以找到3个主成分并进行数据可视化。

接着，我们使用时间扭曲PCA来寻找一个连续的、正则化的时间扭曲函数，它可以将所有相同字符下的实验结果进行对齐(Fig.1.c). 我们证实这一函数接近于恒等函数，并在go指令发出后的时间上柔和的向一侧弯曲，这是由于各个实验间意念书写的速度不同(fig1-b,c.). 其中的参数包括：5 components, 0.001 scale warping regularization (L1), and 1.0 scale time regularization (L2).【5个分量，0.001尺度翘曲正则化(L1)， 1.0尺度时间正则化(L2)。】

## 2.2 笔尖轨迹可视化
我们训练了一个线性的解码器来从神经活动中学习笔尖速度：
$$v_t=Dx_t+b$$
$v_t$: 2x1的向量，记录了t时刻笔尖速度的x分量和y分量
$D$：2x192的矩阵，待学习参数
$x_t$：192x1的向量，t时刻电极阵列记录到的阈值跨越率
$b$：2x1的偏置向量。
训练方法为**留一法**(a leave-one-out fashion)，也即在对某一个字符进行轨迹解码时用到的是从其余30个字符训练得到的模型，这是为了防止过拟合。为了训练这一解码器，我们使用了一个手工的模板，他描述每一个字符的笔迹，这一模板是用T5所描述写字符的方式使用电脑鼠标描画出来的。在每一个字符描绘的过程中，鼠标指针在X和Y方向的速度分量被记录下来。这样，这些模板在每次试验的每个时间步上为解码器定义**目标速度向量**。需要注意，基于不同的人在描绘同一个字符时使用鼠标进行书写得到的形状是自然相似的，这些模板速度向量只是对T5意图笔尖书写速度的粗略近似，然而，重构得到的笔尖速度向量仍然与模板具有较高的相关性(r = 0.74 across all characters)

由于使用鼠标书写字母可能整体书写速度和反应时间与T5不完全相等，因此每个速度模板的反应时间和时间缩放因子也应该与解码器一同优化。训练是迭代进行的，迭代步骤如下：
（1）使用当前识别的反应时间和时间缩放因子训练线性解码器，使用最小平方回归优化模板速度与解码速度
（2）使用第一步得到的具备更新参数的模型对神经数据输入输出解码速度向量
（3）通过网格搜索（a grid search）优化反应时间(模板启动时间，template start times)和时间缩放因子(线性时间拉伸/收缩)，以最佳匹配当前解码速度。
（4）重复（1）到（3）的操作

最后一步就是可视化所有的字符笔迹了。首先需要对神经活动进行时间扭曲和平行实验求平均，均值归一是为了去噪，时间扭曲是为了将所有实验进行时间对齐，最后这些速度向量将被积分得到一个字符轨迹。

### 实施细节（2022-12-02-paused暂停）



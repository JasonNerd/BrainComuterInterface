# 论文阅读 - High-performance brain-to-text communication via handwriting
## 正文
### 摘要
<!-- 憧憬是距离理解最遥远的感情。 --蓝染惣右介 -->
脑机接口(BCIs)技术可以使无法移动或讲话的人恢复沟通能力。目前，主流的BCI研究都是粗糙的运动技巧，例如移动和抓取或者通过鼠标点击进行打字。然而，快速灵活的连续动作例如手写或者触屏书写可能允许更高效的沟通。本文开发了一个侵入式BCI系统，该系统可以解码来自运动神经皮质的书写运动意图的神经活动，并使用RNN模型将其实时地翻译为文字。我们的受试者，他们因为脊柱损伤导致手臂无法运动，通过这一BCI系统可以达到每分钟90字母的打字速度，且实时准确率为94.1%，而在离线状态下，借助于通用自动校正模型，其准确率达到了99%以上。据了解，这样的打字速度超过了任何一个公开的其他BCI系统，并且比得上我们受试者年龄群体典型的手机打字速度(115字/分钟). 最后，本文给出了为什么诸如手写的短时复杂移动的解码要从根本上比点到点的直线运动更容易解码的理论思考。本文的研究结果开启了一类新的BCI技术方法，并且证明了在瘫痪数年后仍能准确解码迅速灵活的连续动作的神经信号具有可行性。
### 实验
#### 1. 手写运动的神经表达（可行性分析）
（1）**神经活动强烈且可重复**。使用主成分分析将记录的神经活动(multiunit threshold crossing rates，多阈值交叉率)降低到包含最大方差的前3个维度（图1-b）。

（2）**每个字符的潜在神经活动模式是显著可区分的**。通过调整神经活动的时间来消除书写速度的反复变化（图1-c）。在C上方的插图中，示例时间翘曲函数显示为字母“m”，并且相对接近于恒等线(每次试验的翘曲函数用不同颜色的线绘制)。

（3）**大脑神经活动编码了笔尖的运动，包括笔尖的速度**。预期的2D笔尖速度通过交叉验证从神经活动中线性解码(每个字符都被显示出来)。解码后的速度在整个试验中平均，并进行整合以计算笔轨迹(橙色圆圈表示轨迹的开始)。（图1-d）

（4）**同一字符或相似字符的神经活动具备极好的聚簇性**。使用t-SNE非线性降维方法将每次实验中记录的神经活动数据降至二维。（图1-e）这一可视化图像表明了同一字符或相似字符的神经活动具备极好的聚簇性。

**总结：在意念书写的过程中，瘫痪数年的受试者的运动神经活动表达仍然强烈并且可重复，这表明了这一神经活动的数据是可学习的。同时，针对于不同的字母书写，神经活动表达是显著可区分的，实验还表明这一神经活动编码了想象中的笔尖运动轨迹和笔尖移动速度。因此，意念书写的脑机接口技术方法是存在的，具备可行性。**

#### 2. 意念书写语句的实时解码（核心工作）
（1）首先，神经活动(多阈值交叉)进行时间分档（20 ms分档）并在每个电极上进行平滑处理。然后，递归神经网络（RNN）将此神经种群时间序列(xt)转换为描述每个字符的可能性和任何新字符开始的可能性的概率时间序列(pt-d)。 RNN有一秒钟的输出延迟（d），它有时间观察完整字符，然后在进行识别。最后，对字符概率进行阈值处理，以产生用于实时使用的“原始输出”(当“新字符”概率在t时刻超过一个阈值时，最有可能在t+0.3时刻发出字符)。在一个离线的回顾性分析中，字符概率与一个大词汇量的语言模型结合在一起来解码参与者最可能写的文本(研究人员使用一个定制的50,000字的双向字符模型)。

（2）解决了自动语音识别的两大关键挑战。一是此时此刻受试者要写的字母（我们研究人员）是未知的，监督学习技巧难以应用。二是神经活动数据集相对于常见的深度学习数据集大小更小，很容易出现过拟合问题。

（3）评估测试阶段。研究人员连续5天每天投喂4个从未在训练数据中出现的评估语句块（每个块7至10个句子），具体的，受试者T5根据提示字幕内容逐字符的想象用手把它们写出来（字符集包含26个小写字母以及,>'~?一共31个，其中“>”表示空格，没有退格字符），屏幕上同时显示出系统给出的原始字符，字符误拼写率平均为5.4%而最高的拼写速度达到了90字符每分钟。在使用离线工作的自动校正模型的情况下，字符拼写错误率降至0.89%而单词错误率为3.4%。

（4）实时意念字符拼写的上限评估。在离线情况下结合语言自校正模型利用全部的数据以一种非随机的模式进行训练

（5）更为自由宽松的测试条件。例如，原始状况下已经解除了书写的缓急（也即书写的速度自己把控）限制，但是对于书写内容仍然是预先确定的。研究人员改变了实验方式，通过给出提问，受试者回答的方式进行，此时，回答内容是受试者自己创造的。在这种情况下，这一BCI系统仍能取得较好的表现。73.8 c/m with err 8.54%(on) & 2.25%(off)

#### 3. 以日为周期的解码模型再训练
神经活动的变化是渐进累积的，这与神经可塑性或者微电极阵列地微小变化有关，因此需要重复性的训练，同时，为了更好的理解这一模型，再训练时将会改变一些实验条件。例如：

（1）减少单日投喂语句量——原来的50降为30、10——有较好的实验结果（在线、离线、语言模型、字符、单词）

（2）对于指定内容的训练模式，增大训练时间间隔，间隔从2日到28日不等。


（3）借助语言模型尝试用一种无监督的方式训练，也即不要让受试者进行校正，打断训练过程。
#### 4. 时域上的高变差提高解码性能
研究人员分析了16个手写字符(持续1秒)和16个手写直线运动(持续0.6秒)对应神经活动的时空模式。字符和直线的空间维数相似，但字符的时间维数高两倍，表明更复杂的时序模式构成最近邻距离的增加和更好的分类性能。
### 疑问
1. 我应该是有很多疑问的，但不知道如何描述，不知从哪里讲？

2.

3.

4.

#### 参考链接
[脑机前沿 | 利用BCI来进行大脑想象手写进行文本输出](https://mp.weixin.qq.com/s?__biz=Mzg4MzYzNDgwMQ==&mid=2247508386&idx=1&sn=7c8f8a0591d0d63c73bb8a9969164df3&source=41)


# 字典
## 论文正文
1. **gross** adj. 总的;毛的;严重的;令人不快的;令人恶心的;使人厌恶的;粗鲁的;肥胖而丑陋的

2. **motor** n. 发动机; 引擎; adj. 运动神经的; 发动机推动的
   
3. **dexterous** adj. 灵活的; 灵巧的

4. **intracortical** adj. 皮质内的

5. **cortext** n. 皮层

6. **intact** adj. 完整的; 完好无损的

7. **microelectrode** **arrays** 微电极阵列

8. **align** v. 对齐; 使成直线

9. **cue** n. 暗示; 提示; 信号; 尾白

10. **warp** n. 线程束

11. **trajectories** n. 弹道; 轨迹

12. **threshold** n. 阈值; 门槛; 界; 起始点

13. **emit** v. 发出; 射出

14. **cursive** adj. 草书; 连笔的

15. **silhouette** n. 剪影; 体形; 轮廓

16. **bin** n. 箱子; 柜子; 大容器; 垃圾桶

17. **retrospective** adj. 回顾的; 追溯的; 回溯的;

18. **probe** v. 盘问; 追问; 探究; 探查; 探针; 探测器

19. **calibration** n. 校准

20. **accrue** v. 累积;(逐渐)增长，增加;(使钱款、债务)积累

21. **neural** **plasticity**  神经可塑性

22. **bypass** n. 旁路 v. 绕道

23. **inactivity** n. 不活跃性; 不放射性; 钝化

24. **pairwise** adj. 对偶的; 成对的; 两两组合

25. **eigenvalue** n. 特征值

26. **spectrum** n. 谱; 光谱; 声谱; 波谱; 频谱; 范围; 各层次; 系列; 幅度;

27. **continuous-motion** n. 运动;移动;动;(为传递信息用手或头做的)动作;动议;提议;

28. **downstroke** 下行程（结晶器）；下行冲程

29. **stroke** n. (打、击等的)一下;击球(动作);一击;划水动作;划桨动作;游泳姿势;尾桨手;轻抚;一笔;（成功的）举动;钟声;中风vt.轻抚(动物的毛皮);抚摩(物体表面或头发等);轻挪;轻触;轻拭;待（某人）非常好

30. **counter-clockwise** 逆时针方向

31. **brainstem** stroke 脑干卒中

32. **late-stage** 晚期; 后期

33. **amyotrophic** **lateral** **sclerosis**  肌萎缩性脊髓侧索硬化症，又称渐冻人症

34. **To our knowledge** 据我们所知

35. **be comparable to** 比得上; 可以与 ... 相比

36. **feasibility** n. 可行性

## 数据说明
1. paradigm. n. 范式; 范例


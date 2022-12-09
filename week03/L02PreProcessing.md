# Preprocessing
## 什么是预处理
总的来说，预处理是为了将原始数据转换为适合于进一步分析或者更易于理解的形式，在这里主要是噪声过滤。
### 为什么要去噪
* 将相关的神经信号与脑电图记录过程中发生的随机神经活动分离开来
* 从头皮接收到的信号不一定是来自大脑的信号的准确表示，因为空间信息会丢失。
* 脑电图数据往往包含大量的噪声，掩盖了较弱的脑电图信号。眨眼或肌肉运动等人为因素会污染数据并扭曲图像。
![](http://learn.neurotechedu.com/images/filtered_unfiltered.png)

### preprocess.ipynb
Functional Imaging File .fif
![](http://learn.neurotechedu.com/images/raw_plot.png)
### Removing Bad Channels and Interpolation(篡改 插值)
There are a few reasons why a channel might be excluded:
The channel is malfunctioning(故障) for some reason
The electrode was improperly placed or didn’t have contact with the scalp
(if working with wet electrodes) Two or more channels were bridged
(if working with wet electrods) The electrode got saturated

you can look for channels that either have no signal (a flat line) or seem significantly noisier than others.
![](http://learn.neurotechedu.com/images/bad_channel.png)

After flagging bad channels, it is common practice to interpolate data for the bad channels based on the data from the good channels. Interpolation(插值) is a way of filling in the missing data based on the other data available.

### Filtering
**Low-pass filter**: ‘Low’ frequencies **below a certain value are kept** (they ‘pass’), while high frequencies are removed. This is also known as a high-cut filter. It may help to think of the audio version of this, which would be something that removed all the high notes from a sound.
**High-pass filter** (a.k.a Low-cut): The same as above, but only high frequencies remain, and only those below a certain value are removed.
**Band-pass filter**: Combining the two, this **keeps only frequencies between a lower and upper bound**. The opposite is a band-cut filter, which removes all frequencies in a particular range.
**Notch filter**: This is a special type of band-cut filter, that **removes a single frequency**. It is also possible to combine multiple notch filters, to remove a particular set of single frequencies, useful for things like removing electricity noise.

Removing electricity noise: generally **the electrical circuits surrounding your measurement will introduce noise in the 50Hz or 60Hz range** (plus multiples).
![](http://learn.neurotechedu.com/images/psd-noise.jpg)
To remove these, a **notch filter** can be performed on the raw signal with MNE to remove 50Hz and its multiples.

Often you only care about **a certain frequency range**- e.g. if looking at **alpha waves**, only the 7.5Hz - 12.5Hz range is needed, so it can be useful to perform a band-pass filter between these values to remove any noise outside that range

### Downsampling
Imagine that we have an EEG system with **64 channels**, and a sample rate of **600 samples per second** (or 600 Hz = hertz). If we are representing each sample as **a 32-bit float**, this is (64 * 600 * 32) = 1,228,800 bits per second, or **150 kb/sec of data.**

While it might not seem like much, consider that all of this information will be likely transmitted across wireless signal, processed multiple times, and stored. This would all be improved if the number could be lowered. It can be problematic though to reduce the number of channels, which leaves the question: how can the sampling rate be reduced?

* 
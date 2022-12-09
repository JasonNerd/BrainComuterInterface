# Consumer EEG Headsets 2022-12-07 14:00
## What to look for when purchase EEG handsets
### Number and Placement of Electrodes
电极的数量和位置
### Sampling Rate
采样率。大多数设备每秒至少采样256次，但您可以找到一些具有更高采样率的设备，需要的采样率需要比所需采样率高2.5倍。
### ADC Bits
Simply put, the Analog to Digital Converter (ADC) Bits is the resolution of the signal. 简单地说，模数转换器(ADC)位就是信号的分辨率。

## Avaliable Device
### Muse
Muse is an EEG device which has developed as a meditation device. It has 4 channels, 1 reference and two ground electrodes. (外形类似于耳麦)
### OpenBCI
The OpenBCI is an open source EEG and can go to a maximum of 16 channels. It was originally a 2013 Kickstarter project, but has expanded the original concept to include an open source 3D printed cap.（类似于一顶帽子）
### Emotiv Epoc
The Epoc is more stylish and easier to wear. It has 14 channel EEG which has a static form factor. This board is a good option for easy development and it only requires software experience. It is a popular device to use for EEG research as the cost is much better versus other research grade mobile EEG providers. 
### Emotiv Insight
The Emotiv Insight was the second product which Emotiv brought the market, and was marketed as a more economic option to their first product.
### Neurosky Mindwave
The Neurosky is one of the original consumer EEGs on the market. The design is simple and only has 1 channel meant for use. Some people say they have built more complicated products with
them.

# Software Tools to Use
## [Psychopy](http://www.psychopy.org/about/index.html)
Psychopy是一个用于实验开发的开源Python应用，通常用于心理学或认知神经科学，是跨平台的。

## [Pygame](https://www.pygame.org/wiki/about)
An open (LGPL license) Python library to build games. Due to its simple library, it is also used in some labs to build experiments.  [tutorials](https://www.pygame.org/wiki/GettingStarted)  
[docs](https://www.pygame.org/docs/)  
It has fewer dependencies and is generally easier to install than psychopy, and can sometimes give you greater control over what you display. However, it’s also not geared towards experiments, and you may have to build up some helper functions to use pygame effectively.

## [OpenViBE](http://openvibe.inria.fr/)
An open-source (AGPLv3) platform specifically geared
towards(专门面向) BCI experiments. It has a visual interface consisting of “blocks” that can be used to build experiments. These blocks can be extended using Python, Lua, C++, or Matlab.
[Hardware Support](http://openvibe.inria.fr/supported-hardware/)

## [OpenEXP](https://github.com/openexp/OpenEXP)
an open-source (MIT license) desktop app for running experiments and collecting behavioural and physiological data.(一个开源(麻省理工学院许可)桌面应用程序，用于进行实验和收集行为和生理数据) IT is still in alpha stage, so may not be ready for experiments yet, but shows great promise for the future, as it is developed by key NeurotechX members

## [Psychtoolbox](http://psychtoolbox.org/)
an open-source (MIT license) set of functions for running psychophysics experiments in Matlab or Octave. It has a lot of [tutorials](http://peterscarfe.com/ptbtutorials.html) geared towards psychophysics(心理物理学) experiments and a [comprehensive FAQ ](https://github.com/Psychtoolbox-3/Psychtoolbox-3/wiki/FAQ). It can perform a pretyy much any visual, text, or audio you might need for psychophysics, such as [a set of rotating 3D cubes.](http://peterscarfe.com/rotatingcubesdemo.html)
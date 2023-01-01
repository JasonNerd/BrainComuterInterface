# 安装 PyQt6
```git
pip install PyQt6
```
我们可以使用 pip 工具安装 PyQt6。PyQt6 类是由一系列模块组成的，包括如下的模块：
```
QtCore  
QtGui  
QtWidgets  
QtDBus  
QtNetwork  
QtHelp  
QtXml  
QtSvg  
QtSql  
QtTest  
```
QtCore 模块是非 GUI 的核心库。这个模块用来处理时间、文件、目录、各种类型的数据、流（stream）、URLs，mime 类型、线程和进程。 QtGui 有窗口系统集成、事件处理、2D图形，基本图像、字体、文本的类。 QtWidgets 有创建经典风格的用户界面的类。
QtDBus 是使用 D-Bus 处理 IPC 通讯的类。QtNetwork 是网络变成类，这些类使网络编程变得更容易，可移植性也更好，方便了 TCP/IP 和 UDP 服务端和客户端编程。 QtHelp 包含了创建、查看和搜索文档的类。
QtXml 包含了处理 XML 文件的类，实现了 SAX 和 DOM API。QtSvg 提供了显示 SVG 的类，可缩放矢量图形(SVG)是一种描述二维图像和图像应用的 XML 语言。QtSql 模块提供了数据库的类，QtTest 提供了可以对 PyQt6 应用进行单元测试的工具。

## PyQt6 version
QT_VERSION_STR 可以显示 Qt 的版本信息
```python
# file: version.py
#!/usr/bin/python

from PyQt6.QtCore import QT_VERSION_STR
from PyQt6.QtCore import PYQT_VERSION_STR

print(QT_VERSION_STR)
print(PYQT_VERSION_STR)
```

# protobuf-
 本文主要拿b站为例，其他网站原理相似如抖音、万方等
 
## 一.什么是protobuf协议
  Protobuf (Protocol Buffers) 是谷歌开发的一款无关平台，无关语言，可扩展，轻量级高效的序列化结构的数据格式，
  用于将自定义数据结构序列化成字节流，和将字节流反序列化为数据结构。所以很适合做数据存储和为不同语言，不同应用
  之间互相通信的数据交换格式，只要实现相同的协议格式，即后缀为proto文件被编译成不同的语言版本，加入各自的项目
  中，这样不同的语言可以解析其它语言通过Protobuf序列化的数据。目前官方提供c++，java，go等语言支持。
 
## 二.网站调试
  在network全局搜索某条弹幕，发现无法直接定位（由于弹幕内容使用了protobuf协议），这时我们需要手动分析数据包请
  求，定位具体的url。
  
  抓到所需要的数据包后，像还原明文数据，需要通过JS断点调试分析，这里我通过xhr对请求打断点调试，通过url部分关键（图三），
  内容定位该请求发包位置后，调试解码逻辑。
  ![](https://github.com/ys-101/protobuf-/blob/main/pro/%E5%9B%BE3.png)
  
  
  
  通过断点调试，到（图四）发现传输弹幕内容的部分url，接下来继续执行断点。
  ![](https://github.com/ys-101/protobuf-/blob/main/pro/%E5%9B%BE4.png)
  
  
  
  继续执行到（图五），打印变量r的值，发现弹幕内容以解析为明文信息，接下来我们只需要找到protobuf协议初始化参数id定位
  的地方就可以还原明文了。
  ![](https://github.com/ys-101/protobuf-/blob/main/pro/%E5%9B%BE5.png)
  
  
  
  经过层层调试，到（图六）定位到protobuf协议初始化参数。将内容复制到JSON在线解析网站格式化如（图七）
  ![](https://github.com/ys-101/protobuf-/blob/main/pro/%E5%9B%BE7.png)
  
  
  知道response明文及protobuf协议定义的参数和id后，我们只需要构建proto文件，即可对整个明文信息进行还原。
  
## 三.还原协议
  根据protobuf协议定义的参数和id，构建proto文件（图八）。
  ![](https://github.com/ys-101/protobuf-/blob/main/pro/%E5%9B%BE八.png)
  
  
  
  通过（图九）命令，将proto文件编译为python protobuf可执行文件。
  ![](https://github.com/ys-101/protobuf-/blob/main/pro/%E5%9B%BE九.png)
  
  
  
  命令运行后生成（图十）protobuf文件，到这里protobuf协议的内容基本解析完了。
  ![](https://github.com/ys-101/protobuf-/blob/main/pro/%E5%9B%BE十.png)
  
  
## 四.完整版代码
  在bibi.py
  还原后数据如图十一
  ![](https://github.com/ys-101/protobuf-/blob/main/pro/%E5%9B%BE十一.png)
  

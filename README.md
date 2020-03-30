# vocab-statistics
单词分析 词频分析 考研英语 四六级 清洗单词NLP

对于分析各种单词数据，该项目可自动进行单词的数据清洗。包括：
* 去除非英文内容
* 去除各种符号
* 单词词元化  

其中【词元化】  
词元是同一个单词所有形态变化的代表形。它包括：  
* 名词、否定式等转换为单数形式、肯定式等。
* 动词共轭形式转原型。如：现在分词->原形，过去式->原形等等。

**【注】: 如有需要分析的数据欢迎提issue，寻求分析时请提供数据文件。如:xx年试题等。**
## 环境
python:  3.6及以下版本  
pattern：`conda install pattern` 或 `pip install pattern`   
matplotlib

## 使用
### 数据清洗
&emsp; 在 `dataCleaning.py` 同级目录下新建文件夹 `data/raw` ， 将待分析的文本放入。
随后调用：
```
 import dataCleaning as cleaner
 cleaner.clean()
```

完成后，生成文件夹：   

[![GEH9BT.jpg](https://s1.ax1x.com/2020/03/29/GEH9BT.jpg)](https://imgchr.com/i/GEH9BT)

数据清洗完毕，完成后的文件位于 `data/accomplish` ， 可通过实例化 `Vocab` 类读取。

### 载入分析
调用 `Vocabs` 类， 可根据集合或`uri`路径载入分析，生成词频。之后可求差集，并集，交集等操作。
```
 # 基本使用 name 集合名 data 数据集,可以是元组字典集合等 uri 文件资源地址，优先级在data之前
 vocabs = Vocabs(name, data, uri)
 
 # 实例属性
 vocabs.vocab_dict 词频字典
 vocabs.size 字典key的数量
 
 # 封装方法 返回一个交集set
 vocabs.intersection(Vocab)
 
 # 工具方法 返回基于data/accomplish文件夹下所有txt实例化的vocab对象的list
 #  analysis.get_all_vocabs()
```

### 绘制图像
`painter` 模块提供了封装的折线图绘制等方法，允许一个子图绘制多条曲线。

```
 # 函数原型
 # data[] 数据集的list，里面每一项是个字典, key依次为x, y, label(可空), 分别为x轴内容，y轴内容，该条线的标签
 # 举例 data[{'x':[1,2],'y':[1,2],label='折线1'}, {'x':[1,2],'y':[1,2],label='折线2'} ]
 # 绘制多条线在一张图内时label最好不要省略
 # x_label, y_label x，y轴的名字 f_name保存的文件名以及图title, 会用'-'分割，分割出的数组的最后一个元素作为title
 # save 是否保存， img_size 图像大小， font_size 字体大小， x_gap x轴间隔，即步长
 line_chart(data=[], x_label=[], y_label=[], f_name='', save=True, img_size=(8, 6), font_size=16, x_gap=1)
```
### 样例结果

![GELab6.png](https://s1.ax1x.com/2020/03/29/GELab6.png)  

![GZNwQ0.png](https://s1.ax1x.com/2020/03/29/GZNwQ0.png)

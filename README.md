# vocab-statistics
单词分析 词频分析 考研英语 四六级 清洗单词NLP

#尚未完善~~ 暂时不可使用

## 环境
python: <=3.6  
pattern：conda install pattern, pip install pattern  
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

### 载入分析
调用 `Vocabs` 类， 可根据集合或`uri`路径载入分析，生成词频。之后可求差集，并集，交集等操作。
```
 vocabs = Vocabs(name, data, uri)
```

### 样例结果

![GEH2rV.png](https://s1.ax1x.com/2020/03/29/GEH2rV.png)

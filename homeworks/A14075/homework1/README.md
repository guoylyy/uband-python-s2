具体可看:  https://github.com/hydewww/TermFrequency

# 词频分析

```coding in python3.6```

为摆脱无脑谷歌翻译而诞生的程序，希望能帮助自己啃下绝望的众英文文档。

## 用法

- **程序所需文件夹需先行创建**，可复制```example```中文件进行测试

- 用户添加的文件最好存为utf-8格式，可参考```example```中文件

### Main.py

分析文本，筛去常用词汇()后按```词频顺序```输出固定比例(自定义)的表格

- 文本放在```text```

- 英汉词典位于```buildin_dicts```(内置牛津词典)

- 常用词汇位于```clear_lists```

- 输出文件夹为```output```	

- 可改参数位于代码末尾

### GenerateDicts.py

将希望导入的词典转为程序所需格式

- 需修改分词部分的代码

- 新词典放在```new_dicts```

- 生成词典所在位置```buildin_dicts```

- Tips:若```buildin_dicts```只有中高考/四六级词汇，输出的就是文本中考纲范围内的单词

### 导入至anki

anki是本人强推的背诵软件，各平台均有客户端，官网:https://apps.ankiweb.net/index.html

点击```导入文件```选中```anki.txt```即可导入，记忆库中不会添加重复项。

关于anki的各种奇技淫巧可关注anki的知乎专栏:https://zhuanlan.zhihu.com/-anki


## Todo

- 用爬虫抓取文本
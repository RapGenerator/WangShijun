# Goals for Algorithm-group and WangShijun's ideas

using both English and Chinese for my own convenience and yours'

this file may be updated at any time

## 4 General Goals raised up at 8.2
- 语义通顺
- 评判标准
- 根据“主题”生成歌词
- 押韵

## my Decomposition for our goals & my coresponding Ideas

### 语义通顺

- thematic correspondence
	- between sentences
	- 几句歌词都在围绕同一个主题，而不是各说各话
- semantic coherence
	- within sentences
	- 一句歌词本身是“人话”
	- seq2seq比RNN更适合

### 评判标准

- subjective judging by human
    - [一篇论文](https://github.com/RapGenerator/WangShijun/blob/master/NotesforChinesePoetryGenerationwithPlanningbasedNeuralNetwork.md#evaluation-metrics)里就是这么干的。
- rhyme要求是可以按押韵规则写程序来评价的
- fluency/coherence/meaning要求，除了人工评价外，暂想不到评判标准
- ~~BLEU 与 cross_entrocy 的结合~~（YiWeiwen提出，被老师否掉了）

> “bleu和cross entropy看的点不一样，没必要深究怎么结合”
> 
> “整体评价还是human judge就可以”
> 
> ——王德瑞老师

### 根据“主题”生成歌词

- ideas below are inspired by [the paper](https://github.com/RapGenerator/WangShijun/blob/master/Chinese%20Poetry%20Generation%20with%20Planning%20based%20Neural%20Network.pdf)
- 流程：
    - 用户选择主题
    	- 前端需要考虑
    	- 涉及到 主题的展示形式
    - AI理解用户选择的主题的语义
    	- 受 主题的展示形式 影响
    	- 不同的主题展示形式应用 不同的 语义理解方式
    - AI将语义融入生成的歌词中
    	- 不同的主题展示形式应用 相同的 语义融入方式
    	- 上一点就要求：对于不同的主题展示形式，其语义理解的output是一致的
- 对用户，“主题”以什么形式展现？
    - 当然是在 natural language 的范畴内，不考虑图片、音乐、视频blabla
    - 一个关键词？
    - 几个关键词？
    - 一句话？
    - 一段话？
    - 也可以多种形式都支持
    - 如何展现“主题”会影响到后续的语义处理
    - 先做一个限制性较大、交互性较差的版本
    	- 直接要求用户必须给固定个数个关键词
    	- 则可先略过keywords expansion与keywords extraction部分
    - 后续再考虑在增加交互性
    	- 之后再加入keywords expansion与keywords extraction部分
- AI 理解了语义之后的统一output
    - 几个关键词
    - 都和用户选择的主题相关
    - 每个关键词用于生成一段歌词
        - 一段可以是~~一句，也可以是~~两句，或者四句（暂定为四句）
            - 一句的话，所需的关键词数量较多，keywords expansion/keywords extraction所得到的关键词的质量不易保证
            - 由于歌词押韵的惯例，最好得是以偶数句为单位生成
        - ~~一句还是~~两句或是四句，要在歌词生成之前定好，不能出现 一个关键词用于生成两句歌词、另一个关键词用于生成四句歌词的情况
    - 每段歌词拼在一起成为最终的歌词
- AI 针对 不同的主题展现形式 的语义理解方式
    - 一个关键词/几个关键词：keywords expansion
        - 将关键词扩充为固定数量个关键词（暂定为4个）
        - 固定数量 有多少个，要根据我们最终想要生成多少句歌词来定
            - 最终生成的歌词句数 = 语义理解output的关键词数 * 由一个关键词生成的歌词句数
        - 关键词扩充方式
            - co-occurence-based method
            - 找和已有关键词同时出现次数高的词来作为扩充的关键词
                - 此方法的优点
                    - 相较于后两种方式，较容易用代码实现
                    - 可解释性强
                    - 可以避开游飞老师说的“坑”
                - 游飞老师说的“坑”的形成原因：similarity-based
                - 扩充出的关键词须为已有关键词的：relative words rather than similar words
                - co-coherence-based method将引入的“新坑”：任何词都与“的地得”的同时出现次数很多，这些没有价值的词会极易成为被扩充的关键词
                - “新坑”的解决办法：用停用词词典筛选
            - RNNLM-based method
                - 用一个RNN去学习古诗中每句的关键词序列，以原有关键词作为序列的前几个，用学好的RNN去预测后几个关键词
                - 学习方式：在数据集的每首诗的每一句上运用textrank抽取关键词，并以此作为ground truth的label
            - Knowledge-based method
                - 写个爬虫去爬取wikipedia的第一段解释文本（再做extraction）、百度百科的第一段解释文本（再做extraction）、知乎相关问题的标签（标签短则可直接用）etc
    - 一句话/一段话：keywords extraction
        - 从长文本中抽取关键词
        - 抽取关键词方式
            - based on TextRank
                - jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
            - based on TF-IDF
                - jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
        - 如果抽取出的关键词个数不够我们的要求，可以再抽取了关键词后再用keywords expansion

### 押韵

- 押韵有两个要求：rhyme与tone。我之前将rhyme与tone混为一谈，看了论文才发现两者是不同的东西
- rhyme（要管）
    - 即，我之前理解的“押韵”
    - 古诗的押韵 与 嘻哈歌词的押韵 的不同
        - 押韵之处：古诗的押韵之处在第一、二、四句的最末，嘻哈歌词rap部分每句都要押韵
        - 押韵字数：古诗押韵在每一句的最末一个字，嘻哈歌词不一定只押韵在最末的一个字，可以是多个字
        - 是否换韵：古诗无换韵，嘻哈歌词需要换韵
        	- 根据一个关键词生成的一段歌词，要求押同一个韵
        	- 将不同关键词生成的几段歌词拼起来时，自然就换韵了
- tone（不要管）
    - 平、仄 声调
    - 一声、二声 为 平声，三声、四声 为 仄声
    - 对于嘻哈歌词，没有声调要求
    - 不用深入研究，弃

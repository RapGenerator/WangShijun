# Rhyme Study

## Goal

to make the generated lyrics rhyme, at least rhyme more

## Approaches

**need more ideas**

- split dataset
	- split based on rhyme
	- using paragraphs (several continuous lines) that all rhyme
	- **the amount of each training dataset is far not adequate**
- score the paragraph
	- writing a ranking function
	    - using in beam-search step to rank paragraph based on rhyme **hard**
	    - using after beam-search step to distinguish most rhyme paragraph
	- give more rhyme paragraph a higher score, while less rhyme paragraph a lower score
	- **need to choose an appropriate beam-size**

## Problems

- rhyme category method
	- based on rhyme content
		- like "ang", "e ai", "uan ei un" etc
	- based on rhyme form
		- like 排韵，隔行韵，交韵，抱韵 etc
- 不同的韵母不一定不押韵！how to define "rhyme or not"
    - using strict=False or strict=True? **need to try out**
    - reviewing 'in' rhyme with 'ing' or not? **need to try out**

韵母表

follow represents are consist with that used in pypinyin.lazy_pinyin() with strict=False/True

| strict=False | i | u | u | | strict=True | i | u | v |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| a  | ia  | ua  |    || a  | ia  | ua  |    |
| o  |     | uo  |    || o  |     | uo  |    |
| e  | ie  |     | ue || e  | ie  |     | ve |
| ai |     | uai |    || ai |     | uai |    |
| ei |     | ui  |    || ei |     | uei |    |
| ao | iao |     |    || ao | iao |     |    |
| ou | iu  |     |    || ou | iou |     |    |
| an | ian | uan |    || an | ian | uan |    |
| en | in  | un  | un || en | in  | uen | vn |
|ang | iang| uang|    ||ang | iang| uang|    |
|eng | ing |     |    ||eng | ing |     |    |
|ong | iong|     |    ||ong | iong|     |    |


汉语拼音全表

![汉语拼音全表](https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike150%2C5%2C5%2C150%2C50/sign=6fd993399225bc313f5009ca3fb6e6d4/6609c93d70cf3bc7dd118b1bda00baa1cd112a37.jpg)

- how to quantity the rhyme level?
	- between different rhyme forms
	- 排韵
		- 多于两行
		- 单押
		- 双押
		- N押
	- 隔行韵
		- 多于四行，偶数行
	- 交韵
		- 多于四行，偶数行
	- 抱韵
		- 四行


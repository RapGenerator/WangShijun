# rnn method on char level

## data using
8.txt : provided by our teacher

## how to train
> $ python3 gen_lyrics.py 0

## how to generate
> $ python3 gen_lyrics.py 1

free to change line 199 in code "gen_lyrics.py"
> prime = 'what you give to the rnn to begin generating with'

## performance
- stupid, easily trapped in endless loop

  - using raw data
eg:

放肆一下  
山  
我的痛苦 但是我的大鹏加  
我的心情的祖的 dife a money way  
我的头犹豫的尸雾  
我们无月性  
我们扬得是灵避之前  
我们是点定 with my money way  
我的头犹豫的尸雾  
有钱的头发  
I money way  
我的命 挥点 Liake are theestyle  
请侬给吾一则freestyle吗？  
又长又大  
历史不得听的奖理  
我的哥们的戒鹏  
我的心情  
军日谂8 un woney live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿的 live 蔡镇鸿

  - using split data

eg:

嘻哈一下  
我们都领悟一下 当hap la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la

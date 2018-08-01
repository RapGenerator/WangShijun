# data splitting by tone

## motivation
- using one single split data file to train the model, can make the generation text all rhyme definitely

> it really works.
> 
> said by LuYiyang after testing (using char-rnn method)

- using several split data files to train the model, can make the output changing rhyme in someway


## description
each "x_intail.txt" contains all the lyrics with tone "x" in the end of one line

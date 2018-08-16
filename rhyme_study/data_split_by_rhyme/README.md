# data splitting by rhyme

## motivation
- using one single split data file to train the model, can make the generation text all rhyme definitely

> it really works.
> 
> said by LuYiyang after testing (using char-rnn method)

- using several split data files to train the model, can make the output changing rhyme in someway


## description
- in danya
    
    - using designed rules for rhyming judging
    
    - each "x.txt" contains all the lyrics with tone "x" in the end of one line

- in shuangya

    - using designed rules for rhyming judging
    
    - each "x+y.txt" contains all the lyrics with tone "x" & "y" in the end of one line
    
    - contains some empty files

- in sanya

    - using designed rules for rhyming judging
    
    - each "x+y+z.txt" contains all the lyrics with tone "x" & "y" & "z" in the end of one line

    - contains some empty files

- in old-danya

    - each "x_intail.txt" contains all the lyrics with tone "x" in the end of one line

    - statistical description:

most common rhyme:

listed below when the number of lines is more than 300

|    rhyme   | number of lines |
| ---------- | --- |
| i | 10824 |
| e | 5657 |
| u | 4866 |
| ian | 4713 |
| ou | 3392 |
| an | 3183 |
| ai | 3140 |
| ao | 2999 |
| a | 2891 |
| uo | 2756 |
| ing | 2752 |
| ang | 2665 |
| ei | 2042 |
| ong | 1888 |
| ui | 1868 |
| en | 1573 |
| o | 1464 |
| uan | 1446 |
| in | 1436 |
| eng | 1285 |
| iao | 1254 |
| ie | 1059 |
| iang | 1029 |
| ia | 824 |
| ua | 812 |
| iu | 704 |
| y | 613 |
| uang | 567 |
| un | 472 |
| uai | 403 |
| t | 342 |
| ue | 339 |

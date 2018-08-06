# Notes for "Chinese Poetry Generation with Planning based Neural Network"

[the paper](https://github.com/RapGenerator/WangShijun/blob/master/Chinese%20Poetry%20Generation%20with%20Planning%20based%20Neural%20Network.pdf)

## problem statement

- generate classical Chinese poetry -- quatrain
- principles of a quatrain
	- one poem, 4 lines (different with ours)
	- one line, 5 or 7 characters (different with ours)
	- every character has a particular tone (different with ours)
		- tone refers to Ping, Ze
	- the last character of the second line and last line must belong to the same rhyme category (similar to ours, need further study)
- flow of existing method
	- user's writing intent -> a set of key words
	- a set of key words -> selecting one line from the dataset of poems
	- using the selected line as the first line of generated poem
	- generating other 3 lines based on the first line and the previous lines, RNN framework
- drawback of existing method
	- the user's writing intent can only affect the first line
	- semantic inconsistency, other 3 lines may have no association with the main topic of the poem
	- can't use modern term to generate a poem, due to the dataset of ancient poems

## general description for model

- two-stage
- framework: modified RNN encoder-decoder
- advantage
	- the generated poem is coherent
	- the generated poem is consistent with the user's intent

## model structure

- poem planning
	- the contents of poems, deal with "what to say" problem
	- user's writing intent -> a set of keywords/ a sentence/ a document described by natural language -> determine a sequence of 4 sub-topics for the poem
	- each sub-topic is related to the main topic, and represents an aspect of the writing intent
	- each line represented by a sub-topic
	- Keyword Extraction, if the user's input is too long, using TextRank algorithm, while keeping the original order
	- Keyword Expansion, if the user's input is too short, using RNNLM-based method or Knowledge-based method
- poem generation
	- surface realization, deal with "how to say" problem
	- using a modified RNN
		- modified for supporting encoding of both sub-topics and the preceding lines
		- the specific detail of modification needs to refer to the paper directly
	- sequentially, generated line by line
	- each line is generated according to the corresponding sub-topic and the preceding generated lines

## model advantages

- every line has a closer connection to user's intent
- can learn from extra knowledge source besides the poem dataset
	- can use web data or encyclopedias to generate sub-topics
	- eg: intent: 'Barack Obama' -> sub-topics such as: 'power', 'outstanding'...

## evaluation metrics

- HUMAN JUDGES!!!
- 4 evaluation standards

| standard | explanation |
|----------|------|
| poeticness | does the poem follow the rhyme and tone requirements? |
| fluency | does the poem read smoothly and fluently? |
| coherence | is the poem coherent across lines? |
| meaning | does the poem have a certain meaning and artistic conception? |

- i think the first standard can be computing by algorithm based on certain rules of rhyme

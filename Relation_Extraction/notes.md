- we want to find relation between words and concepts
- we want to build semantic network, relational graph

## Semantic networks

- representing relations between concepts
- example: WordNet is a network which collects words in synonym groups
- knowledge graph is organising not just semantic relations, but also knowledge

### Applications

- semantic analysis
- query expansion
- lexical substitution
- question answering
- domain classification
- summarization
- paraphrase

## What do we need

- morphological tags for all the words in a text
- syntactic analysis might help
- dataset

## Approaches

### Patter recognition

- most common approach
- trying to match a regular expression to Part-of-Speech and text

### Corpus query

- special case of pattern recognition
- for bigger data

### Multilingual translation

- to provide synonyms

### Distributed approach

- vector space model
- word-contect frequence matrix
- clustering

### Neural networkd

- mostly convolutional
- information we need to start:
  - word embeddings
  - position embeddings
  - part of speech embeddings

## Evaluation

- solving TOEFL synonym test
- SemEval
  - various tasks evaluating computational semantic analysis systems
  - human annotators provide gold standards

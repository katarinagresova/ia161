distinquish between meanining of words in different contects.
understanding organization of sentences in important for many NLP tasks.

## Syntantic analysis

- syntactic units are carriers of meaning
- words are not enough
  - *Honey, give me love* vs. *Love, give me honey*

## Morphology

- lower part of parsing
- word level meaning

### Word level analysis

- Problematic example: czech word *stát* with two completely different meanings
  - noun *stát* as country
  - verb *stát* as standing
- The main way to resolve ambiguities
  - looking at a word context
  - statistical computation

### Processin unknown words

- reasons for out-of-vocabulary words
  - rare terms
  - new terms
  - typos
  - colloquial words

## Parsing and Fact Extraction

- syntactic trees

### Extraction of structured information 

- split sentence into parts that have meaning
- processing parts into logical formula

### Grammar checking

- word level
- sentence level

## How to analyse natural language syntax?

### Prerequisites

- word level analysis (part of speech, gender, number)
- named entity recognition - can help with syntactic analysis
- common sense information (e.g. “pregnant” goes with women only)

### Named entity recognition

- determine that e.g. “prof. Václav Šplíchal” is a person
- can be viewed as a sub-task of syntactic analysis

### Statistical methods

- people annotate corpus
- statistic methods learn rules from the corpus
- positives:
  - universal across languages (to some extent)
- negatives
  - annotation is expensive
  - hard to customize for different applications
  - data are usually not big enough

### Rule-based methods

- specialists develop a set of rules (“grammar”)
- positives:
  - easy to customize for different applications
- negatives:
  - not universal, depends on specialists
  - grammar can become uneasy to maintain

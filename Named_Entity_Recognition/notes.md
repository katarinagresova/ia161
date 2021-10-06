# Names Entity Recognition (NER) consists of two tasks:
- recognition
- classification

It is one of the most desired part of NLP since it is a key to extract knowledge from text.
- getting structured information from unstructured text (from computer point of view)

## Names Entity Recognition
> is it an named entity?

### Recognizing boundaries
- depends on external knowledge

[Masaryk University] in [Brno] - current name  
[Masaryk University in Brno] - historical name

## Names Entity Classification
> what type of named entity it is?

### Classes
- common classes: PERSON, ORGANIZATION, LOCATION
- less common classes: MONEY, PERCENT, DATE, TIME
- rare classes: ARTWORK, PRODUCT, ROLE

### Metonymy
- the main problem of named entity classification
- we very often replace one expression by another (Prague sais that... meaning Czech government)

# Methods for NER

## Gazetteer methods (list of NEs)
> string search for known entities

Problems:
- one entity can have several meening
  - `May` the force be with you.
  - I was born on `May`.
  - Karel `May` is my favorite writer.
- unable to find new named entities

## Semi-supervised machine learning (bootstraping)
- based on patterns
- requires a small set of seeds
- we search for words, that appears in the same context as our provided seeds

## Supervised machine learning (training -> model)
- conditional random fields (CRFs) were the best models up to few years ago (now neural networks took over)
- we need wider context - meaning is not dependend just on surrounding words
- works with annotated data

### Neural Networks
- annotation stays
- recurrent neural networks (LSTM, BiLSTM) work good, but Transformers works the best - it is able to use bigger context
  - Transformers even solve all NLP tasks at once

# Evaluation of NER systems
- precision, recall, F1-score
  - not so good measurement because some tasks are harder
- separate precision, recall, F1-score for different classes


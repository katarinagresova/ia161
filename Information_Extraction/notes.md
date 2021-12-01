- main goal: make unstructured info structured
  - (un)structured for machines
- focuses on facts
  - fact is a statement about important things


## Ontologies

- computers have no prior, implicit knowledge
- in NLP, many facts are not mentioned in text, because they are abvious for us as humans
- we use ontologies (=machine readable knowledge base) to provide computers with some knowledge
- they are usualy modeled as a graph with triplets (subject – predicate – object)

### Schema.org

- one of famous ontologies
- it contains
  - taxonomy
  - human readable definition
  - properties
- info here is obvious for humans, but very handy for computers

### Semantic Web Technologies

- proposed ontology standard
- goal: web pages would be readable by humans as computers as well

## Information Extraction Applications

- direct appliacations for analytical readers
  - financial analysts
  - media analysts
  - lawyers
  - PR workers
  - students

- subsequent computer applications
  - information systems
  - question answering
  - automatic reasoning
  - automatic summarization
  - dialogue systems
  - ontology engineering

## Techniques

- Disambiguate and shorten the information
- Find informational redundancy, aggregate information from several
sources

## Successful Information Extraction Systems

- Automatic personal assistants
  - agrees automatically on meeting times
  - recognizes/asks for contact details
  - connects with other applications (e.g. Google Calendar)
- Extracting protein interaction from research texts
- Summarizing and filtering stock market news
- IE from social media (noisy)
- Automatic compliance checking with IE from regulatory documents
- Medication IE from clinical notes (dictated)

## Information Extraction Evaluation

- dificult
- datasets, competitions

## Information Extraction Approaches

### Specific domain / Complex information

- precise, narrow requests from small homogeneous corpora
- weighting/ordering/refining results

### General domain / Simple snippets of information

- vague request from huge data
- aggregation of the response

## Information Extraction Components

- named entity recognition (NE)
  - finds and classifies names, places, dates, keywords etc.
- coreference resolution (CO)
  - finds identity relations between entities
- relation extraction (RE)
  - add description to entities, finds relation between entities (based on CO)
- event extraction (EE)
  - fits RE into event scenarios
- ontology engineering
  - what relations are known and expected

### Relation Extraction

- scope: sentence or document level
- approaches
  - hand-crafted rules + statistics
  - pattern extraction
  - scenarios + filling the gaps
  - **neural approaches**
    - have better results then patterns
    - convolutional NN, recurrent NN, attention mechanism, hierarchical tagging, pre-trained models
    - problem: needs many data to train
  - **machine learning with distant supervision**
    - training data is not created by hund
    - distant supervision is used to collect positive examples
    - problem: how to get negative examples?

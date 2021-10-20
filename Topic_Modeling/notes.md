Topic modeling is about discovering unknown topical patterns in documents

## Applications;
- Recomenders systems
    - like Netflix, Amazon
    - we cluster users, we cluster products and then we match them to each other
- Document/book classification
- Bioinformatics
    - creating patient risk groups
- Opinion/sentiment analysis
- Chtbots, topic tracking
    - so chatbot will stay on the same topic during conversation
- Text categorization
  
## How to do it?

### Latent Semantic Analysis
- vector representation of documents
- compare by vector distance
- Application
    - Data clustering
    - Term relations (synonymy, polysemy)
    - Cross language document retrieval
    - Similarity in multi chice questions
    - detecting if patent is unique
- How does it work?
    - count term-document matrix (word frequency in document)
        - rows = words, columns = documents
        - it is a big, but sparse matrix
    - weighting metrix elements
        - most popular measure: tf-idf
            - term apearing only in few documents get bigger weight
    - Singular Value Decomposition
        - reducing dimensions, throwin away noise

### Latent Dirichlet Allocation

- statistical model
- we are expecting that each document is generated be selected words from topics
- each document is a mix of topics
- LDA tries to discover these topics and their ratio
- Applications:
  - topic relations
  - content recommendation
  - group.community overlapping
  - document topic changes
  - genetics (ancestral population)
- process
  - pick fixed number of topics
  - for each document, rendomly assign topic to each word
  - itereatively improve until steady statte

## Topic Labeling

- represent topic with human-friendly label
- approaches:
  - top N words from the list
  - find Wikipedia article based on word list
  - documnt summarization from topic documents

## Topic Coherence

- measuring score for single topic quality by semantic similarity between words in topic
- main goal is to detect similarity between words in a topic

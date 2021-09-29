> Stylometry is about measuring style of a style

It is measuring anything that can be quantified (length od sentences, usage of capital letters, count of errors, etc.).
Assumption is that everybody has specific style of writing (and it is not controlled by us, it is our default)



## What can be revealed?

- gender,
- region of origin,
- age,
- personality (extroverted ot introverted),
- education level,
- indication of the identity of the author:
  - authorship attribution,
  - machine generated text detection,
- etc.

## Stylometry techniques

- input: plain text
- result: vector of features
- task: learn weights of each feature to predict characteristics

## Authorship recognition

- stylome = author writeprint
- range: typical feature values for that calue
- consistency: which features are most important
- corpus similarity: which features areuncommon in corpus

## Categories of features

- morphological
- syntactic
- lexical
- other

## Assumptions - Author has:

- unique active vocabulary
- favourite phrases and word n-grams
- a certain level of knowledge of grammar (mistakes)
- personalized handling of typography

## Author's characteristic features

- Word/Sentence length statistics
- Author gender
  - Authors gender can be detected from first person sentences in some languages
- Wordclass (bigrams) statistics
- Morphological tags statistics
- Word repetition
  - Which words or wordclasses are frequently repeated
- Syntactic analysis
  - extracting features from syntactic trees

## Double-layer ML technique

- layer for each author and second layer of each combination of authors

Process:
1) Extract document features for each author characteristic
2) Apply learnt weights
3) Compare documents to obtain a similarity vector
4) ML classifier predict probability of the same authorsip

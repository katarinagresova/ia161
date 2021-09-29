> In language modeling we want to know how a specific language usually works, what are common phrases, word co-locations, etc.

## Basic tasks

- **Predicting words**
  - Given a sequence of a words, predict next word
- **Ranking phrases**
  - Useful when generating many phrases and we want to know which one is the best
  - Generating paraphrases of a question and then scoring them
  - Together with predicting words used for machine translation
- **Generating text**
  - Generating longer text from scratch, based on seed word or based on some other conditions
  - Can be used to generate caption of images

## Tasks relying on language modeling

- Statistical machine translation
- Automatic speech recognition
  - Generating text from waves, many versions, then ranking them
  - Every new word can change several previous predicted words
- Optical text recognition

## N-gram models

- **Idea:** longer context is not so important. Probability of longer sequence can be approximated by shorter n-grams.
- **Markov's assumption:** conditional probability can be approximated with limited history
- **Problems:**
  - Too many unique n-grams in a corpus and many of them occurs only once in a corpus
  - Missing n-gram - we need to assign non-zero probability for unseen data

## Quality and comparison of Language Models

- **Extrinsic**
  - We have some application and we can evaluate quality of result
- **Intrinsic**
  - Perplexity (lower is better) - using cross-entropy
    - When log in cross-entropy is binary, it is in bits
    - It is easy to cheat, or hard to say it we have good model or some bug in a model

## Neural Networks

- No probabilities, only scores
- **Representation of a words**
  - one-hot
  - Distributional representation
    - Word embeddings
    - Word is represented by shorter vector (not length of whole vocab)
    - Vectors are capturing some linguistic properties
- **State-of-the-art** neural models
  - Embeddings on input level
  - BERT
    - Training tasks - Easy to create data for these task
      - Masking tokens
      - Is-next-sentence
  - GPT
    - Generates next token in a sentence
  - TS
    - Uses transfer learning
- **Evaluation**
  - Standard benchmarks
    - GLUE
    - SuperGLUE
    - XTREME
  - Perplexity is not used anymore (only to compare it to statistical models)









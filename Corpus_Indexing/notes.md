Corpus: plan text + XML tags

## How to search?

- Plain text search is slow for large corpora
- Why not SQL? Corpus doesn't have relations nature. Rows are not independent from each other.


## Big corpora
- Too big to be stored in memory
- Too big to be search sequentially  
  -> We need preprocessing (indexing)
  - Trade off between compile-time (preprocessing) and run-time
  - Trade off between in memory and off-memory processing

## Zipf's law
- Observed law
- Statistical distribution of many phenomena, including natural language
- Low amount of words that are very frequent and then many rare words
  - In English, on average, word 'the' is 7% of any corpus
  - That’s why we need really big corpora - to observe those statistically rare words
- Big corpora is better
- Formaly: frequency of the n-th element fn ≈ (1/n) · f1
   - Frequency is inversely proportional to the rank according to frequency

## Building corpora
1. Content definition
   - What it will be used for?
2. Obtaining data
   - Crawling
3. Data cleaning
   - Spam, boilerplate, duplicates
4. Tokenization
   - Splitting text into parts
5. Sentence segmentation
   - Finding sentences
6. Further annotation (PoS tagging)
7. Corpus indexing and analysis

## Corpus indexing
- Text corpus is just a database
- Key data structures
   - Lexicon
       - Mapping between words and numbers
       - Working with numbers, rather with words - operations are faster
   - Corpus text
       - Whole corpus translated into numbers
       - To iterate over positions
   - Inverted (reversed) index
       - In what position a word appears
       - Like: id 1 appears on positions 1 and 5
       - To give fast access to positions for a given value
   - How to store integer numbers?
       - Given Zipf's distribution: fixed-length storing is very inefficient
       - Size of index matters - smaller works faster
       - Solution: variable-length encoding, such as Huffman coding or Elias' code
       - Saving just differences of inverted indices, not indices themselves
         - 1, 5, 10, 12 -> 1, 4, 5, 2
- Key idea: operations on **sorted** forward-only streams of positions
   - Order matters
   - We call it a FastStream
- CQL - corpus query language

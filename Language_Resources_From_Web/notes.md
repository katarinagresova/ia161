Extracting full natural language sentenses and ignoring duplicates and boilerplate. Text should be representing how language look in common use.

## Text corpus

> A corpus is a set of texts in a natural language.

### Usages

- **generally:** data for studying natural language
- **linguists:** analyses of language phenomena, language changes over
time
- **lexicographers, teachers:** dictionaries, word meanings, examples of a
typical use
- **sociologists:** style and theme, hot topics
- **marketing experts:** brands/product evaluation, sentimet analysis
- **statistical NLP:** language models for taggers, analysers, translation
systems, predictive writing, ...

### Sources

- **printed media:** books, newspapers, magazines, poetry collections
- **internet:** articles, presentations, blogs, discussions, socnet messages
(tweets, fb)
- **speech:** transcription of speech recordings, movie subtitles
- **other:** personal correspondence, school essays

### Size Matters

- Most language phenomena follow the Zipfian distribution ⇒ the more data the better.
- But a significant fraction of all web pages are of poor utility.
- Why are qualitative aspects so important?
  - web is the most used data source to obtain enough source texts – Web as Corpus
  - web is garbage (by definition) – garbage as corpus?
  - building language resources from the web requires extensive post-processing

### Building steps

- language identification
- character encoding detection
- efficient web crawling
- boilerplate removal
- de-duplication (removal of identical or nearly identical texts)
- fighting web spam
- text classification (topic, genre, language variety)
- authorship recognition & plagiarism detection
- storing & indexing of large text collections

## Web crawling

- Traverses the internet (graph of pages and links).
- Downloads documents (content & meta information).
- Stores documents (or their parts) in various formats for further use.
- Crawlers for various purposes:
  - GoogleBot – web indexing,
  - Linkcrawler – links, broken links checking,
  - Heritrix – general crawler, (Java, multiple treads),
  - SpiderLing – text corpora, (Python, multiple sockets).
- Parts
  - scheduler - desides which website to visit now
  - queue - of webpages discovered by crawling
  - downloader

## Language identification

Problems:
- multiple languages in a single web page, e.g. Maori/English
- similar languages, e.g. Danish vs. Norwegian
- language varieties, e.g. European vs. Brasilian Portuguese

Solutions:
- Google Compact Language Detector v. 3
  - neural network model
- langid.py
  - naive Bayes classifier over byte n-grams (1 ≤ n ≤ 4)

## Boilerplate removal

### What it a biolerpate?

- **Repeated parts** of a web page (not containing a new text) – header, footer, navigation.
- **Uninteresting text** (too short or not continuous) – advertisement, lists of items, article previews.
- Discussions should be separated from the main article text.

### Removal approaches

- Machine learning (SVM, CRF, neural networks, n-gram models):
  - Annotated web pages required for training.
  - Victor (CRF),
  - Ncleaner (n-grams).
- Heuristics:
  - Rules for including/excluding sections of text.
  - BTE (tag density),
  - Boilerpipe (link/text ratio),
  - jusText (link/text ratio, frequent words, context sensitive – smoothing).
  - Site Style Tree
    - represents both layout and content of a web page.
    - tries to find differences where pages differs - that are important parts
    - the same parts are biolerplate  

## Non-text removal

- we want to study just texts produced by humans

### Web spam definition

- Good content: fluent, natural, consistent text (regardless its purpose)
- Bad content – computer generated text
  - machine translation
  - keyword stuffing
  - phrase stitching
  - synonym replacement
  - automated summaries
  - any incoherent text
  
### Approaches to Web Spam Removal

1. trustworthy websites only
2. website rules in the crawler: distance from the seeds, hostname
3. supervised classification
4. semi-manual filtering of websites
    - curated by human
    - annotated spam websites can be then used to train a supervised classification model

## De-duplication

- Quite straightforward for full duplicates
  - compute hash functions and compare those
- What about similar documents?
  - People copy just parts of the document: original vs. copy
  - Or copy and modify: original vs. modified
  - Or copy and extend: original vs. extended

### Solutions

- N-gram shingling algorithm
  - shingles (slovak: šindle) are computed with mooving window with step smaller then window size
- onion – One INstance ONly2

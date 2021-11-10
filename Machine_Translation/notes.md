## Statistical Machine Translation

- rule-based systems motivated by linguistics
- best systems for machine translation since 2000 till around 2016
- usage: first translation, gisting
- output needs to be post-edited for final production

## Neural Machine Translation

- current state-of-the-art for machine translation
- today, all machine translation uses neural machine translation
- gives much better results than statistical translation
- big plus: almost no knowleadge about languages needed

### Architectures

- uses deep neural nets
- usualy based on encoder-decoder architecture
  - encoder: input is encoded into some vector
  - decoder: vector is decoded into sentence in target language
- current trend: transformers

### Word Alignment Matrix

- attention mechanism usualy means alignment of words

### Automatic evaluation of translation

- human: very time consuming and expensive
- gold standard: manually prepared reference translation 
- various approaches: n;grams agreement betwee c and r_i, edit distance, ...
- metrics
  - BLEU - the most widely used metric
    - based on n-grams
    - python `sacreBLEU` package
  - METEOR: correlates best with human evaluation

## What is translated?

- web pages
- technical manuals, how-tos
- scientific documents, papers, articles - for understanding, no publishing
- leaflets, flyers, catalogues
- Wikipedia articles (CS-SK)

## Machine translation today

- based on huge amounts data - model are better now because we have more data
- automatic evaluation metrics
- European union helped to provide data - official documents are translated to all 24 official languages
- Google Translate used as a base standard
  - there are better systems finetuned on specific domains
- morphologically rich languages have worse results
  - we need much more data for the same quality of results
- pairs \*-En En-\* prevails

## Data: parallel corpora
- Europarl: a collection of texts from the European Paliament
- OPUS: parallel texts of various sources
- Acquis CommunataireL EU laws

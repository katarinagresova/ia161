## Taks definition

We can look at it as **classification task**

 - Easiest task: positive vs. negative comments (or neutral)  
 - Second task: how do we know?  
 - Third task: what specifically is positive/negative?  

## Why it is important and interesting?

Opinions can **influence other people**

 - social media, reviews, ... influence other people decision,
 - framing in news,
 - summary of several opinions, ...

## Approaches

 - **Find positive and negative words and sum the up**
 - **Supervised machine learning**
   - Quite old approach
   - Convert stars to opinion (positive/negative)
     - Caution: some countries my put one star to the best thing
   - Best results with simple models as SVM
     - But depends on data, language
 - **Deep learning**
    - Last 5 years
    - Problems with word embedding
      - Close vectors for synonyms, names, but also for other words in similar contexts (as good or bad)
      - Sentiment-aware word embedding

## Datasets

 - **Lexicons**
    - datasets of positive and negative words
    - for older methods
    - but can help train NN as well
  - **Labeled texts**
    - IMBD dataset is most famous in this field

## State-of-the-art

Human performance around 80% - inter-annotator agreement is low.

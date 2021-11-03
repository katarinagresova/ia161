# Building Language Resources from the Web

Web crawling, boilerplate removal, de-duplication and plagiarism detection.

[Lecture notes](https://github.com/katarinagresova/ia161/blob/main/Language_Resources_From_Web/notes.md)  
[Practical session](https://github.com/katarinagresova/ia161/blob/main/Language_Resources_From_Web/IA161_Plagiarism_Detection.ipynb)

Official course materials can be found [here](https://nlp.fi.muni.cz/en/AdvancedNlpCourse/LanguageResourcesFromWeb).

# ia161 module

## Running Plagiarism Detector

To run plagiarism detection script, clone this repository and try it with provided data.

```bash
git clone https://github.com/katarinagresova/ia161.git
cd ia161/Language_Resources_From_Web/
python3 detector.py training_data.vert
```

To use your own data, format them in a following way:
- each document in a `<doc></doc>` tags with attributes:
    - author
    - id - unique id of a document
    - class - original or plagiarism
    - source - the id of the source (in the case of plagiarism) or the same as the id of the document (in the case of original)
- content of a document is then in a POS tagged vertical format : 3 TAB separated columns: word, lemma (the base form of the word), POS/morphological tag.

## Running Tests

For testing, you need to install `pytest` and `pytest-cov` packages.

To run a specific test

```bash
pytest -v ./tests/test_specific_file.py
```

To run all tests

```bash
pytest -v tests/
```

To get a test coverage
```bash
pytest --cov=src/genomic_benchmarks/ tests/ 
```

from ia161.detector import PlagiarismDetector
from pathlib import Path
import pytest
import numpy as np

TEST_RESOURCES_DIR_PATH = (Path(__file__).parents[0] / 'resources').resolve()

def test_parse_input():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')

    assert detector.metadata is not None
    assert len(detector.metadata.keys()) == 1
    assert len(detector.metadata['Josef Plch']) == 2
    assert len(detector.metadata['Josef Plch']['original']) == 2
    assert len(detector.metadata['Josef Plch']['suspicious']) == 1
    assert detector.metadata['Josef Plch']['original'][0] == {
        'author' : 'Josef Plch',
        'id' : '101',
        'class' : 'original',
        'source_id' : '101'
    }
    assert detector.metadata['Josef Plch']['original'][1] == {
        'author' : 'Josef Plch',
        'id' : '102',
        'class' : 'original',
        'source_id' : '102'
    }
    assert detector.metadata['Josef Plch']['suspicious'][0] == {
        'author' : 'Josef Plch',
        'id' : '106',
        'class' : 'plagiarism',
        'source_id' : '101'
    }

    assert detector.docs is not None
    assert len(detector.docs) == 3
    assert len(detector.docs['101']) == 18
    assert detector.docs['101']['word'][0] == 'Reveň'
    assert detector.docs['101']['lemma'][0] == 'reveň'
    assert detector.docs['101']['tag'][0] == 'k1gFnSc1'

def test_length_removal_zero():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')

    with pytest.raises(ValueError):
        detector.length_removal(0)

def test_length_removal_one():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')

    old_docs = detector.docs
    detector.length_removal(1)

    assert old_docs == detector.docs

def test_length_removal_two():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')
    detector.length_removal(2)

    assert len(detector.docs) == 3
    assert len(detector.docs['101']) == 14
    assert len(detector.docs['102']) == 22
    assert len(detector.docs['106']) == 19

def test__precompute_bag_of_words_docs():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')
    detector.length_removal(3)
    detector._precompute_bag_of_words_docs()

    assert detector.bag_of_words_docs is not None
    assert len(detector.bag_of_words_docs) == 3
    assert len(detector.bag_of_words_docs['101']) == 3
    assert len(detector.bag_of_words_docs['101']['word']) == 10
    assert len(detector.bag_of_words_docs['101']['lemma']) == 9
    assert len(detector.bag_of_words_docs['101']['tag']) == 6

    assert \
        sum(detector.bag_of_words_docs['101']['word'].values()) == \
        sum(detector.bag_of_words_docs['101']['lemma'].values()) == \
        sum(detector.bag_of_words_docs['101']['tag'].values())

def test_bag_of_words_the_same_documents():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')
    detector.length_removal(3)

    similarity = detector.bag_of_words('101', '101', 'word')
    assert similarity == 1

    similarity = detector.bag_of_words('101', '101', 'lemma')
    assert similarity == 1

    similarity = detector.bag_of_words('101', '101', 'tag')
    assert similarity == 1

    similarity = detector.bag_of_words('102', '102', 'word')
    assert similarity == 1

    similarity = detector.bag_of_words('106', '106', 'word')
    assert similarity == 1

def test_bag_of_words_different_documents():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')
    detector.length_removal(3)

    similarity = detector.bag_of_words('101', '102', 'word')
    assert similarity == 0.0

def test_bag_of_words_similar_documents():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')
    detector.length_removal(3)

    similarity = detector.bag_of_words('101', '106', 'word')
    assert similarity > 0.3 and similarity < 0.31

def test__precompute_doc_counts_per_word():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')
    detector.length_removal(3)
    detector._precompute_doc_counts_per_word()

    assert detector.doc_counts_per_word is not None
    assert len(detector.doc_counts_per_word) == 3
    assert len(detector.doc_counts_per_word['word']) == 40
    assert len(detector.doc_counts_per_word['lemma']) == 37
    assert len(detector.doc_counts_per_word['tag']) == 27

def test__tf_unknown():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')
    detector.length_removal(3)
    detector._precompute_doc_counts_per_word()

    tf = detector._tf('new_word', '101', 'word')
    assert tf == 0

def test__tf():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')
    detector.length_removal(3)
    detector._precompute_doc_counts_per_word()

    tf = detector._tf('Reveň', '101', 'word')
    assert tf == 2/12

    tf = detector._tf('reveň', '101', 'lemma')
    assert tf == 3/12
    
def test__idf():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')
    detector.length_removal(3)
    detector._precompute_doc_counts_per_word()

    idf = detector._idf('Reveň', 'word')
    assert idf == np.log(4/(1 + 1))

def test_tf_idf_the_same_documents():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')
    detector.length_removal(3)

    similarity = detector.tf_idf('101', '101', 'word')
    assert similarity == 1

    similarity = detector.tf_idf('101', '101', 'lemma')
    assert similarity == 1

    similarity = detector.tf_idf('101', '101', 'tag')
    assert similarity == 1

    similarity = detector.tf_idf('102', '102', 'word')
    assert similarity == 1

    similarity = detector.tf_idf('106', '106', 'word')
    assert similarity == 1

def test_tf_idf_different_documents():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')
    detector.length_removal(3)

    similarity = detector.tf_idf('101', '102', 'word')
    assert similarity == 0


def test_tf_idf_similar_documents():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')
    detector.length_removal(3)

    similarity = detector.tf_idf('101', '106', 'word')
    assert similarity > 0.08 and similarity < 0.081
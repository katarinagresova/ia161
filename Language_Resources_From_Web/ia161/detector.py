""" Plagiarism Detector

author: Katarina Gresova
email: 514001@mail.muni.cz

Implemented algorithm: TF-IDF
"""

import pandas as pd
import numpy as np
from scipy import spatial
from pathlib import Path
import re

class PlagiarismDetector:

    RESOURCES_DIR_PATH = (Path(__file__).parents[0] / '..'  / 'resources').resolve()

    def __init__(self):
        self.metadata = None
        self.docs = None

        self.doc_similarity_threshold = 0.5

        # store computations that might be useful for other methods
        self.bag_of_words_docs = None
        self.doc_counts_per_word = None

    def _guess_location(self, vert_file):
        if Path(vert_file).exists():
            return Path(vert_file)
        elif (self.RESOURCES_DIR_PATH / str(vert_file)).exists():
            return self.RESOURCES_DIR_PATH / str(vert_file)
        else:
            raise FileNotFoundError(f'File {vert_file} not found.')


    def parse_input(self, vert_file):
        """Parse input vert file into two dictionaries - metadata and docs.

        On top level, metagata group documents by authors. Each author has two lists of documents:
        - original
        - suspicious
        Each document metadata is represented by dictionary with keys:
        - author,
        - unique id,
        - class (original or suspicious),
        - source_id (The same as unique id for originals. Referencing original unique id for suspicious documents.),
        Second dictionary - docs - is organized by document id (referencing unique id from metadata).
        Each document is represented by pandas DataFrame with three columns:
        - word
        - lemma
        - tag
        """

        header_re = re.compile('<doc author="([^"]+)" id="(\d+)" class="(plagiarism|original)" source="(\d+)"')
        self.metadata = {}
        self.docs = {}
        current_id = None
        doc_list = []

        vert_file = self._guess_location(vert_file)
        with open(vert_file, "r") as handle:
            for line in handle:

                # start of the document - preparing metadata
                if line.startswith('<doc'):

                    # structure for info about document
                    author, id_, class_, source_id = header_re.match(line).groups()
                    doc = {
                        'author': author,
                        'id': id_,
                        'class': class_,
                        'source_id': source_id,
                    }
                    current_id = id_
                    doc_list = []

                    # end of the document - storing metadata
                elif line.startswith('</doc'):

                    # adding document to author's set - to original of suspisious documents
                    if not doc['author'] in self.metadata:
                        self.metadata[doc['author']] = {'original': [], 'suspicious': []}
                    if doc['class'] == 'original':
                        self.metadata[doc['author']]['original'].append(doc)
                    else:
                        self.metadata[doc['author']]['suspicious'].append(doc)

                    self.docs[current_id] = pd.DataFrame(doc_list, columns=['word', 'lemma', 'tag'])

                elif not line.startswith('<'):

                    # storing content of document
                    word, lemma, tag = line.rstrip().split('\t')[:3]
                    doc_list.append([word, lemma, tag])

    def length_removal(self, min_length):

        for id_, doc in self.docs.items():
            self.docs[id_] = doc[doc['word'].map(len) >= min_length]

    def bag_of_words(self, doc1_id, doc2_id, column):
        if self.bag_of_words_docs is None:
            self._precompute_bag_of_words_docs()

        vectors = [[], []]
        docs = [
            self.bag_of_words_docs[doc1_id][column],
            self.bag_of_words_docs[doc2_id][column]
        ]
        all_words = list(docs[0].keys() | docs[1].keys())

        for doc_index in [0, 1]:
            doc_len = float(sum(docs[doc_index].values()))

            for word in all_words:
                vectors[doc_index].append(docs[doc_index].get(word, 0) / doc_len)

        cosine_similarity = 1.0 - spatial.distance.cosine(vectors[0], vectors[1])
        return cosine_similarity

    def _precompute_bag_of_words_docs(self):
        self.bag_of_words_docs = {}

        for id_, doc in self.docs.items():
            self.bag_of_words_docs[id_] = {}
            for column in ['word', 'lemma', 'tag']:
                self.bag_of_words_docs[id_][column] = {}
                for word in doc[column]:
                    self.bag_of_words_docs[id_][column][word] = self.bag_of_words_docs[id_][column].get(word, 0) + 1

    def _tf(self, word, doc_id, column):

        try:
            num_of_words = float(sum(self.bag_of_words_docs[doc_id][column].values()))
            # count of word in current document / count of all words in document
            return self.bag_of_words_docs[doc_id][column][word] / num_of_words
        except(Exception):
            return 0

    def _precompute_doc_counts_per_word(self):

        if self.bag_of_words_docs is None:
            self._precompute_bag_of_words_docs()

        self.doc_counts_per_word = {}

        for _, doc in self.bag_of_words_docs.items():
            for column in ['word', 'lemma', 'tag']:
                self.doc_counts_per_word[column] = {}
                for word in doc[column]:
                    self.doc_counts_per_word[column][word] = self.doc_counts_per_word[column].get(word, 0) + 1

    def _idf(self, word, column):

        num_of_docs = len(self.docs)

        try:
            word_occurance = self.doc_counts_per_word[column][word] + 1
        except(Exception):
            word_occurance = 1
        return np.log(num_of_docs / word_occurance)

    def _tf_idf_doc(self, doc_id, column):

        if self.doc_counts_per_word is None:
            self._precompute_doc_counts_per_word()

        tf_idf_vec = np.zeros((len(self.doc_counts_per_word[column]),))
        for index, word in enumerate(self.doc_counts_per_word[column].keys()):
            tf = self._tf(word, doc_id, column)
            idf = self._idf(word, column)

            value = tf * idf
            tf_idf_vec[index] = value
        return tf_idf_vec

    def tf_idf(self, doc1_id, doc2_id, column):

        vector1 = self._tf_idf_doc(doc1_id, column)
        vector2 = self._tf_idf_doc(doc2_id, column)
        cosine_similarity = 1.0 - spatial.distance.cosine(vector1, vector2)
        return cosine_similarity

    def get_all_metrics(self):
        return [self.bag_of_words, self.tf_idf]

    def _compute_stats(self, stats):
        try:
            precision = stats['tp'] / float(stats['tp'] + stats['fp'])
        except ZeroDivisionError:
            precision = 0.0
        try:
            recall = stats['tp'] / float(stats['tp'] + stats['fn'])
        except ZeroDivisionError:
            recall = 0.0
        try:
            f1_measure = 2 * precision * recall / (precision + recall)
        except ZeroDivisionError:
            f1_measure = 0.0

        return precision, recall, f1_measure

    def evaluate(self, metrics=None):

        if metrics is None:
            metrics = self.get_all_metrics()

        for metric in metrics:
            for column in ['word', 'lemma', 'tag']:
                stats = {'tp': 0, 'fp': 0, 'tn': 0, 'fn': 0}

                for _, doc_set in self.metadata.items():
                    for doc in doc_set['suspicious']:

                        most_similar_doc_id = doc['id']  # default: document is most similar to itself
                        highest_similarity_score = 0.0
                        for orig_doc in doc_set['original']:

                            similarity_score = metric(doc1_id=doc['id'], doc2_id=orig_doc['id'], column=column)
                            if similarity_score >= self.doc_similarity_threshold and similarity_score > highest_similarity_score:
                                most_similar_doc_id = orig_doc['id']
                                highest_similarity_score = similarity_score

                        if most_similar_doc_id == doc['source_id']:
                            if doc['class'] == 'plagiarism':
                                stats['tp'] += 1
                            else:
                                stats['tn'] += 1
                        else:
                            if doc['class'] == 'plagiarism':
                                stats['fp'] += 1
                            else:
                                stats['fn'] += 1

                        print('%s\t%s\t%s\n' % (doc['id'], most_similar_doc_id, doc['source_id']))

                precision, recall, f1_measure = self._compute_stats(stats)
                print(
                    'Overall precision: %.2f, recall: %.2f, F1: %.2f \nfor method %s and column %s\n' % (
                        precision, recall, f1_measure, metric, column
                    )
                )

    def set_doc_similarity_threshold(self, threshold):
        self.doc_similarity_threshold = threshold

if __name__ == "__main__":
    detector = PlagiarismDetector()
    detector.parse_input('training_data.vert')
    detector.length_removal(3)
    detector.set_doc_similarity_threshold(0.5)
    detector.evaluate()

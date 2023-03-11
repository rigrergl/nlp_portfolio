"""
    Extracts the 25 most important terms from the cleaned text files

    Requirements:
        must have run the following scripts beforehand:
            1. link_scraper
            2. text_scaper
            3. clean_text
"""

import math
import pathlib
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')


def create_tf_dict(doc):
    tokens = word_tokenize(doc)
    tokens = [t for t in tokens if t.isalpha() and t not in stopwords.words('english')]

    # get term frequencies
    token_set = set(tokens)
    tf_dict = {t: tokens.count(t) for t in token_set}

    # normalize by number of tokens
    for t in tf_dict.keys():
        tf_dict[t] = tf_dict[t] / len(tokens)

    return tf_dict


def create_idf_dict(tf_dicts):
    idf_dict = {}

    # make the vocabularies
    vocab = set()
    vocab_by_doc = list()
    for tf_dict in tf_dicts:
        vocab = vocab.union(tf_dict.keys())
        vocab_by_doc.append(tf_dict.keys())

    for term in vocab:
        num_docs_containing_t = ['x' for v in vocab_by_doc if term in v]
        idf_dict[term] = math.log((1 + len(tf_dicts)) / (1 + len(num_docs_containing_t)))

    return idf_dict


def create_tf_idf(tf, idf):
    tf_idf = {}
    for t in tf.keys():
        tf_idf[t] = tf[t] * idf[t]

    return tf_idf


def main():
    docs = []
    for i in range(1, 16):
        with open(pathlib.Path.cwd().joinpath('data', 'text', f'text_{i}_clean.txt'), 'r', encoding='utf-8') as f:
            new_doc = f.read().lower()
            docs.append(new_doc)

    # generate term frequency dictionaries
    tf_dicts = []
    for doc in docs:
        new_dict = create_tf_dict(doc)
        tf_dicts.append(new_dict)

    # make the idf dict
    idf_dict = create_idf_dict(tf_dicts)

    # make the tf-idf dicts
    tf_idf_dicts = []
    for tf_dict in tf_dicts:
        tf_idf_dicts.append(create_tf_idf(tf_dict, idf_dict))

    # test tf-idf
    doc_term_weights = sorted(tf_idf_dicts[0].items(), key=lambda x: x[1])
    print(doc_term_weights[:5])

    doc_term_weights = sorted(tf_idf_dicts[0].items(), key=lambda x: x[1], reverse=True)
    print(doc_term_weights[:5])


if __name__ == '__main__':
    main()

"""
    Extracts the 25 most important terms from the cleaned text files

    Requirements:
        must have run the following scripts beforehand:
            1. link_scraper
            2. text_scaper
            3. clean_text
"""

import pathlib
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')


def create_tf_dict_(doc):
    tokens = word_tokenize(doc)
    tokens = [t for t in tokens if t.isalpha() and t not in stopwords.words('english')]

    # get term frequencies
    token_set = set(tokens)
    tf_dict = {t: tokens.count(t) for t in token_set}

    # normalize by number of tokens
    for t in tf_dict.keys():
        tf_dict[t] = tf_dict[t] / len(tokens)

    return tf_dict


def main():
    docs = []
    for i in range(1, 16):
        with open(pathlib.Path.cwd().joinpath('data', 'text', f'text_{i}_clean.txt'), 'r', encoding='utf-8') as f:
            new_doc = f.read().lower()
            docs.append(new_doc)

    # generate term frequency dictionaries
    tf_dicts = []
    for doc in docs:
        new_dict = create_tf_dict_(doc)
        tf_dicts.append(new_dict)


if __name__ == '__main__':
    main()

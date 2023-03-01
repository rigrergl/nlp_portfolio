import pathlib

import nltk
from nltk import word_tokenize
from nltk.util import ngrams

nltk.download('punkt')

data_folder = pathlib.Path('data')


def gen_ngrams(filename):

    # read text and remove newlines
    file_path = data_folder / filename
    with open(file_path, 'r') as f:
        text = f.read()

    text = text.replace("\n", "")

    # create bigrams and unigrams list
    unigrams = word_tokenize(text)
    bigrams = list(ngrams(unigrams, 2))

    print(bigrams[:200])

    return None, None


if __name__ == '__main__':
    bigram_dict_en, unigram_dict_en = gen_ngrams('LangId.train.English')


import pathlib
import pickle

import nltk
from nltk import word_tokenize
from nltk.util import ngrams

nltk.download('punkt')

data_folder = pathlib.Path('data')


def gen_ngrams(filename):

    # read text and remove newlines
    file_path = data_folder / filename
    with open(file_path, 'r', encoding="utf8") as f:
        text = f.read()

    text = text.replace("\n", "")

    # create bigrams and unigrams list
    unigrams = word_tokenize(text)
    bigrams = list(ngrams(unigrams, 2))

    # create dict of bigram counts
    bigram_dict = {b: bigrams.count(b) for b in set(bigrams)}

    # create dict of unigram counts
    unigram_dict = {u: unigrams.count(u) for u in set(unigrams)}

    return bigram_dict, unigram_dict


if __name__ == '__main__':
    bigram_dict_en, unigram_dict_en = gen_ngrams('LangId.train.English')
    bigram_dict_fr, unigram_dict_fr = gen_ngrams('LangId.train.French')
    bigram_dict_it, unigram_dict_it = gen_ngrams('LangId.train.Italian')

    pickle.dump(bigram_dict_en, open('bigram_dict_en', 'wb'))
    pickle.dump(unigram_dict_en, open('unigram_dict_en', 'wb'))

    pickle.dump(bigram_dict_fr, open('bigram_dict_fr', 'wb'))
    pickle.dump(unigram_dict_fr, open('unigram_dict_fr', 'wb'))

    pickle.dump(bigram_dict_it, open('bigram_dict_it', 'wb'))
    pickle.dump(unigram_dict_it, open('unigram_dict_it', 'wb'))


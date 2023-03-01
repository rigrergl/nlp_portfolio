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

    # create dict of bigram counts
    bigram_dict = {b: bigrams.count(b) for b in set(bigrams)}

    # create dict of unigram counts
    unigram_dict = {u: unigrams.count(u) for u in set(unigrams)}

    return bigram_dict, unigram_dict


if __name__ == '__main__':
    bigram_dict_en, unigram_dict_en = gen_ngrams('LangId.train.English')

    count = 0
    for key, value in bigram_dict_en.items():
        if count >= 20:
            break
        print(key, value)
        count += 1

    print()
    count = 0
    for key, value in unigram_dict_en.items():
        if count >= 20:
            break
        print(key, value)
        count += 1

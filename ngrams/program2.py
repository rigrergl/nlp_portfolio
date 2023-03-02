import pickle
import pathlib

from nltk import word_tokenize
from nltk.util import ngrams


def calc_lang_prob(line):
    unigrams_test = word_tokenize(line)
    bigrams_test = list(ngrams(unigrams_test, 2))

    total_v_size = len(unigram_dict_en) + len(unigram_dict_fr) + len(unigram_dict_it)

    p_laplace_en = 1
    p_laplace_fr = 1
    p_laplace_it = 1

    for bigram in bigrams_test:
        # Multiply by next probability in English
        n_en = bigram_dict_en[bigram] if bigram in bigram_dict_en else 0
        u_en = unigram_dict_en[bigram[0]] if bigram[0] in unigram_dict_en else 0
        p_laplace_en = p_laplace_en * ((n_en + 1) / (u_en + total_v_size))

        # Multiply by next probability in French
        n_fr = bigram_dict_fr[bigram] if bigram in bigram_dict_fr else 0
        u_fr = unigram_dict_fr[bigram[0]] if bigram[0] in unigram_dict_fr else 0
        p_laplace_fr = p_laplace_fr * ((n_fr + 1) / (u_fr + total_v_size))

        # Multiply by next probability in Italian
        n_it = bigram_dict_it[bigram] if bigram in bigram_dict_it else 0
        u_it = unigram_dict_it[bigram[0]] if bigram[0] in unigram_dict_it else 0
        p_laplace_it = p_laplace_it * ((n_it + 1) / (u_it + total_v_size))

    return p_laplace_en, p_laplace_fr, p_laplace_it


if __name__ == '__main__':
    # Get English dictionaries
    bigram_dict_en = pickle.load(open('bigram_dict_en', 'rb'))
    unigram_dict_en = pickle.load(open('unigram_dict_en', 'rb'))

    # Get French dictionaries
    bigram_dict_fr = pickle.load(open('bigram_dict_fr', 'rb'))
    unigram_dict_fr = pickle.load(open('unigram_dict_fr', 'rb'))

    # Get Italian dictionaries
    bigram_dict_it = pickle.load(open('bigram_dict_it', 'rb'))
    unigram_dict_it = pickle.load(open('unigram_dict_it', 'rb'))

    # Read in test file
    with open(pathlib.Path.cwd().joinpath('data').joinpath('LangId.test'), encoding='utf8') as f:
        test_text = f.read().splitlines()

    for test_line in test_text:
        en_prob, fr_prob, it_prob = calc_lang_prob(test_line)
        if en_prob > fr_prob and en_prob > it_prob:
            print('English')
        elif fr_prob > it_prob:
            print('French')
        else:
            print('Italian')


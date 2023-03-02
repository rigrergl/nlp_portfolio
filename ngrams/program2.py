import pickle
import pathlib


def calc_lang_prob(line):
    print(line)
    return None, None, None


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

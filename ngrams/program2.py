import pickle

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
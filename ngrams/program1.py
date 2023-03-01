import pathlib

data_folder = pathlib.Path('data')


def gen_ngrams(filename):
    file_path = data_folder / filename
    with open(file_path, 'r') as f:
        raw_text = f.read()

    print(raw_text[:200])

    return None, None


if __name__ == '__main__':
    bigram_dict_en, unigram_dict_en = gen_ngrams('LangId.train.English')


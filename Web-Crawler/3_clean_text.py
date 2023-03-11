import pathlib
from nltk.tokenize import sent_tokenize
import re


def clean_text(text):
    text = text.replace("\n", "").replace("\t", "")  # remove newlines and tabs
    text = re.sub(' +', ' ', text).strip()  # remove extra spaces
    text = text.lower()
    result = ""

    for sent in sent_tokenize(text):
        result = result + sent + "\n"

    return result


def main():
    for i in range(1, 16):
        with open(pathlib.Path.cwd().joinpath('data', 'text', f'text_{i}.txt'), 'r', encoding='utf-8') as f:
            raw_text = f.read()

        cleaned_text = clean_text(raw_text)

        with open(pathlib.Path.cwd().joinpath('data', 'text', f'text_{i}_clean.txt'), 'w', encoding='utf-8') as out:
            out.write(cleaned_text)


if __name__ == '__main__':
    main()

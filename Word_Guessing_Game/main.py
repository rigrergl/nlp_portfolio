import sys
import os
import nltk


def main():
    #  Download tokenizer 'punkt'
    if not os.path.exists(os.path.join(nltk.data.find('tokenizers'), 'punkt')):
        nltk.download('punkt')
    else:
        print("Package punkt found, download skipped")

    # check args
    if len(sys.argv) < 2:
        print("Usage: python main.py [file_name]")

    file_name = sys.argv[1]

    # Read file
    with open(file_name, 'r') as f:
        text = f.read()

    # Calculate Lexical Diversity
    tokens = nltk.word_tokenize(text)
    tokens = [t.lower() for t in tokens]
    token_set = set(tokens)
    print("Lexical Diversity: %.2f" % (len(token_set) / len(tokens)))


if __name__ == "__main__":
    main()

import sys
import os
import nltk
nltk.download('punkt')
nltk.download('stopwords')


def main():
    # check args
    if len(sys.argv) < 2:
        print("Usage: python main.py [file_name]")

    file_name = sys.argv[1]

    # Read file
    with open(file_name, 'r') as f:
        text = f.read()

    # Calculate Lexical Diversity
    tokens = nltk.word_tokenize(text.lower())
    token_set = set(tokens)
    print("Lexical Diversity: %.2f" % (len(token_set) / len(tokens)))

    # preprocess raw text
    tokens, nouns = preprocess_raw_text(text)


def preprocess_raw_text(raw_text):
    stop_words = nltk.corpus.stopwords.words('english')

    # Tokenize text
    tokens = nltk.word_tokenize(raw_text.lower())
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words and len(t) > 5]
    print(len(tokens))

    return None, None


if __name__ == "__main__":
    main()

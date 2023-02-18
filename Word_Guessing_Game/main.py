import sys
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


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
    print("Lexical Diversity: %.2f\n" % (len(token_set) / len(tokens)))

    # preprocess raw text
    lemmatized_tokens, nouns = preprocess_raw_text(text)


def preprocess_raw_text(raw_text):
    stop_words = nltk.corpus.stopwords.words('english')

    # Tokenize text
    tokens = nltk.word_tokenize(raw_text.lower())
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words and len(t) > 5]

    # Lemmatize the tokens
    wnl = nltk.stem.WordNetLemmatizer()
    lemmatized_tokens = [wnl.lemmatize(t) for t in tokens]

    # Make a list of unique lemmas
    lemmas_unique = list(set(lemmatized_tokens))

    # POS tagging on unique lemmas
    pos_tags = nltk.pos_tag(lemmas_unique)
    print("First 20 POS tags on unique lemmas:")
    print(pos_tags[:20], "\n")

    # Create a list of only those lemmas that are nouns
    nouns = [tag[0] for tag in pos_tags if tag[1][0] == 'N']

    # Print number of tokens and number of nouns
    print("Number of tokens:", len(lemmatized_tokens))
    print("Number of nouns:", len(nouns))

    return lemmatized_tokens, nouns


if __name__ == "__main__":
    main()

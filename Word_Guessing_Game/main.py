import sys
import nltk
from random import randint
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

'''
Assumptions:
    - In the preprocessing method, I made the decision to return lemmatized tokens rather than the tokens specified in step a
        of the instructions. I made this decisions because to me it makes more sense to count noun frequency using the lemmatized tokens 
        of the original text, since the unique nouns list is generated using the lemmatized version of the tokens. In my experiments, counting 
        noun frequencies this way (grouping all nouns that have the same lemma), also made the frequency counts more consistent, alleviating
        the randomness of the Part of Speech (POS) tagger.
'''


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

    # Get the 50 most common nouns
    vocab = {n: lemmatized_tokens.count(n) for n in nouns}
    sorted_vocab = sorted(vocab, key=vocab.get, reverse=True)
    top_50_nouns = sorted_vocab[:50]

    print("Top 50 Nouns: ")
    for noun in top_50_nouns:
        print(noun, ":", vocab[noun])
    print("\n")

    play_guessing_game(top_50_nouns)


def play_guessing_game(word_bank):
    random_i = randint(0, 49)
    word = word_bank[random_i]

    score = 5
    word_display = ["_"] * len(word)

    print("Let's play a word guessing game!")
    while score >= 0:
        if "_" not in word_display:
            print("You solved it!\n")
            print("Current score:", score, "\n")
            print("Guess another word")
            random_i = randint(0, 49)
            word = word_bank[random_i]
            word_display = ["_"] * len(word)
            continue

        print_word_display(word_display)
        guess = input("Guess a letter: ")
        if guess == "!":
            break

        indices = get_indices_of_char(word, guess)
        if indices:
            print("Right! Score is", score)
            for i in indices:
                word_display[i] = guess
        else:
            score -= 1
            print("Sorry, guess again. Score is", score)

        if score < 0:
            print("Sorry, you're all out of points. Game over :(")


def get_indices_of_char(word, char):
    indices = []
    for i in range(len(word)):
        if word[i] == char:
            indices.append(i)
    return indices

def print_word_display(guess):
    result = ""
    for c in guess:
        result += c + " "
    print(result)


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
    print("Number of nouns:", len(nouns), "\n")

    return lemmatized_tokens, nouns


if __name__ == "__main__":
    main()

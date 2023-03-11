"""
    Creates a knowledge based off of the manually determined top 10 terms
"""

import pathlib
import pickle


def main():
    with open(pathlib.Path.cwd().joinpath('data', 'manually_determined_top_10_terms.txt'), 'r', encoding='utf-8') as f:
        important_terms = [line.strip() for line in f]

    knowledge_base = {}

    # loop through the terms
    for term in important_terms:
        facts = []

        for i in range(1, 16):
            with open(pathlib.Path.cwd().joinpath('data', 'text', f'text_{i}_clean.txt'), 'r', encoding='utf-8') as f:
                text = f.read().splitlines()

            for sentence in text:
                if term in sentence:
                    facts.append(sentence)
        knowledge_base[term] = facts

    pickle.dump(knowledge_base, open('knowledge_base.p', 'wb'))


if __name__ == '__main__':
    main()

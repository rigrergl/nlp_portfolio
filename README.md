# nlp_portfolio
A collection of projects to help me learn about Natural Language Processing.

## Assignment 0
Introduction document summarizing historical and current approaches to NLP, as well as a reflection on my personal interest in NLP.

You can see the [document here](Overview_of_NLP.pdf).

## Program 1
Simple program to get used to text processing in python.

You can see the [code here](Assignment1/main.py) and a [descriptive document here](Assignment1/readme.md).

## Word Guessing Game
Program to get used to Part of Speech (POS) tagging with NLTK. Also includes a hangman-style word guessing game that chooses a word at random from the 50 most common lemmas occurring in the text.

You can see the [code here](Word_Guessing_Game/main.py) and instruction on how to run it [here](Word_Guessing_Game/readme.md)


## WordNet
Assignment to demonstrate skills in WordNet and SentiWordNet, as well as finding collocations. Notebook can be found [here](NLP_WordNet.ipynb)

## Ngrams
Assignment to gain experience in creating ngrams from text and building a language model from ngrams, as well as to reflect on the utility of ngram language models

[program1](ngrams/program1.py) generate the unigram and bigram dicts for the given English, French, and Italian training sets. It then pickles these dictionaries so that they can be used by program2.

[program2](ngrams/program2.py) uses unpickles the dictionaries created by program1 and uses them to compute the most likely language for each line in the test data set. It then computes the accuracy using the solutions set. 

The [narrative](ngrams/Narrative.pdf) provides a reflection on ngrams and the utility of ngram language models.


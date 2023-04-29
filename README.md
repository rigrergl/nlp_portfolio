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

## Sentence Parsing
Assignment to understand concepts related to sentence syntax, understand the 3 types of sentence parses (PSG, dependency, and SRL), and to be able to use syntax parsers

The document for this assignment can be found [here](Sentence-Parsing.pdf)

## Web Crawler
Assignment to understand the importance of corpora in NLP, understand how to extract information from website using html, understand how websites work, and be able to do web scraping using Beautifuk Soup.

The report for this assigment can be found [here](Web-Crawler/Report.pdf).

The code for this project includes the following python files:
1. [1_link_scraper.py](Web-Crawler/1_link_scraper.py)
2. [2_text_scraper.py](Web-Crawler/2_text_scraper.py)
3. [3_clean_text.py](Web-Crawler/3_clean_text.py)
4. [4_extract_important_terms.py](Web-Crawler/4_extract_important_terms.py)
5. [5_create_knowledge_base.py](Web-Crawler/5_create_knowledge_base.py)

Instructions on how to run then Web Crawler locally can be found [here](Web-Crawler/readme.md). 

## Text Classification 1 
Assignment Goals:
- Gain experience with sklearn using text data
- Gain experience with text classification

What I did:
- Used [this](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction) dataset to train models to classify a job posting as real or fraudulent
- Tried Naive Bayes, Logistic Regression, and Neural networks using sklearn
- Wrote up my analysis on the various approaches in the [notebook](Text-Classification/Text_Classification.ipynb)

## ACL Paper Summary
Assignment Goals:
- Get familiar with reading ACL Papers
- Learn how to stay updated with the rapidly evolving field of NLP

What I did:
- Read the following [paper](https://aclanthology.org/2022.acl-long.538/)
- Wrote up an analysis on the authors' findings and contributions

The paper analysis can be found [here](https://github.com/rigrergl/nlp_portfolio/blob/main/ACL%20Paper%20Summary.pdf)

## Text Classification 2
Assignment Goals:
- Gain experience with Keras
- Gain experience with text classificatiom
- Gain experience with deep learning model variations and embeddings

What I did:
- Experimented with several approaches to train a classifier model
- Tried basic sequential model
- Trained a Recurrent Neural Network (RNN)
- Trained a few variations on a Convolutional Neural Network (CNN) with different embedding techniques
- Evaluated and analysed the results, comparing the performance of each model

Notebook containing the code can be found [here](https://github.com/rigrergl/nlp_portfolio/blob/main/Text-Classification-2/Text-Classification-2.ipynb)

## ChatBot
Assignment Goals:
- Create a chatbot using NLP techniques learned in class
- The chatbot should be able to carry on a limited conversation in a particular domain using a knowledge base or
knowledge from the web, and knowledge it learns from the user

What I did:
- Extracted information on over 12K book from [this](https://www.kaggle.com/datasets/ymaricar/cmu-book-summary-dataset) dataset. 
- Used [weaviate](https://weaviate.io/) to store the text information about the books as vectors in a vector database
- Created a ChatBot is integrated with [OpenAI's chat API](https://platform.openai.com/docs/guides/chat) to gather user preferences
- Used the information gathered about the user to query the vector database and retrieve books that the user might like

The code and report can be found [here](https://github.com/rigrergl/nlp_portfolio/tree/main/chatbot)

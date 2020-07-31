from os import listdir
import pandas as pd 
import re
from collections import Counter
from nltk import tokenize
import matplotlib.pyplot as plt
import seaborn as sns
from stylometry.stylometry.extract import *
import spacy
import en_core_web_sm


def remove_quotes(article):
    quotes = re.findall("\“.*?\”", article)
    quotes2 = re.findall("\".*?\"", article)
    for quote in quotes:
        article = article.replace(quote, '')
    for quote in quotes2:
        article = article.replace(quote, '')
    return article

def alpha_chars_ratio(article):
    count = 0 
    total = 0
    for char in article:
        total += 1
        if char.isalpha():
            count += 1
    return count/total

def digit_chars_ratio(article):
    count = 0
    total = 0
    for char in article:
        total += 1
        if char.isdigit():
            count += 1
    return count/total

def upper_chars_ratio(article):
    count = 0 
    total = 0 
    for char in article:
        total += 1
        if char.isupper():
            count += 1
    return count/total

def white_chars_ratio(article):
    count = 0 
    total = 0 
    for char in article:
        total += 1
        if char.isspace():
            count += 1
    return count/total

def counter_of_words(article):
    article = article.lower()
    article = re.sub("[^\w ]", "", article)
    words = article.split(" ")
    return Counter(words)

def total_number_of_words(article):
    counter = counter_of_words(article)
    total = 0
    for item, value in counter.items():
        total += value
    return total

def size_of_vocabulary(article):
    counter = counter_of_words(article)
    return len(list(counter.keys()))

def type_token_ratio(article): # better solution 
    return size_of_vocabulary(article)/total_number_of_words(article)

# words occuring once
def hapax_legomena(article):
    counter = counter_of_words(article)
    total = 0 
    for item, value in counter.items():
        if value == 1:
            total += 1
    return total

def hapax_dislegomena(article):
    counter = counter_of_words(article)
    total = 0 
    for item, value in counter.items():
        if value == 2:
            total += 1
    return total

def average_word_length(article): # there is better solution
    counter = counter_of_words(article)
    total_length = 0
    size = len(list(counter.keys()))
    for word in counter.keys():
        total_length += len(word)
    return total_length/size

def average_sentence_char_length(article):
    sentences = tokenize.sent_tokenize(article)
    size = len(sentences)
    total = 0 
    for sentence in sentences:
        for char in sentence:
            total += 1
    return total/size

def average_sentence_word_length(article):
    sentences = tokenize.sent_tokenize(article)
    size = len(sentences)
    total = 0
    for sentence in sentences:
        counter = counter_of_words(sentence)
        for item, value in counter.items():
            total += value
    return total/size

def lexical_diversity(article):
    instance = StyloDocument(text=article)
    return instance.type_token_ratio()

def mean_word_length(article):
    instance = StyloDocument(text=article)
    return instance.mean_word_len()

def mean_paragraph_len(article):
    instance = StyloDocument(text=article)
    return instance.mean_paragraph_len()

def exclamation_mark_rate(article):
    instance = StyloDocument(text=article)
    return instance.term_per_thousand('!')

def question_mark_rate(article):
    instance = StyloDocument(text=article)
    return instance.term_per_thousand('?')

def number_of_adverbs(article):
    text = nltk.word_tokenize(article)
    fdist = FreqDist(article)
    count = 0
    for tag in nltk.pos_tag(text):
        if tag[1] == 'RB':
            count += 1
    return count/fdist.N()

def number_of_adjectives(article):
    text = nltk.word_tokenize(article)
    fdist = FreqDist(article)
    count = 0
    for tag in nltk.pos_tag(text):
        if tag[1] == 'JJ':
            count += 1
    return count/fdist.N()

def number_of_nouns(article):
    text = nltk.word_tokenize(article)
    fdist = FreqDist(article)
    count = 0
    for tag in nltk.pos_tag(text):
        if tag[1] == 'NN':
            count += 1
    return count/fdist.N()

def number_of_prepositions(article):
    text = nltk.word_tokenize(article)
    fdist = FreqDist(article)
    count = 0
    for tag in nltk.pos_tag(text):
        if tag[1] == 'IN':
            count += 1
    return count/fdist.N()

def number_of_conjuctions(article):
    text = nltk.word_tokenize(article)
    fdist = FreqDist(article)
    count = 0
    for tag in nltk.pos_tag(text):
        if tag[1] == 'CC':
            count += 1
    return count/fdist.N()

def number_of_verbs(article):
    text = nltk.word_tokenize(article)
    fdist = FreqDist(article)
    count = 0
    for tag in nltk.pos_tag(text):
        if 'VB' in tag[1] :
            count += 1
    return count/fdist.N()

def adj_adv(article):
    text = nltk.word_tokenize(article)
    fdist = FreqDist(article)
    count = 0
    for tag in nltk.pos_tag(text):
        if tag[1] == 'JJ' or tag[1] =='RB':
            count += 1
    return count/fdist.N()

def number_of_quotes(article):
    result = re.findall("\“.*?\”", article)
    diff_result = re.findall("\".*?\"", article)
    return len(result)+len(diff_result)

def number_of_ne(article):
    nlp = en_core_web_sm.load()
    spacy_article = nlp(article)
    fdist = FreqDist(article)
    return len(spacy_article.ents)/fdist.N()


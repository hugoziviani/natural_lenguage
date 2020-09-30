import nltk

from nltk import ngrams
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest
from string import punctuation
from collections import Counter
from itertools import zip_longest


def extract_ngrams(data, num):
    n_grams = ngrams(nltk.word_tokenize(data), num)
    return [ ' '.join(grams) for grams in n_grams]

def frequency_by_vocab(text, vocabulary, n_grams):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text.lower())
    n_text = ' '.join(words)
    n_grams_text = extract_ngrams(n_text, n_grams)

    result = list()
    for word in vocabulary:
        if word in n_grams_text:
            result.append(n_text.count(word))
        else:
            result.append(0)
    return result
         
def without_stop_words(text, vocabulary):
    wrds = word_tokenize(text.lower())
    words_free=list()
    stopwords_table = set(stopwords.words('portuguese') + list(punctuation))
    for wd in wrds:
        if wd not in stopwords_table:
            words_free.append(wd)
    
    frequency = FreqDist(words_free)
    return frequency

def get_ngrams(text, n_words, vocabulary_grams):
    tokenizer = RegexpTokenizer(r'\w+')
    result = tokenizer.tokenize(text.lower())
    ponctuations = set(list(punctuation))
    list_to_frequency=list()
    n_grams = ngrams(result, n_words)
    for grams in n_grams:
        if ' '.join(grams) not in ponctuations:
            list_to_frequency.append(' '.join(grams))
            if ' '.join(grams) not in vocabulary_grams:
                vocabulary_grams.append(' '.join(grams))
                

    frequency = FreqDist(list_to_frequency)
    return frequency

def main():

    text1 = "Falar é fácil. Mostre-me o código."
    text2 = "É fácil escrever código. Difícil é escrever código que funcione."
    
    n_grams = 1
    vocabulary = list()
    f3 = get_ngrams(text1, n_grams, vocabulary)
    f4 = get_ngrams(text2, n_grams, vocabulary)
    l3 = frequency_by_vocab(text1, vocabulary, n_grams)
    l4 = frequency_by_vocab(text2, vocabulary, n_grams)
    print()
    print("1-gram")
    print("Texto 1", l3)
    print("Texto 2", l4)


    vocabulary_grams = list()
    n_grams = 2
    
    f1 = get_ngrams(text1, n_grams, vocabulary_grams)
    f2 = get_ngrams(text2, n_grams, vocabulary_grams)
    l1 = frequency_by_vocab(text2, vocabulary_grams, n_grams)
    l2 = frequency_by_vocab(text2, vocabulary_grams, n_grams)
    print()
    print("2-gram")
    print(f1.tabulate)
    print(f2.tabulate)
    print("Texto1: ",l1)
    print("Texto2: ",l2)
    
    
    vocabulary_grams = list()
    n_grams = 3
    
    f1 = get_ngrams(text1, n_grams, vocabulary_grams)
    f2 = get_ngrams(text2, n_grams, vocabulary_grams)
    l1 = frequency_by_vocab(text2, vocabulary_grams, n_grams)
    l2 = frequency_by_vocab(text2, vocabulary_grams, n_grams)
    print()
    print("3-gram")
    print(f1.tabulate)
    print(f2.tabulate)
    print("Texto1: ",l1)
    print("Texto2: ",l2)


if __name__ == "__main__":
    main()
import nltk

from nltk import ngrams
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest
from string import punctuation




def raw_text_frequency_and_vocab(text, vocabulary):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text.lower())
    
    # words = word_tokenize(text.lower())
    stopwords_table = set(list(punctuation))
    list_to_frequency=list()
    for wd in words:
        if wd not in stopwords_table:
            list_to_frequency.append(wd)
            if wd not in vocabulary:
                vocabulary.append(wd)
    frequency = FreqDist(list_to_frequency)
    return frequency

def clean_text_frequency_and_vocab(text, vocabulary):
    frequency = FreqDist(text)
    return frequency

def without_stop_words(text, vocabulary):
    wrds = word_tokenize(text.lower())
    words_free=list()
    stopwords_table = set(stopwords.words('portuguese') + list(punctuation))
    for wd in wrds:
        if wd not in stopwords_table:
            words_free.append(wd)
    
    frequency = FreqDist(words_free)
    return frequency

def vocabulary_relation(text_frequency, vocabulary):
    table = list()
    for wd in vocabulary:
        if wd in text_frequency:
            table.append(text_frequency[wd])
        else:
            table.append(0)

    return table

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

def vocabulary_in_n_grams(vocabulary, n_grams):    
    vocab_linked = ' '.join(vocabulary)
    n_grams = ngrams(nltk.word_tokenize(vocab_linked), n_grams)
    return [ ' '.join(grams) for grams in n_grams]

def main():

    text1 = "Falar é fácil. Mostre-me o código."
    text2 = "É fácil escrever código. Difícil é escrever código que funcione."

    vocabulary = list()

    frequency1 = raw_text_frequency_and_vocab(text1, vocabulary)
    frequency2 = raw_text_frequency_and_vocab(text2, vocabulary)
    relation1 = vocabulary_relation(frequency1, vocabulary)
    relation2 = vocabulary_relation(frequency2, vocabulary)

    

    vocabulary_grams = vocabulary_in_n_grams(vocabulary, 2)
    
    frequency3 = get_ngrams(text1, 2, vocabulary_grams)
    frequency4 = get_ngrams(text2, 2, vocabulary_grams)
    relation3 = vocabulary_relation(frequency3, vocabulary_grams)
    relation4 = vocabulary_relation(frequency4, vocabulary_grams)

    print(vocabulary_grams)
    print(vocabulary)
    # frequency1.tabulate()
    # frequency2.tabulate()
    # print(relation1)
    # print(relation2)
    
    # somar o vocabulario e depois passar a tabulação de 2 em 2 elementos
    
    frequency3.tabulate()
    frequency4.tabulate()
    print(relation3)
    print(relation4)

if __name__ == "__main__":
    main()


# O código mantém a órdem das palavras a medida que vai encontrando-as no texto.
# Decidi fazer assim, pois foi o que entendi da especificação, mas poderia facilmente
# ordená-las de forma alfabética.
# O código tem duas funções, uma realiza a separação das palavras sem ignorar as stop-words,
# já a outra realiza a seleção do vocabuário e recorrências, ignorando-as.
# Ao pesquisar, busquei uma maneira que fosse mais otmizada, caso o vocabulário crescece de 
# maneira exponencial, assim aproveitei da modularidade do python para tais funções.
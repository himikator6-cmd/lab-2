import time
import nltk
import snowballstemmer
import pymorphy2
from L1_Modules import text_cleaner as tc
from L1_Modules import universal_preprocessor as up


def Space_Learning_Tokenizer(text):
    cleaned_text = tc.cleaner(text)
    Tokens = cleaned_text.split(' ')
    Vocabulary = list(set(Tokens))
    return Tokens, Vocabulary

def Space_Tokenizer(text, Vocabulary):
    Stime = time.time()
    cleaned_text = tc.cleaner(text)
    Tokens = cleaned_text.split(' ')
    Etime = time.time()
    Vtime = round(((Etime - Stime) / len(cleaned_text)) * 100000000) / 100
    OOV = 0
    for t in range(len(Tokens)):
        if (Tokens[t] not in Vocabulary):
            Tokens[t] = "[UNK]"
            OOV = OOV + 1
    OOV = (round((OOV / len(Tokens)) * 10000)) / 100        
    return Tokens, OOV, Vtime


def Space_Learning_Tokenizer_Stemming(text):
    stemmer = snowballstemmer.stemmer('russian');
    cleaned_text = tc.cleaner(text)
    Tokens = cleaned_text.split(' ')
    Tokens = stemmer.stemWords(Tokens)
    Vocabulary = list(set(Tokens))
    return Tokens, Vocabulary

def Space_Tokenizer_Stemming(text, Vocabulary):
    stemmer = snowballstemmer.stemmer('russian');
    Stime = time.time()
    cleaned_text = tc.cleaner(text)
    Tokens = cleaned_text.split(' ')
    Tokens = stemmer.stemWords(Tokens)
    Etime = time.time()
    Vtime = round(((Etime - Stime) / len(cleaned_text)) * 100000000) / 100
    OOV = 0
    for t in range(len(Tokens)):
        if (Tokens[t] not in Vocabulary):
            Tokens[t] = "[UNK]"
            OOV = OOV + 1
    OOV = (round((OOV / len(Tokens)) * 10000)) / 100        
    return Tokens, OOV, Vtime


def Space_Learning_Tokenizer_Lemmatization(text):
    morph = pymorphy2.MorphAnalyzer(lang = 'ru')
    cleaned_text = tc.cleaner(text)
    Tokens = cleaned_text.split(' ')
    for t in range(len(Tokens)):
        Tokens[t] = (morph.parse(Tokens[t])[0]).normal_form
    Vocabulary = list(set(Tokens))
    return Tokens, Vocabulary

def Space_Tokenizer_Lemmatization(text, Vocabulary):
    morph = pymorphy2.MorphAnalyzer(lang = 'ru')
    Stime = time.time()
    cleaned_text = tc.cleaner(text)
    Tokens = cleaned_text.split(' ')
    for t in range(len(Tokens)):
        Tokens[t] = (morph.parse(Tokens[t])[0]).normal_form
    Etime = time.time()
    Vtime = round(((Etime - Stime) / len(cleaned_text)) * 100000000) / 100
    OOV = 0
    for t in range(len(Tokens)):
        if (Tokens[t] not in Vocabulary):
            Tokens[t] = "[UNK]"
            OOV = OOV + 1
    OOV = (round((OOV / len(Tokens)) * 10000)) / 100        
    return Tokens, OOV, Vtime


def Space_Preprocessed_Learning_Tokenizer(text):
    cleaned_text = tc.cleaner(text)
    preprocessed_text = up.preprocessor(cleaned_text)
    Tokens = preprocessed_text.split(' ')
    Vocabulary = list(set(Tokens))
    return Tokens, Vocabulary

def Space_Preprocessed_Tokenizer(text, Vocabulary):
    Stime = time.time()
    cleaned_text = tc.cleaner(text)
    preprocessed_text = up.preprocessor(cleaned_text)
    Tokens = preprocessed_text.split(' ')
    Etime = time.time()
    Vtime = round(((Etime - Stime) / len(cleaned_text)) * 100000000) / 100
    OOV = 0
    for t in range(len(Tokens)):
        if (Tokens[t] not in Vocabulary):
            Tokens[t] = "[UNK]"
            OOV = OOV + 1
    OOV = (round((OOV / len(Tokens)) * 10000)) / 100        
    return Tokens, OOV, Vtime


def Space_Preprocessed_Learning_Tokenizer_Stemming(text):
    stemmer = snowballstemmer.stemmer('russian');
    cleaned_text = tc.cleaner(text)
    preprocessed_text = up.preprocessor(cleaned_text)
    Tokens = preprocessed_text.split(' ')
    Tokens = stemmer.stemWords(Tokens)
    Vocabulary = list(set(Tokens))
    return Tokens, Vocabulary

def Space_Preprocessed_Tokenizer_Stemming(text, Vocabulary):
    stemmer = snowballstemmer.stemmer('russian');
    Stime = time.time()
    cleaned_text = tc.cleaner(text)
    preprocessed_text = up.preprocessor(cleaned_text)
    Tokens = preprocessed_text.split(' ')
    Tokens = stemmer.stemWords(Tokens)
    Etime = time.time()
    Vtime = round(((Etime - Stime) / len(cleaned_text)) * 100000000) / 100
    OOV = 0
    for t in range(len(Tokens)):
        if (Tokens[t] not in Vocabulary):
            Tokens[t] = "[UNK]"
            OOV = OOV + 1
    OOV = (round((OOV / len(Tokens)) * 10000)) / 100        
    return Tokens, OOV, Vtime


def Space_Preprocessed_Learning_Tokenizer_Lemmatization(text):
    morph = pymorphy2.MorphAnalyzer(lang = 'ru')
    cleaned_text = tc.cleaner(text)
    preprocessed_text = up.preprocessor(cleaned_text)
    Tokens = preprocessed_text.split(' ')
    for t in range(len(Tokens)):
        Tokens[t] = (morph.parse(Tokens[t])[0]).normal_form
    Vocabulary = list(set(Tokens))
    return Tokens, Vocabulary

def Space_Preprocessed_Tokenizer_Lemmatization(text, Vocabulary):
    morph = pymorphy2.MorphAnalyzer(lang = 'ru')
    Stime = time.time()
    cleaned_text = tc.cleaner(text)
    preprocessed_text = up.preprocessor(cleaned_text)
    Tokens = preprocessed_text.split(' ')
    for t in range(len(Tokens)):
        Tokens[t] = (morph.parse(Tokens[t])[0]).normal_form
    Etime = time.time()
    Vtime = round(((Etime - Stime) / len(cleaned_text)) * 100000000) / 100
    OOV = 0
    for t in range(len(Tokens)):
        if (Tokens[t] not in Vocabulary):
            Tokens[t] = "[UNK]"
            OOV = OOV + 1
    OOV = (round((OOV / len(Tokens)) * 10000)) / 100        
    return Tokens, OOV, Vtime


def NLTK_Word_Learning_Tokenizer(text):
    cleaned_text = tc.cleaner(text)
    Tokens = nltk.word_tokenize(cleaned_text)
    Vocabulary = list(set(Tokens))
    return Tokens, Vocabulary

def NLTK_Word_Tokenizer(text, Vocabulary):
    Stime = time.time()
    cleaned_text = tc.cleaner(text)
    Tokens = nltk.word_tokenize(cleaned_text)
    Etime = time.time()
    Vtime = round(((Etime - Stime) / len(cleaned_text)) * 100000000) / 100
    OOV = 0
    for t in range(len(Tokens)):
        if (Tokens[t] not in Vocabulary):
            Tokens[t] = "[UNK]"
            OOV = OOV + 1
    OOV = (round((OOV / len(Tokens)) * 10000)) / 100        
    return Tokens, OOV, Vtime


def NLTK_Word_Learning_Tokenizer_Stemming(text):
    stemmer = snowballstemmer.stemmer('russian');
    cleaned_text = tc.cleaner(text)
    Tokens = nltk.word_tokenize(cleaned_text)
    Tokens = stemmer.stemWords(Tokens)
    Vocabulary = list(set(Tokens))
    return Tokens, Vocabulary

def NLTK_Word_Tokenizer_Stemming(text, Vocabulary):
    stemmer = snowballstemmer.stemmer('russian');
    Stime = time.time()
    cleaned_text = tc.cleaner(text)
    Tokens = nltk.word_tokenize(cleaned_text)
    Tokens = stemmer.stemWords(Tokens)
    Etime = time.time()
    Vtime = round(((Etime - Stime) / len(cleaned_text)) * 100000000) / 100
    OOV = 0
    for t in range(len(Tokens)):
        if (Tokens[t] not in Vocabulary):
            Tokens[t] = "[UNK]"
            OOV = OOV + 1
    OOV = (round((OOV / len(Tokens)) * 10000)) / 100        
    return Tokens, OOV, Vtime


def NLTK_Word_Learning_Tokenizer_Lemmatization(text):
    morph = pymorphy2.MorphAnalyzer(lang = 'ru')
    cleaned_text = tc.cleaner(text)
    Tokens = nltk.word_tokenize(cleaned_text)
    for t in range(len(Tokens)):
        Tokens[t] = (morph.parse(Tokens[t])[0]).normal_form
    Vocabulary = list(set(Tokens))
    return Tokens, Vocabulary

def NLTK_Word_Tokenizer_Lemmatization(text, Vocabulary):
    morph = pymorphy2.MorphAnalyzer(lang = 'ru')
    Stime = time.time()
    cleaned_text = tc.cleaner(text)
    Tokens = nltk.word_tokenize(cleaned_text)
    for t in range(len(Tokens)):
        Tokens[t] = (morph.parse(Tokens[t])[0]).normal_form
    Etime = time.time()
    Vtime = round(((Etime - Stime) / len(cleaned_text)) * 100000000) / 100
    OOV = 0
    for t in range(len(Tokens)):
        if (Tokens[t] not in Vocabulary):
            Tokens[t] = "[UNK]"
            OOV = OOV + 1
    OOV = (round((OOV / len(Tokens)) * 10000)) / 100        
    return Tokens, OOV, Vtime

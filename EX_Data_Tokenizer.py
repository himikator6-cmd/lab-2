import json
from L1_Modules import text_cleaner as tc
from L1_Modules import word_tokenizers as wt


FTR1 = 'Train_Samplings/train1.jsonl'
FTR2 = 'Train_Samplings/train2.jsonl'
FTR3 = 'Train_Samplings/train3.jsonl'
FTR4 = 'Train_Samplings/train4.jsonl'
FTR5 = 'Train_Samplings/train5.jsonl'
FTR6 = 'Train_Samplings/train6.jsonl'
FTR7 = 'Train_Samplings/train7.jsonl'
FTR8 = 'Train_Samplings/train8.jsonl'
FTS1 = 'Test_Samplings/test1.jsonl'
FTS2 = 'Test_Samplings/test2.jsonl'
FTS3 = 'Test_Samplings/test3.jsonl'
FTS4 = 'Test_Samplings/test4.jsonl'
FTS5 = 'Test_Samplings/test5.jsonl'

FTR = [FTR1, FTR2, FTR3, FTR4, FTR5, FTR6, FTR7, FTR8]
FTS = [FTS1, FTS2, FTS3, FTS4, FTS5]


News = tc.read_jsonl_news_text(FTR[0])
for f in range(1, len(FTR)):
    News = News + tc.read_jsonl_news_text(FTR[f])
SPTLNews = []
for n in range(len(News)):
    if ((' '.join(wt.Space_Preprocessed_Learning_Tokenizer_Lemmatization(News[n])[0])) not in SPTLNews):
        SPTLNews.append(' '.join(wt.Space_Preprocessed_Learning_Tokenizer_Lemmatization(News[n])[0]))
with open('Tokenized_Train_Samplings/train_SPTL.jsonl', 'w', encoding = 'utf-8') as f:
    for article in SPTLNews:
        json_line = json.dumps(article, ensure_ascii = False)
        f.write(json_line + '\n')


News = tc.read_jsonl_news_text(FTS[0])
for f in range(1, len(FTS)):
    News = News + tc.read_jsonl_news_text(FTS[f])
SPTLNews = []
for n in range(len(News)):
    if ((' '.join(wt.Space_Preprocessed_Learning_Tokenizer_Lemmatization(News[n])[0])) not in SPTLNews):
        SPTLNews.append(' '.join(wt.Space_Preprocessed_Learning_Tokenizer_Lemmatization(News[n])[0]))
with open('Tokenized_Test_Samplings/test_SPTL.jsonl', 'w', encoding = 'utf-8') as f:
    for article in SPTLNews:
        json_line = json.dumps(article, ensure_ascii = False)
        f.write(json_line + '\n')


Culture = tc.read_jsonl_news_text(FTS[0], category = 'Культура')
Sport = tc.read_jsonl_news_text(FTS[0], category = 'Спорт')
Travel = tc.read_jsonl_news_text(FTS[0], category = 'Путешествия')
for f in range(1, len(FTS)):
    Culture = Culture + tc.read_jsonl_news_text(FTS[f], category = 'Культура')
    Sport = Sport + tc.read_jsonl_news_text(FTS[f], category = 'Спорт')
    Travel = Travel + tc.read_jsonl_news_text(FTS[f], category = 'Путешествия')
SPTLCulture = []
SPTLSport = []
SPTLTravel = []
for n in range(len(Culture)):
    if ((' '.join(wt.Space_Preprocessed_Learning_Tokenizer_Lemmatization(Culture[n])[0])) not in SPTLCulture):
        SPTLCulture.append(' '.join(wt.Space_Preprocessed_Learning_Tokenizer_Lemmatization(Culture[n])[0]))
for n in range(len(Sport)):
    if ((' '.join(wt.Space_Preprocessed_Learning_Tokenizer_Lemmatization(Sport[n])[0])) not in SPTLSport):
        SPTLSport.append(' '.join(wt.Space_Preprocessed_Learning_Tokenizer_Lemmatization(Sport[n])[0]))
for n in range(len(Travel)):
    if ((' '.join(wt.Space_Preprocessed_Learning_Tokenizer_Lemmatization(Travel[n])[0])) not in SPTLTravel):
        SPTLTravel.append(' '.join(wt.Space_Preprocessed_Learning_Tokenizer_Lemmatization(Travel[n])[0]))
with open('Tokenized_Test_Samplings/test_culture_SPTL.jsonl', 'w', encoding = 'utf-8') as f:
    for article in SPTLCulture:
        json_line = json.dumps(article, ensure_ascii = False)
        f.write(json_line + '\n')
with open('Tokenized_Test_Samplings/test_sport_SPTL.jsonl', 'w', encoding = 'utf-8') as f:
    for article in SPTLSport:
        json_line = json.dumps(article, ensure_ascii = False)
        f.write(json_line + '\n')
with open('Tokenized_Test_Samplings/test_travel_SPTL.jsonl', 'w', encoding = 'utf-8') as f:
    for article in SPTLTravel:
        json_line = json.dumps(article, ensure_ascii = False)
        f.write(json_line + '\n')

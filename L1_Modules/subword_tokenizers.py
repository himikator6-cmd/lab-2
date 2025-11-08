import time
import tokenizers
from L1_Modules import text_cleaner as tc
from L1_Modules import universal_preprocessor as up


def BPE_Learning_Tokenizer(text, Voc_Size, Min_Freq):
    cleaned_text = tc.cleaner(text)
    cleaned_text = cleaned_text.replace('? ', '. ')
    cleaned_text = cleaned_text.replace('! ', '. ')
    sentences = cleaned_text.split('. ')
    for s in range(len(sentences) - 1):
        sentences[s] = sentences[s] + "."
    tokenizer = tokenizers.Tokenizer(tokenizers.models.BPE(unk_token = "[UNK]"))
    tokenizer.pre_tokenizer = tokenizers.pre_tokenizers.Whitespace()
    Trainer = tokenizers.trainers.BpeTrainer(vocab_size = Voc_Size, min_frequency = Min_Freq, special_tokens = ["[UNK]"])
    tokenizer.train_from_iterator(sentences, trainer = Trainer)
    return tokenizer


def WordPiece_Learning_Tokenizer(text, Voc_Size, Min_Freq):
    cleaned_text = tc.cleaner(text)
    cleaned_text = cleaned_text.replace('? ', '. ')
    cleaned_text = cleaned_text.replace('! ', '. ')
    sentences = cleaned_text.split('. ')
    for s in range(len(sentences) - 1):
        sentences[s] = sentences[s] + "."
    tokenizer = tokenizers.Tokenizer(tokenizers.models.WordPiece(unk_token = "[UNK]"))
    tokenizer.pre_tokenizer = tokenizers.pre_tokenizers.Whitespace()
    Trainer = tokenizers.trainers.WordPieceTrainer(vocab_size = Voc_Size, min_frequency = Min_Freq, special_tokens = ["[UNK]"])
    tokenizer.train_from_iterator(sentences, trainer = Trainer)
    return tokenizer


def Tokenizer(text, tokenizer):
    Stime = time.time()
    cleaned_text = tc.cleaner(text)
    encoded_text = tokenizer.encode(cleaned_text)
    Etime = time.time()
    Vtime = round(((Etime - Stime) / len(cleaned_text)) * 100000000) / 100
    Tokens = encoded_text.tokens
    Words1 = cleaned_text.split(' ')
    preprocessed_text = up.clean_punctuation(cleaned_text)
    Words2 = preprocessed_text.split(' ')
    K = 0
    for w in Words2:
        if (len(tokenizer.encode(w).tokens) > 1):
            K = K + 1
    VS = tokenizer.get_vocab_size()
    FR = round((K / len(Words1)) * 10000) / 100
    CR = round((len(cleaned_text) / len(Tokens)) * 100) / 100
    return Tokens, VS, FR, CR, Vtime

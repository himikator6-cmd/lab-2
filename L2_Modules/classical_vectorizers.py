

def One_Hot_Encodding_Learning(Documents):
    Tokens = Documents[0].split(' ')
    for d in range(1, len(Documents)):
        Tokens = Tokens + Documents[d].split(' ')
    Vocabulary = list(set(Tokens))
    Dictionary = {}
    for t in range(len(Vocabulary)):
        Vector = [0] * len(Vocabulary)
        Vector[t] = 1
        Dictionary[Vocabulary[t]] = Vector
    return Dictionary


def Bag_Of_Words_Learning(Documents):
    Tokens = Documents[0].split(' ')
    for d in range(1, len(Documents)):
        Tokens = Tokens + Documents[d].split(' ')
    Vocabulary = list(set(Tokens))
    Dictionary = {}
    for t in range(len(Vocabulary)):
        Dictionary[Vocabulary[t]] = t
    return Dictionary


def Bag_Of_Words(Dictionary, Document):
    Tokens = Document.split(' ')
    Vector = [0] * len(Dictionary)
    for t in Tokens:
        if t in Dictionary:
            Vector[Dictionary[t]] = Vector[Dictionary[t]] + 1
    return Vector
 

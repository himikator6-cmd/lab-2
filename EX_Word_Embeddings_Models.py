import pickle
from L2_Modules import technical_functions as tf
from L2_Modules import word_embeddings as we


Train = "Tokenized_Train_Samplings/train_SPTL.jsonl"


Traintext = tf.tokeinized_text_extractor(Train)
TrainSentences = [Traintext[0].split(' ')]
for t in range(1, len(Traintext)):
    TrainSentences.append(Traintext[t].split(' '))


WSGModel = we.W2V_Skip_gram(TrainSentences, 100, 5)
with open("Models/W2V_Skip_gram_100_5.pkl", 'wb') as f:
    pickle.dump(WSGModel, f)


WSGModel = we.W2V_Skip_gram(TrainSentences, 100, 8)
with open("Models/W2V_Skip_gram_100_8.pkl", 'wb') as f:
    pickle.dump(WSGModel, f)


WSGModel = we.W2V_Skip_gram(TrainSentences, 100, 10)
with open("Models/W2V_Skip_gram_100_10.pkl", 'wb') as f:
    pickle.dump(WSGModel, f)


WSGModel = we.W2V_Skip_gram(TrainSentences, 200, 5)
with open("Models/W2V_Skip_gram_200_5.pkl", 'wb') as f:
    pickle.dump(WSGModel, f)


WSGModel = we.W2V_Skip_gram(TrainSentences, 200, 8)
with open("Models/W2V_Skip_gram_200_8.pkl", 'wb') as f:
    pickle.dump(WSGModel, f)


WSGModel = we.W2V_Skip_gram(TrainSentences, 200, 10)
with open("Models/W2V_Skip_gram_200_10.pkl", 'wb') as f:
    pickle.dump(WSGModel, f)


WSGModel = we.W2V_Skip_gram(TrainSentences, 300, 5)
with open("Models/W2V_Skip_gram_300_5.pkl", 'wb') as f:
    pickle.dump(WSGModel, f)


WSGModel = we.W2V_Skip_gram(TrainSentences, 300, 8)
with open("Models/W2V_Skip_gram_300_8.pkl", 'wb') as f:
    pickle.dump(WSGModel, f)


WSGModel = we.W2V_Skip_gram(TrainSentences, 300, 10)
with open("Models/W2V_Skip_gram_300_10.pkl", 'wb') as f:
    pickle.dump(WSGModel, f)


WCBOWModel = we.W2V_CBOW(TrainSentences, 100, 5)
with open("Models/W2V_CBOW_100_5.pkl", 'wb') as f:
    pickle.dump(WCBOWModel, f)


WCBOWModel = we.W2V_CBOW(TrainSentences, 100, 8)
with open("Models/W2V_CBOW_100_8.pkl", 'wb') as f:
    pickle.dump(WCBOWModel, f)


WCBOWModel = we.W2V_CBOW(TrainSentences, 100, 10)
with open("Models/W2V_CBOW_100_10.pkl", 'wb') as f:
    pickle.dump(WCBOWModel, f)


WCBOWModel = we.W2V_CBOW(TrainSentences, 200, 5)
with open("Models/W2V_CBOW_200_5.pkl", 'wb') as f:
    pickle.dump(WCBOWModel, f)


WCBOWModel = we.W2V_CBOW(TrainSentences, 200, 8)
with open("Models/W2V_CBOW_200_8.pkl", 'wb') as f:
    pickle.dump(WCBOWModel, f)


WCBOWModel = we.W2V_CBOW(TrainSentences, 200, 10)
with open("Models/W2V_CBOW_200_10.pkl", 'wb') as f:
    pickle.dump(WCBOWModel, f)


WCBOWModel = we.W2V_CBOW(TrainSentences, 300, 5)
with open("Models/W2V_CBOW_300_5.pkl", 'wb') as f:
    pickle.dump(WCBOWModel, f)


WCBOWModel = we.W2V_CBOW(TrainSentences, 300, 8)
with open("Models/W2V_CBOW_300_8.pkl", 'wb') as f:
    pickle.dump(WCBOWModel, f)


WCBOWModel = we.W2V_CBOW(TrainSentences, 300, 10)
with open("Models/W2V_CBOW_300_10.pkl", 'wb') as f:
    pickle.dump(WCBOWModel, f)


FSGModel = we.Fasttext_Skip_gram(TrainSentences, 100, 5)
with open("Models/Fasttext_Skip_gram_100_5.pkl", 'wb') as f:
    pickle.dump(FSGModel, f)


FSGModel = we.Fasttext_Skip_gram(TrainSentences, 100, 8)
with open("Models/Fasttext_Skip_gram_100_8.pkl", 'wb') as f:
    pickle.dump(FSGModel, f)


FSGModel = we.Fasttext_Skip_gram(TrainSentences, 100, 10)
with open("Models/Fasttext_Skip_gram_100_10.pkl", 'wb') as f:
    pickle.dump(FSGModel, f)


FSGModel = we.Fasttext_Skip_gram(TrainSentences, 200, 5)
with open("Models/Fasttext_Skip_gram_200_5.pkl", 'wb') as f:
    pickle.dump(FSGModel, f)


FSGModel = we.Fasttext_Skip_gram(TrainSentences, 200, 8)
with open("Models/Fasttext_Skip_gram_200_8.pkl", 'wb') as f:
    pickle.dump(FSGModel, f)


FSGModel = we.Fasttext_Skip_gram(TrainSentences, 200, 10)
with open("Models/Fasttext_Skip_gram_200_10.pkl", 'wb') as f:
    pickle.dump(FSGModel, f)


FSGModel = we.Fasttext_Skip_gram(TrainSentences, 300, 5)
with open("Models/Fasttext_Skip_gram_300_5.pkl", 'wb') as f:
    pickle.dump(FSGModel, f)


FSGModel = we.Fasttext_Skip_gram(TrainSentences, 300, 8)
with open("Models/Fasttext_Skip_gram_300_8.pkl", 'wb') as f:
    pickle.dump(FSGModel, f)


FSGModel = we.Fasttext_Skip_gram(TrainSentences, 300, 10)
with open("Models/Fasttext_Skip_gram_300_10.pkl", 'wb') as f:
    pickle.dump(FSGModel, f)


FCBOWModel = we.Fasttext_CBOW(TrainSentences, 100, 5)
with open("Models/Fasttext_CBOW_100_5.pkl", 'wb') as f:
    pickle.dump(FCBOWModel, f)


FCBOWModel = we.Fasttext_CBOW(TrainSentences, 100, 8)
with open("Models/Fasttext_CBOW_100_8.pkl", 'wb') as f:
    pickle.dump(FCBOWModel, f)


FCBOWModel = we.Fasttext_CBOW(TrainSentences, 100, 10)
with open("Models/Fasttext_CBOW_100_10.pkl", 'wb') as f:
    pickle.dump(FCBOWModel, f)


FCBOWModel = we.Fasttext_CBOW(TrainSentences, 200, 5)
with open("Models/Fasttext_CBOW_200_5.pkl", 'wb') as f:
    pickle.dump(FCBOWModel, f)


FCBOWModel = we.Fasttext_CBOW(TrainSentences, 200, 8)
with open("Models/Fasttext_CBOW_200_8.pkl", 'wb') as f:
    pickle.dump(FCBOWModel, f)


FCBOWModel = we.Fasttext_CBOW(TrainSentences, 200, 10)
with open("Models/Fasttext_CBOW_200_10.pkl", 'wb') as f:
    pickle.dump(FCBOWModel, f)


FCBOWModel = we.Fasttext_CBOW(TrainSentences, 300, 5)
with open("Models/Fasttext_CBOW_300_5.pkl", 'wb') as f:
    pickle.dump(FCBOWModel, f)


FCBOWModel = we.Fasttext_CBOW(TrainSentences, 300, 8)
with open("Models/Fasttext_CBOW_300_8.pkl", 'wb') as f:
    pickle.dump(FCBOWModel, f)


FCBOWModel = we.Fasttext_CBOW(TrainSentences, 300, 10)
with open("Models/Fasttext_CBOW_300_10.pkl", 'wb') as f:
    pickle.dump(FCBOWModel, f)



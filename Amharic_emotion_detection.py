import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from amharic_stop_words import *
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score
np.random.seed(500)
Corpus = pd.read_csv("amharic_emotions_ds.csv")
#print(Corpus.head())
Corpus['text'].dropna(inplace=True)
Corpus['text']= [word_tokenize(entry) for entry in Corpus['text']]
c = Corpus['text']

for index,entry in enumerate(Corpus['text']):
    Final_words = []
    for word in entry:
     if(stop_word_check(word)==False):
        Final_words.append(word)
    Corpus.loc[index,'text_final']=str(Final_words)

Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(Corpus['text_final'],Corpus['label'],test_size=0.3)
Encoder = LabelEncoder()

Train_Y = Encoder.fit_transform(Train_Y)
Test_Y = Encoder.fit_transform(Test_Y)
Tfidf_vect = TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(Corpus['text_final'])
p = Corpus['text_final']
Train_X_Tfidf = Tfidf_vect.transform(Train_X)
Test_X_Tfidf = Tfidf_vect.transform(Test_X)
#print("A vocabulary")
#print(Tfidf_vect.vocabulary_)

#print('\n'.join(Tfidf_vect.vocabulary_))

#print(Train_X_Tfidf)
Naive = naive_bayes.MultinomialNB()
Naive.fit(Train_X_Tfidf,Train_Y)# predict the labels on validation dataset
predictions_NB = Naive.predict(Test_X_Tfidf)# Use accuracy_score function to get the accuracy
#print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, Test_Y)*100)
SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(Train_X_Tfidf,Train_Y)# predict the labels on validation dataset
predictions_SVM = SVM.predict(Test_X_Tfidf)# Use accuracy_score function to get the accuracy
#print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, Test_Y)*100)
print("Test data ")
print(list(Test_X)[37])
print("Vectorized form of our test data ")
print(Test_X_Tfidf[37])


print("Pridiction Result")

s_word = "ተደሰትኩ ሳቅኩ ደስ_አለኝ እርካታ "
s_tokenized = word_tokenize(s_word)
s = ""+str(s_tokenized).strip()+""
ds_form = [110000,s_tokenized]
id = 13332

r = []
r.append(s_tokenized)
#s = (id,s_tokenized)
ser = pd.Series(id,s_tokenized)
v = Tfidf_vect.transform(s_tokenized)



#h_feature = vectorizer_happy.fit_transform(Train_X.split())
#d = {h_feature,vectorizer_happy}
#s = p.DataFrame(data=d)
print("$$$$$$$$$ vvv")
print(v)

#print(s)
#happy = vectorizer_happy.fit_transform([s_word,list(Corpus['text_final'])])
print(v)


pred = SVM.predict(Test_X_Tfidf[37])

if(pred[0]==0):
    print("Happy")
elif(pred[0]==1):
    print("Sad")
elif(pred[0]==2):
    print("Anger")
else:
    print("Surprise")


#print(test_data_vect)


#print(predictions_SVM(test_data_vect))

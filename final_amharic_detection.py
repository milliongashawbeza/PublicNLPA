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
import enum
from add_emotion_text import *
#from sklearn.externals import joblib
word_text = input("Please enter an Amharic Text :\n")
add_dataset("",word_text)
if(len(word_text)>0):
    np.random.seed(500)
    Corpus = pd.read_csv("amharic_emotions_ds.csv")
    Prediction_Ds = pd.read_csv("amharic_emotions_ds.csv")

    #print(Corpus.head())
    Corpus['text'].dropna(inplace=True)
    Corpus['text'] = [word_tokenize(entry) for entry in Corpus['text']]


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
    a_new_word = ""+str(word_tokenize(word_text))+""
    Test_a_new_word = ("999", str(a_new_word))
    #Test_a_new_word = ("89", "['ከመላው', 'ዓለም', 'ፍቅር', 'እንዳላት', 'ተሰማት']")
    Encode_a_new_word=Encoder.fit_transform(Test_a_new_word)



    Tfidf_vect = TfidfVectorizer(max_features=5000)

    Tfidf_vect.fit(Corpus['text_final'])

    Train_X_Tfidf = Tfidf_vect.transform(Train_X)
    Test_X_Tfidf = Tfidf_vect.transform(Test_X)
    #Tfidf for the new word
    Tdidf_of_a_new_word= Tfidf_vect.transform(Test_a_new_word)
    print("************")
    print(Tdidf_of_a_new_word)

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
    tok = word_tokenize(word_text)





    s_word = "ተደሰትኩ ሳቅኩ ደስ_አለኝ እርካታ"
    print(word_text)




    #print(s)
    #happy = vectorizer_happy.fit_transform([s_word,list(Corpus['text_final'])])


    print("Pridiction of a new word")
    pred = SVM.predict(Tdidf_of_a_new_word)

    print(pred)



    if(pred[1]==1):
        print("Happy")
    elif(pred[1]==2):
        print("Sad")
    elif(pred[1]==3):
        print("Surprise")
    else:
        print("Angry")



    #print(test_data_vect)


    #print(predictions_SVM(test_data_vect))

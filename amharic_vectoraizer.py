from sklearn.feature_extraction.text import TfidfVectorizer
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
s_happy = "ተደሰትኩ ሳቅኩ ደስ_አለኝ እርካታ"
s_sad = "ተናደድኩ አለቀስኩ"
s_surprise = "ተደነቅኩ ተገረምኩ ያስገርማል ያስደንቃል"
s_anger = "አስጸያፊ ተጸየፍኩ ጠበኛ በቁጣ ተናደደ ተነዳድኩ ተቆጣሁ ተቆጣ ተቆጣች "
sentence = "ዛሬ በጣም ተደሰትኩ አስጸያፊ ተጸየፍኩ ጠበኛ በቁጣ ተናደደ ተነዳድኩ ተቆጣሁ ተቆጣ ተቆጣች"
Corpus = pd.read_csv("amharic_emotions_ds.csv")
np.random.seed(500)

Corpus['text'].dropna(inplace=True)
Corpus['text'] = [word_tokenize(entry) for entry in Corpus['text']]

print(Corpus['text'][0])
vectorizer_happy = TfidfVectorizer()
vectorizer_sad = TfidfVectorizer()
vectorizer_anger = TfidfVectorizer()
vectorizer_surprise = TfidfVectorizer()

h_feature = vectorizer_happy.fit_transform(sentence.split())
#d = {h_feature,vectorizer_happy}
#s = p.DataFrame(data=d)
print("$$$$$$$$$")

#print(s)
happy = vectorizer_happy.fit_transform([s_happy,sentence])
sad = vectorizer_sad.fit_transform([s_sad,sentence])
anger = vectorizer_anger.fit_transform([s_anger,sentence])
surprise = vectorizer_surprise.fit_transform([s_surprise,sentence])
print(vectorizer_happy.get_feature_names())
print("#######")
print(happy)
print(vectorizer_sad.get_feature_names())
print("#######")
print(sad)
print(vectorizer_anger.get_feature_names())
print("#######")
print(anger)
print(vectorizer_surprise.get_feature_names())
print("#######")
print(surprise)






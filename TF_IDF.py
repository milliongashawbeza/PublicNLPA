import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from mlxtend.feature_selection import ColumnSelector
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB



df_Xtrain = pd.DataFrame({'tweet': ['This is a tweet']*10,
                          'label': 0})
y_train = df_Xtrain['label'].to_numpy().ravel()

pipe = Pipeline([
    ('col_selector', ColumnSelector(cols=('tweet'),drop_axis=True)),
    ('tfidf', TfidfVectorizer()),
    ('bernoulli', BernoulliNB()),
])


pipe.fit(df_Xtrain,y_train)

Pipeline(steps=[('col_selector', ColumnSelector(cols='tweet', drop_axis=True)),
                ('tfidf', TfidfVectorizer()), ('bernoulli', BernoulliNB())])

from nltk.corpus import brown
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/home/milli/Desktop/NLPRes/amh_wikipedia_2016_30K/amh_wikipedia_2016_30K-words.txt'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
#tagged_token = nltk.tag.str2tuple('መሮጥ/NN')
#print(tagged_token)
#text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
#text.similar('woman')
#print(brown.words())
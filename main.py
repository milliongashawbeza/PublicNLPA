import string
from collections import Counter
import matplotlib.pyplot as plt
from amharic_bigram_generator import *
from amharic_punctuation_remover import *
from amharic_tokenizer import *
from amharic_stop_words import *
#Reading text
text = open("read.txt", encoding="utf-8").read()
clear_text = clear_amharic_sentence(text)
bigramm = bigramm(clear_text)
tokenized_word = word_tokenize(bigramm)

# Removing stop words from the tokenized words list
# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list

final_words=[]
for word in tokenized_word:
    if(stop_word_check(word)==False):
        final_words.append(word)

emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        #word, emotion = clear_line.split(':')
        d = clear_line.split(':')
        if d[0] in final_words:
            emotion_list.append(d[1])

print(emotion_list)
w = Counter(emotion_list)
print(w)

# Plotting the emotions on the graph

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()